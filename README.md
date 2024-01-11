# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.
Before you begin, make sure you have [Python](https://www.python.org/) and [Jayvee](https://github.com/jvalue/jayvee) installed. We will work with [Jupyter notebooks](https://jupyter.org/). The easiest way to do so is to set up [VSCode](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).


## Project Work
Knowing unemployment trends in a socioeconomic setting is crucial for making wise policy choices. The main goal of this study is to provide a thorough examination of East and West German unemployment statistics. Finding patterns, contrasting regional differences, and drawing conclusions that further a sophisticated knowledge of the dynamics of unemployment in the two areas are the main goals. This study has investigated the following important areas:

1. **Comparative Analysis of Unemployment Trends (2018-2023)**:
   - Investigating the historical trends of unemployment in East and West Germany.
   - Identifying key factors contributing to variations in unemployment rates between the two regions.

2. **Monthly and Seasonal Variations in Unemployment Rates**:
   - Analyzing how unemployment rates fluctuate on a monthly and seasonal basis.
   - Exploring the impact of specific months or seasons on regional unemployment patterns.

3. **Demographic Correlations**:
   - Investigating correlations between unemployment rates and demographic factors.
   - Analyzing gender-specific unemployment trends and disparities in both regions.

4. **Predictive Analysis and Future Trends**:
   - Employing predictive modeling to forecast potential future unemployment trends.
   - Providing insights into factors that may influence future employment dynamics.

Policymakers, researchers, and anybody else seeking to learn more about the economic conditions in East and West Germany might find this project report to be an extensive resource. The detailed findings presents the specific conclusions and suggestions, providing insightful viewpoints on the dynamics of regional unemployment.

I cordially encourage you to explore the in-depth analysis provided in this project [[Report]](project/report.ipynb). The purpose of the study is to support well-informed decision-making and strategies for resolving issues related to unemployment in various German regions.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises, sometimes using [Python](https://www.python.org/), sometimes using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.<jv or py>`.

In regular intervalls, exercises will be given as homework to complete during the semester. We will divide you into two groups, one completing an exercise in Jayvee, the other in Python, switching each exercise. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv` or `./exercises/exercise1.py`
2. `./exercises/exercise2.jv` or `./exercises/exercise2.py`
3. `./exercises/exercise3.jv` or `./exercises/exercise3.py`
4. `./exercises/exercise4.jv` or `./exercises/exercise4.py`
5. `./exercises/exercise5.jv` or `./exercises/exercise5.py`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
