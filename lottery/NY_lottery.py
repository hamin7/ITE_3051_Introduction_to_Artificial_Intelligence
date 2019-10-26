import pandas as pd

cnt_list = []
for i in range(0, 46):
    cnt_list.append(0)

with open('data/lottery.csv') as fp:
    buf = fp.readlines()

for i in range(1, len(buf)):
    temp_lotto = ''.join(buf[i])
    temp_lotto = temp_lotto.replace('\n', '')
    cur_lotto_list = list(temp_lotto.split(','))

    print(cur_lotto_list)
    #print(len(cur_lotto_list))
    for i in range(2, len(cur_lotto_list)):
        cnt_index = cur_lotto_list[i]
        cnt_list[int(cnt_index)] += 1

for k in range(1, 46):
    print('%5d : %3d'%(k, cnt_list[k]))