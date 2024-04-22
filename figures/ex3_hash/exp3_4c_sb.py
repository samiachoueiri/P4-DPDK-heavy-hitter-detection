import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, Normalize

# Data
hashes = [2, 3, 4, 5, 6, 7, 8]
packet_sizes = [64, 128, 256, 512, 1024, 1500]

# throughput_data = [
#     [10.613,18.21,33.16533333,74.19233333,96.104,98.82633333],  # Throughput for 2 hashes
#     [8.351333333,15.013,28.257,54.881,97.941,98.88066667],  # Throughput for 3 hashes
#     [7.631,13.86066667,26.225,50.76166667,91.59533333,98.82266667],   # Throughput for 4 hashes
#     [6.653,11.956,22.60466667,43.952,85.25633333,98.78366667],   # Throughput for 5 hashes
#     [6.483333333,11.60566667,21.72433333,29.37,82.87933333,98.37166667],   # Throughput for 6 hashes
#     [5.275333333,9.489,17.81666667,30.81333333,67.922,96.966],   # Throughput for 7 hashes
#     [5.337,9.588,18.067,26.47066667,68.33733333,98.34066667]   # Throughput for 8 hashes
# ]
throughput_data = [
    [10,18,33,74,96,98],  # Throughput for 2 hashes
    [8,15,28,54,97,98],  # Throughput for 3 hashes
    [7,13,26,50,91,98],   # Throughput for 4 hashes
    [6,11,22,43,85,98],   # Throughput for 5 hashes
    [6,11,21,29,82,98],   # Throughput for 6 hashes
    [5,9,17,30,67,96],   # Throughput for 7 hashes
    [5,9,18,26,68,98]   # Throughput for 8 hashes
]
# Create a DataFrame for the heatmap and transpose it
data = np.array(throughput_data[::-1])
data = np.array(throughput_data)
df = pd.DataFrame(data.T, index=packet_sizes, columns=hashes)
df = df[::-1]

# Plot heatmap
fig = plt.figure(figsize=(14, 10))
plt.rcParams.update({'font.size': 24})
# colors = ['#95253B', '#82AA45']  # Define the colors for the colormap
colors = ['#8F493F', '#82AA45']  # Define the colors for the colormap
cmap = LinearSegmentedColormap.from_list('custom', colors, N=256)
ax = sns.heatmap(df, annot=True, cmap=cmap)
# plt.title('Throughput as a function of hash functions and packet size')
cbar = ax.collections[0].colorbar
cbar.set_label('Throughput (Gbps)', rotation=90, labelpad=20)
plt.xlabel('Number of Hash Functions')
plt.ylabel('Packet Sizes (Bytes)')
# plt.savefig('exp_3_4c_sb.pdf')
# plt.savefig('exp_3_4c_sb.png')
plt.show()
