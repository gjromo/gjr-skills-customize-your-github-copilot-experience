import pandas as pd
import numpy as np

# Load a CSV file from the project
# Replace with your own dataset path if needed
# data = pd.read_csv('data.csv')

# Example dataset
scores = pd.Series([82, 91, 75, 88, 93, 80, 85])

# TODO: Calculate the mean, median, and mode
# TODO: Find the minimum and maximum values
# TODO: Compute the standard deviation
# TODO: Display the results clearly

print("Mean:", scores.mean())
print("Median:", scores.median())
print("Min:", scores.min())
print("Max:", scores.max())
