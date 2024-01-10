import pandas as pd
from sqlalchemy import create_engine

def extract_data(url):
    """Extract data from a given URL.."""
    try:
        df = pd.read_html(url)[0][:-1]
        return df
    except Exception as e:
        raise Exception(f"Data extraction failed: {e}")

def transform_data(df, column_map, col_to_drop):
    """Transform data by renaming and dropping columns."""
    try:
        df = df.copy()
        df.rename(columns=column_map, inplace=True)
        df.drop(columns=col_to_drop, inplace=True)
       
       # Convert 'male' and 'female' to numeric
        df['male'] = pd.to_numeric(df['male'], errors='coerce')
        df['female'] = pd.to_numeric(df['female'], errors='coerce')

        # Convert 'month' to a number only if it's not already numeric
        if df['month'].dtype == 'object':
            df['month'] = df['month'].apply(month_to_number)

        # Extract year from 'year' column (if it's a datetime type)
        if pd.api.types.is_datetime64_any_dtype(df['year']):
            df['year'] = df['year'].dt.year
       
        return df
    except Exception as e:
        raise Exception(f"Data transformation failed: {e}")

# Function to convert month name to number
def month_to_number(month_name):
    month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 
                  'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    return month_dict[month_name]


def load_data(df, table):
    """Load data into a SQLite database."""
    try:
        engine = create_engine("sqlite:///./data/unemployed.sqlite")
        df.to_sql(table, engine, if_exists="replace")
    except Exception as e:
        raise Exception(f"Data loading failed: {e}")


def main():
    # Common Column Map and Columns to Drop
    column_map = {'Year, month': 'year', 'Year, month.1': 'month',
                  'Total': 'total', 'Male': 'male', 'Female': 'female',
                  'Juveniles of under 20 years of age': 'under_20_year_age',
                  'Long-term unemployed': 'long_term'}
    col_to_drop = ["total", "under_20_year_age", "long_term"]

    # URLs
    west_unemployed = "https://www.destatis.de/EN/Themes/Economy/Short-Term-Indicators/Labour-Market/arb120.html#241586"
    east_unemployed = "https://www.destatis.de/EN/Themes/Economy/Short-Term-Indicators/Labour-Market/arb130.html#241598"

    
    # Extract, Transform, and Load Data for West Unemployed
    df_west = extract_data(west_unemployed)
    df_west_transformed = transform_data(df_west, column_map, col_to_drop)
    load_data(df_west_transformed, "unemployed_west")

    # Extract, Transform, and Load Data for East Unemployed
    df_east = extract_data(east_unemployed)
    df_east_transformed = transform_data(df_east, column_map, col_to_drop)
    load_data(df_east_transformed, "unemployed_east")


if __name__ == "__main__":
    main()
