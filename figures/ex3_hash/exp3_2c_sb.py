import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, Normalize

# Data
hashes = [2, 3, 4, 5, 6, 7, 8]
packet_sizes = [64, 128, 256, 512, 1024, 1500]

# throughput_data = [
#     [5.758333333,10.379,19.54566667,34.66533333,74.12866667,97.91933333],  # Throughput for 2 hashes
#     [4.168666667,7.510666667,14.095,27.29366667,53.90466667,78.17],  # Throughput for 3 hashes
#     [3.889,6.973333333,13.10466667,25.43033333,50.113,72.05533333],   # Throughput for 4 hashes
#     [3.334,6.011,11.345,21.737,43.25433333,62.47266667],   # Throughput for 5 hashes
#     [3.242,5.843666667,10.94566667,21.434,42.04333333,60.86466667],   # Throughput for 6 hashes
#     [2.655,4.785333333,9.043,17.56266667,34.434,49.99433333],   # Throughput for 7 hashes
#     [2.660666667,4.804666667,9.069,17.61,34.607,50.28866667]   # Throughput for 8 hashes
# ]
throughput_data = [
    [5,10,19,34,74,97],  # Throughput for 2 hashes
    [4,7,14,27,53,78],  # Throughput for 3 hashes
    [3,6,13,25,50,72],   # Throughput for 4 hashes
    [3,6,11,21,43,62],   # Throughput for 5 hashes
    [3,5,10,21,42,60],   # Throughput for 6 hashes
    [2,4,9,17,34,49],   # Throughput for 7 hashes
    [2,4,9,17,34,50]   # Throughput for 8 hashes
]
# Create a DataFrame for the heatmap and transpose it
# data = np.array(throughput_data[::-1])
data = np.array(throughput_data)
df = pd.DataFrame(data.T, index=packet_sizes, columns=hashes)
df = df[::-1]

# Plot heatmap
fig = plt.figure(figsize=(14, 10))
plt.rcParams.update({'font.size': 24})
# colors = ['#95253B', '#82AA45']  # Define the colors for the colormap
colors = ['#8F493F', '#82AA45']  # Define the colors for the colormap
cmap = LinearSegmentedColormap.from_list('custom', colors, N=256)
# ax = sns.heatmap(df, annot=True, fmt=".2f", cmap=cmap)
ax = sns.heatmap(df, annot=True, cmap=cmap)
# plt.title('Throughput as a function of hash functions and packet size')
cbar = ax.collections[0].colorbar
cbar.set_label('Throughput (Gbps)', rotation=90, labelpad=20)
plt.xlabel('Number of Hash Functions')
plt.ylabel('Packet Sizes (Bytes)')
# plt.savefig('exp_3_2c_sb.pdf')
# plt.savefig('exp_3_2c_sb.png')
plt.show()
