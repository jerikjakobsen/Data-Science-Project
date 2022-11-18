import pandas as pd
import os

filteredTruliaDF = pd.read_csv(os.path.join('..', 'CSVFiles', 'FilteredTruliaData.csv'), index_col=0)
filteredSalesDF = pd.read_csv(os.path.join('..', 'CSVFiles', 'FilteredSalesData.csv'), index_col=0)

def mergeSaleAndTruliaData(sales, trulia):
    dfJoined = sales.merge(trulia, on=["Address", "City", "State"])
    dfFiltered = dfJoined[dfJoined["listing_date"] < dfJoined["sale_date"]]
    dfFiltered = dfFiltered.sort_values('sale_date').drop_duplicates(["Address", "City", "State"], keep='first')
    return dfFiltered
dfFiltered = mergeSaleAndTruliaData(filteredSalesDF, filteredTruliaDF)
dfFiltered.to_csv('FilteredListing+SaleData.csv')