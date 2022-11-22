import pandas as pd
import sys
import os
filePath = sys.path[0] + "/CSVFiles/FilteredListing+SaleData.csv"
data = pd.read_csv(filePath, sep=",")
print(data)

data.corr().to_csv("correlations.csv")
