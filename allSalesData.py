import dask.dataframe as dd

conn = "mysql+pymysql://root@localhost/us_housing_prices"

df = dd.read_sql_table(
                 table_name="sales",
                 con=conn,
                 index_col="sale_id")

print(df.head())