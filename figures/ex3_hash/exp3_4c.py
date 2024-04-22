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
    [10.613,18.21,33.16533333,74.19233333,96.104,98.82633333],  # Throughput for 2 hashes
    [8.351333333,15.013,28.257,54.881,97.941,98.88066667],  # Throughput for 3 hashes
    [7.631,13.86066667,26.225,50.76166667,91.59533333,98.82266667],   # Throughput for 4 hashes
    [6.653,11.956,22.60466667,43.952,85.25633333,98.78366667],   # Throughput for 5 hashes
    [6.483333333,11.60566667,21.72433333,29.37,82.87933333,98.37166667],   # Throughput for 6 hashes
    [5.275333333,9.489,17.81666667,30.81333333,67.922,96.966],   # Throughput for 7 hashes
    [5.337,9.588,18.067,26.47066667,68.33733333,98.34066667]   # Throughput for 8 hashes
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

# plt.savefig('exp_3_4c.pdf')
# plt.savefig('exp_3_4c.png')
plt.show()
