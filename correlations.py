import pandas as pd

data = pd.read_csv(
    '/Users/shah/Documents/Data-Science-Project/CSVFiles/FilteredListing+SaleData.csv', sep=",")
print(data)

data.corr().to_csv(“correlations.csv”)
