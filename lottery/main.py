import pandas as pd

# Read csv file
df = pd.read_csv("data/lottery.csv")

columns = [df["1"], df["2"], df["3"], df["4"], df["5"], df["6"], df["bonus"]]

# Numbers is 1~
numbers = [i for i in range(1, 46)]
counts = [0] * 45

# Set result variable
for col in columns:
    for num in col:
        counts[num - 1] = counts[num - 1] + 1
lottery_count = zip(numbers, counts)

# Print lottery frequency result
sorted_lf = sorted(lottery_count, key=lambda lf: lf[0], reverse=False)
for idx, val in sorted_lf:
    print(str(idx)+"->"+str(val)+"times")
