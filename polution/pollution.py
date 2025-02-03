import pandas as pd
import matplotlib.pylab as plt

csv_filename = "polution/values.csv"

df = pd.read_csv(csv_filename)

sixthRow = df.iloc[:,5]

plt.plot(sixthRow)

plt.xlabel("Data No")
plt.ylabel("Air Quality Index (AQI)")
plt.title("Air Pollution AQI Over Time")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

plt.show()
