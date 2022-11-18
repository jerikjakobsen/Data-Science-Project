import pandas as pd
import os

df = pd.read_csv(os.path.join('..', 'CSVFiles', 'FilteredListing+SaleData.csv'))

print(df.columns)
print(len(df))