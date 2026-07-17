import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')

# # a =  {'day': 1, 'month': 2, 'year': 2023, 'hour': 12, 'minute': 30}
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data, index=['joshua', 'williams', 'collins'])
# print(pd.options.display.max_rows)  # Accessing the first row using loc/

# new_df = df.dropna()

# new_df = df[(df['Pulse'] >= 120) & (df['Pulse'] <= 180)]

# print(new_df[['Duration', 'Pulse']].sum())


# # new_df = df["Duration"].mode()
# # df.plot()
# # plt.show()

# print(df.corr())
# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
df["Duration"].plot(kind = 'hist')

plt.show()
