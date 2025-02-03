import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/content/Ads_CTR_Optimisation.csv')

#implementing Upper Confidence Bound
import math
N = 10000  # Total number of rounds (you'll be selecting ads 10,000 times)
d = 10  # Number of ads (columns in your dataset)
ads_selected = []  # This will store which ads are selected in each round
number_of_selections = [0] * d  # Track how many times each ad has been selected (initially zero for all ads)
sum_of_rewards = [0] * d  # Track the total rewards for each ad
total_reward = 0  # Keep a running total of the rewards

for n in range(0, N):  # Looping over all rounds (up to 10,000)
    ad = 0  # Initially, set the selected ad to 0
    max_upper_bound = 0  # We will track the ad with the highest UCB value
    for i in range(0, d):  # Loop through each ad (column)
        if number_of_selections[i] > 0:  # If the ad has been selected at least once
            average_reward = sum_of_rewards[i] / number_of_selections[i]  # Calculate the average reward for this ad
            # Calculate the confidence interval (UCB)
            delta_i = math.sqrt(3 / 2 * math.log(n + 1) / number_of_selections[i])
            upper_bound = average_reward + delta_i  # Upper bound = average reward + confidence
        else:
            upper_bound = 1e400  # For ads not yet selected, set an arbitrarily large value to ensure it gets picked
        if upper_bound > max_upper_bound:  # If this ad has the highest UCB value, pick it
            max_upper_bound = upper_bound
            ad = i  # Set the selected ad to this one
    ads_selected.append(ad)  # Store which ad was selected in this round
    number_of_selections[ad] += 1  # Increment the number of times this ad was selected
    reward = df.values[n, ad]  # Get the reward for this ad in this round (from the dataset)
    sum_of_rewards[ad] += reward  # Add the reward to the total reward for this ad
    total_reward += reward  # Add the reward to the total reward across all ads

#visualising the results
plt.hist(ads_selected)
