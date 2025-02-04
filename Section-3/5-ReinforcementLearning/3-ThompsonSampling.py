import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('/content/Ads_CTR_Optimisation.csv')

import random  # Importing the random module to generate random numbers

N = 10000  # Total number of rounds (how many times we show an ad)
d = 10  # Total number of ads (different choices/arms)

ads_selected = []  # List to store the index of the ad chosen in each round
numbers_of_rewards_1 = [0] * d  # List to store the count of times each ad got a reward (clicked)
numbers_of_rewards_0 = [0] * d  # List to store the count of times each ad did NOT get a reward (not clicked)
total_reward = 0  # Variable to keep track of the total reward earned

# Loop through each round (each user visit)
for n in range(0, N):
    ad = 0  # Variable to store the selected ad for this round
    max_random = 0  # Variable to store the highest random draw value

    # Iterate through all ads to find the one with the highest random Beta value
    for i in range(0, d):
        # Generate a random value from a Beta distribution using the past success/failure counts
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)

        # Select the ad with the highest sampled value
        if random_beta > max_random:
            max_random = random_beta
            ad = i  # Update the chosen ad index

    ads_selected.append(ad)  # Store the chosen ad for this round

    reward = dataset.values[n, ad]  # Get the reward (click/no-click) from the dataset

    # Update the success or failure count for the selected ad
    if reward == 1:
        numbers_of_rewards_1[ad] += 1  # Increase success count
    else:
        numbers_of_rewards_0[ad] += 1  # Increase failure count

    total_reward = total_reward + reward  # Update total reward


plt.hist(ads_selected)
