import random
from typing import List
import pandas as pd

df = pd.read_csv("data/lottery.csv")

# function that make random number list.
def random_func(num):
    result = []
    for i in range(len(df)):
        result.append(random.randrange(0,num))
    return result

# 0:son scores no goal, 1: son scores 1 goal, 2: son scores 2 goals, 3: son scores hattrick, 4: son goes crazy.
random_SonHeunhmin = random_func(5)
# 0:pig dream, 1:cow dream, 2:dog dream.
random_dream = random_func(3)
# 0:no assignment weekend, 1:assignment weekend
random_no_assignment = random_func(2)

adding_df = pd.DataFrame(
    {"SonHeunhmin": random_SonHeunhmin, "dream": random_dream, "no_assignment": random_no_assignment}
)
df2 = df.join(adding_df)
df2.to_csv("./data/new_lottery.csv", mode="w")