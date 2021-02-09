import pandas as pd

df1 = pd.DataFrame({'ColA': [10, 20, 30],
                    'ColB': [100, 200, 300]})

df2 = pd.DataFrame({'ColA': [40, 20, 50],
                    'ColB': [400, 200, 500]})

print(pd.concat([df1, df2]).drop_duplicates().reset_index(drop=True))
