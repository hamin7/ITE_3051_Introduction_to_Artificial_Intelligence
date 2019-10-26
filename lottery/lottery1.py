import pandas as pd

# read the data
df = pd.read_csv("data/lottery.csv")

# extract needed column
df1 = df[['1','2','3','4','5','6','bonus']]

# translate dataframe to list for convenience
df2 = df1.values.tolist()

# cnt_number is each number's apearance times
cnt_number = []
for i in range(0, 46):
    cnt_number.append(0)

# count the appearnce times
for i in range(0, len(df2)):
    for j in range(0, 7):
        cnt_index = df2[i][j]
        cnt_number[int(cnt_index)] += 1

# print the appearance times
for k in range(1, 46):
    print('%5d -> %3d times'%(k, cnt_number[k]))