import pandas as pd
import sqlite3 as db
import zipfile as zip
import urllib.request as req

# Extract the data from the url
def extractData(url):
    zip_filename = 'mowesta-dataset.zip'
    data_filename = 'data.csv'
    req.urlretrieve(url, zip_filename)
    with zip.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall()
    return data_filename

# Transform the data into a dataframe
def transformData(file_name):
    df = pd.read_csv(file_name, sep=";", decimal=",", index_col=False,
                     usecols=["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)",
                              "Batterietemperatur in °C", "Geraet aktiv"])

    df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"},
              inplace=True)

    selected_columns = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur", "Batterietemperatur", "Geraet aktiv"]
    df = df[selected_columns]

    # Convert temperature units
    df['Temperatur'] = (df['Temperatur'] * 9 / 5) + 32
    df['Batterietemperatur'] = (df['Batterietemperatur'] * 9 / 5) + 32

    return df

# Validate the data
def validateData(df):
    return (
        df[df['Geraet'] > 0]
        .loc[df['Hersteller'].str.strip() != ""]
        .loc[df['Model'].str.strip() != ""]
        .loc[df['Monat'].between(1, 12)]
        .loc[pd.to_numeric(df['Temperatur'], errors='coerce').notnull()]
        .loc[pd.to_numeric(df['Batterietemperatur'], errors='coerce').notnull()]
        .loc[df['Geraet aktiv'].isin(['Ja', 'Nein'])]
    )

# Load data into database
def loadData(df, db_name, tb_name):
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {tb_name} (
            Geraet BIGINT, Hersteller TEXT, Model TEXT, Monat TEXT,
            Temperatur FLOAT, Batterietemperatur FLOAT, Geraet_aktiv TEXT)"""

    with db.connect(db_name) as conn:
        conn.execute(create_table_query)
        df.to_sql(tb_name, conn, if_exists='replace', index=False)

# Main execution
url = 'https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip'
extractedData = extractData(url)
transformedData = transformData(extractedData)
validatedData = validateData(transformedData)
db_name = 'temperatures.sqlite'
tb_name = 'temperatures'
loadData(validatedData, db_name, tb_name)
