import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap, Normalize

# Number of cores and packet sizes
hashes = [2, 3, 4, 5, 6, 7, 8]
packet_sizes = [64, 128, 256, 512, 1024, 1500]

accuracies = [' - 63.2%', ' - 86.4%', ' - 95%', ' - 98.1%', ' - 99.3%', ' - 99.7%', ' - 99.9%']

# Throughput data for each experiment
throughput_data = [
    [5.758333333,10.379,19.54566667,34.66533333,74.12866667,97.91933333],  # Throughput for 2 hashes
    [4.168666667,7.510666667,14.095,27.29366667,53.90466667,78.17],  # Throughput for 3 hashes
    [3.889,6.973333333,13.10466667,25.43033333,50.113,72.05533333],   # Throughput for 4 hashes
    [3.334,6.011,11.345,21.737,43.25433333,62.47266667],   # Throughput for 5 hashes
    [3.242,5.843666667,10.94566667,21.434,42.04333333,60.86466667],   # Throughput for 6 hashes
    [2.655,4.785333333,9.043,17.56266667,34.434,49.99433333],   # Throughput for 7 hashes
    [2.660666667,4.804666667,9.069,17.61,34.607,50.28866667]   # Throughput for 8 hashes
]

# Create meshgrid for 3D plotting
X, Y = np.meshgrid(hashes, packet_sizes)

# Convert throughput data to numpy array
Z = np.array(throughput_data)

# Create a 3D plot
fig = plt.figure(figsize=(18, 10))
plt.rcParams.update({'font.size': 18})
plt.rcParams['grid.linestyle'] = "dashed"

ax = fig.add_subplot(111, projection='3d')

# Create a custom colormap from red to green with min=0 and max=100
colors = ['#95253B', '#82AA45']  # Define the colors for the colormap
cmap = LinearSegmentedColormap.from_list('custom', colors, N=256)
norm = Normalize(vmin=0, vmax=100)

# Plotting the surface
surf = ax.plot_surface(X, Y, Z.T, cmap=cmap, norm=norm)

# Adding labels and title
ax.set_xticks(hashes)
# ax.set_xticklabels([f'{hash_}{acc_}' for hash_, acc_ in zip(hashes, accuracies)])
ax.set_yticks(packet_sizes)
ax.set_zticks([20,40,60,80,100])
ax.set_xlabel('Number of Hash Functions')
ax.set_ylabel('Packet Sizes (Bytes)')
ax.set_zlabel('Throughput (Gbps)')
ax.set_title('Throughput as a function of hash functions and packet size')

# Adding color bar
cbar = fig.colorbar(surf, shrink=0.5, aspect=5)
cbar.set_label('Throughput (Gbps)')

# plt.savefig('exp_3_2c.pdf')
# plt.savefig('exp_3_2c.png')
plt.show()
