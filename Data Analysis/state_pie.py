import pandas as pd
import os

filteredDF = pd.read_csv(os.path.join('..', 'CSVFiles', 'FilteredListing+SaleData.csv'), index_col=0)

filteredDF.groupby(["State"]).size().plot(kind='pie', y= len(filteredDF), autopct='%1.0f%%' )


print(filteredDF.groupby(["State"]).describe())
print(filteredDF.groupby(["State"]).size())