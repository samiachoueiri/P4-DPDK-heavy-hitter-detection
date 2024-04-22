import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap, Normalize

# Number of cores and packet sizes
cores = [1, 2, 3, 4, 5, 6, 7, 8]
packet_sizes = [64, 128, 256, 512, 1024, 1500]

# Throughput data for each experiment
throughput_data = [
    [1.948,3.506,6.645,12.82166667,25.29266667,36.88833333],  # Throughput for 1 core
    [3.873666667,6.963666667,13.238,25.361,50.354,73.012],  # Throughput for 2 cores
    [5.788666667,10.33,19.63566667,37.904,74.07866667,97.74133333],  # Throughput for 3 cores
    [7.727666667,13.853,26.03033333,50.21,95.40066667,97.66966667],   # Throughput for 4 cores
    [9.617,17.27666667,32.53266667,59.61366667,98.125,97.74466667],   # Throughput for 5 cores
    [11.522,20.61866667,38.67933333,75.168,98.12233333,97.532],   # Throughput for 6 cores
    [12.94033333,23.204,42.01066667,80.16233333,98.11966667,97.73666667],   # Throughput for 7 cores
    [12.97666667,20.54566667,35.92933333,71.89733333,98.13066667,97.72]   # Throughput for 8 cores
]

# Create meshgrid for 3D plotting
X, Y = np.meshgrid(cores, packet_sizes)

# Convert throughput data to numpy array
Z = np.array(throughput_data)

# Create a 3D plot
fig = plt.figure(figsize=(18, 10))
plt.rcParams.update({'font.size': 18})
plt.rcParams['grid.linestyle'] = "dashed"

ax = fig.add_subplot(111, projection='3d')

# Create a custom colormap from red to green with min=0 and max=100
# colors = ['red', 'green']  # Define the colors for the colormap
colors = ['#95253B', '#82AA45']  # Define the colors for the colormap
cmap = LinearSegmentedColormap.from_list('custom', colors, N=256)
norm = Normalize(vmin=0, vmax=100)

# Plotting the surface
surf = ax.plot_surface(X, Y, Z.T, cmap=cmap, norm=norm)

# Adding labels and title
ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])
ax.set_yticks([64, 128, 256, 512, 1024, 1500])
ax.set_zticks([20,40,60,80,100])
ax.set_xlabel('Number of Cores')
ax.set_ylabel('Packet Sizes (Bytes)')
ax.set_zlabel('Throughput (Gbps)')
ax.set_title('Throughput as a function of number of cores and packet size')

# Adding color bar
# fig.colorbar(surf, shrink=0.5, aspect=5)
cbar = fig.colorbar(surf, shrink=0.5, aspect=5)
cbar.set_label('Throughput (Gbps)')

# plt.savefig('exp_2_1to8.pdf')
# plt.savefig('exp_2_1to8.png')
plt.show()
