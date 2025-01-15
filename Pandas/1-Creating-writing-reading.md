DataFrame¶
A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row (or record) and a column.

For example, consider the following simple DataFrame:

![](../images/image_2025-01-15_213219972.png)

![](../images/image_2025-01-15_213300768.png)

![](../images/image_2025-01-15_213343131.png)

or to make a series we do this:

![](../images/image_2025-01-15_213444937.png)

### To read a DataFile

The pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify. For example, you can see in this dataset that the CSV file has a built-in index, which pandas did not pick up on automatically. To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.

![](../images/image_2025-01-15_213705558.png)

### To turn the data into csv file 

![](../images/image_2025-01-15_214228070.png)
