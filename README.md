# PySpark Movie Reviews Analysis

## Project Overview
This project uses PySpark to process and analyze the IMDb Movie Review Dataset containing movie reviews labeled as positive or negative.

## Objectives
- Load the IMDb dataset using PySpark.
- Explore the dataset using schema and sample records.
- Remove null and empty reviews.
- Count total number of reviews.
- Count positive and negative reviews.
- Calculate the length of each review in characters.
- Filter reviews longer than 500 characters.
- Save the cleaned and transformed dataframe as CSV files.

## Technologies Used
- Python
- PySpark
- Apache Spark
- Git
- GitHub

## Dataset
IMDb Movie Review Dataset (50K reviews)

Dataset link: https://www.kaggle.com/datasets/lakshmi25npathi/imdb

The dataset is stored locally in the `data` folder and is not included in this repository.

## How to Run

1. Install Python and Java.
2. Install PySpark:

   ```bash
   pip install pyspark
   ```

3. Place `IMDB Dataset.csv` inside the `data` folder.
4. Run the program:

   ```bash
   python movie_reviews.py
   ```

## Output
The program displays:
- Dataset schema
- First five reviews
- Total number of reviews
- Positive and negative sentiment counts
- Review lengths
- Reviews longer than 500 characters

The cleaned and transformed dataset is saved in:

`output/cleaned_movie_reviews`

## Author
Akshatha N.