from sklearn.ensemble import IsolationForest
import numpy as np

data = np.array([
    [10],
    [12],
    [11],
    [13],
    [100]
])

model = IsolationForest(contamination=0.2)
model.fit(data)

predictions = model.predict(data)

print("Results:")
for value, result in zip(data, predictions):
    if result == -1:
        print(f"{value[0]} -> Anomaly")
    else:
        print(f"{value[0]} -> Normal")
