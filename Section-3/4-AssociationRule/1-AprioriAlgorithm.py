import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/content/Market_Basket_Optimisation.csv', header = None)

df_sample = df.head(500)
transactions = []
# Convert to transactions list
transactions = df_sample.apply(lambda row: [str(item) for item in row if str(item) != 'nan'], axis=1).tolist()

!pip install apyori

from apyori import apriori
rules = apriori(transactions= transactions, min_support = 0.004, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)
#min_support = ( 3 items atleast present * 7 days of the week ) / 500 transactions in data = 0.0042
#min_confidence = put as busniess required
#don't go below 3 for min_lift
#max and min length are set to 2 cos we are trying to find , best deals of buying
#product A and get product B as free

#displaying the first result coming directly from the output
results = list(rules)
results

#putting the results well organised into a Pandas DataFrame
def inspect(results):
    lhs = [tuple(result[2][0][0])[0] for result in results]
    rhs = [tuple(result[2][0][1])[0] for result in results]
    supports = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))
resultsInDataFrame = pd.DataFrame(inspect(results), columns= ['left hand Side', 'Right hand side', 'support', 'confidencces', 'lifts'])

#Displaying the results 
resultsInDataFrame

resultsInDataFrame.nlargest(n = 10, columns = 'lifts')
