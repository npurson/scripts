import os
import pandas as pd
from collections import defaultdict


dict = defaultdict(int)
df = pd.read_excel('./1301.xls', usecols=[3])
df.tail


for _, row in df.iterrows():
    dict[row['卡口/区间']] += 1
print(dict)