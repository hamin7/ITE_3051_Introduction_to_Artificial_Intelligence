import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

# Read data, and extrack five columns.
df = pd.read_csv("data/new_lottery.csv")
selected_data = [df["1"], df["2"], df["6"], df["bonus"], df["SonHeunhmin"]]

# 1st KMeans; goals SonHeunhmin scored and first numbers cluster (K=3)
x, y = selected_data[4], selected_data[0]
X = list(zip(x, y))

# Calling sklearn KMeans, cluster where K=3
kmeans = KMeans(n_clusters=3).fit(X)
labels = kmeans.labels_

# Calling matplotlib, plot the graph
# x, y are goals SonHeunhmin scored, 1st lottery number for each.
# c is color. for clustered label
fig, ax = plt.subplots()
ax.scatter(x, y, c=labels.astype(np.float))
ax.grid(True)
ax.set_title("goals SonHeunhmin scored clusters and first number (K=3)")
ax.set_xlabel("goals SonHeunhmin scored")
ax.set_ylabel("first number")
plt.savefig("goals SonHeunhmin scored and first number.png", dpi=150)
plt.show()


# 2nd KMeans, bonus, second number and dream clusters (k=4)
x, y, z = selected_data[3], selected_data[1], selected_data[4]
X = list(zip(x, y, z))

# Calling sklearn KMeans, cluster where K=4
kmeans = KMeans(n_clusters=4).fit(X)
labels = kmeans.labels_

# x, y, z are bonus, sixth number and dreams for each.
# c is color. for clustered label
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.scatter(x, y, z, c=labels.astype(np.float))
ax.grid(True)
ax.set_title("bonus, second number and dream clusters (K=4)")
ax.set_xlabel("bonus")
ax.set_ylabel("second")
ax.set_zlabel("dream")
plt.savefig("bonus, second number and dream.png", dpi=150)
plt.show()