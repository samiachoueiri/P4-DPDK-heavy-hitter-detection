import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.colors import LinearSegmentedColormap, Normalize


s = [64, 128, 256, 512, 1024, 1500]
c1 = [1, 1, 1, 1, 1, 1]
t1 = [1.948,3.506,6.645,12.82166667,25.29266667,36.88833333]
c2 = [2, 2, 2, 2, 2, 2]
t2 = [3.873666667,6.963666667,13.238,25.361,50.354,73.012]
c3 = [3, 3, 3, 3, 3, 3]
t3 = [5.788666667,10.33,19.63566667,37.904,74.07866667,97.74133333]
c4 = [4, 4, 4, 4, 4, 4]
t4 = [7.727666667,13.853,26.03033333,50.21,95.40066667,97.66966667]
c5 = [5, 5, 5, 5, 5, 5]
t5 = [9.617,17.27666667,32.53266667,59.61366667,98.125,97.74466667]
c6 = [6, 6, 6, 6, 6, 6]
t6 = [11.522,20.61866667,38.67933333,75.168,98.12233333,97.532]
c7 = [7, 7, 7, 7, 7, 7]
t7 = [12.94033333,23.204,42.01066667,80.16233333,98.11966667,97.73666667]
c8 = [8, 8, 8, 8, 8, 8]
t8 = [12.97666667,20.54566667,35.92933333,71.89733333,98.13066667,97.72]

colors = ['#95253B', '#82AA45']
cmap = LinearSegmentedColormap.from_list('custom', colors, N=256)
norm = Normalize(vmin=0, vmax=100)

# Plotting
fig = plt.figure(figsize=(18, 10))
plt.rcParams.update({'font.size': 18})
plt.rcParams['grid.linestyle'] = "dashed"
ax = fig.add_subplot(111, projection='3d')

# ax.plot(c1, s, t1, label='1 core')
# ax.plot(c2, s, t2, label='2 cores')
# ax.plot(c3, s, t3, label='3 cores')
# ax.plot(c4, s, t4, label='4 cores')
# ax.plot(c5, s, t5, label='5 cores')
# ax.plot(c6, s, t6, label='6 cores')
# ax.plot(c7, s, t7, label='7 cores')
# ax.plot(c8, s, t8, label='8 cores')

points = np.array([c1,s,t1]).transpose().reshape(-1,1,3)
segs = np.concatenate([points[:-1],points[1:]],axis=1)
lc = Line3DCollection(segs, cmap=cmap, norm=norm)
lc.set_array(t1) # color the segments by our parameter
ax.plot(c1, s, t1, label='1 core')
ax.add_collection3d(lc)

points = np.array([c2,s,t2]).transpose().reshape(-1,1,3)
segs = np.concatenate([points[:-1],points[1:]],axis=1)
lc = Line3DCollection(segs, cmap=cmap, norm=norm)
lc.set_array(t2) # color the segments by our parameter
ax.plot(c2, s, t2, label='2 cores')
ax.add_collection3d(lc)

points = np.array([c3,s,t3]).transpose().reshape(-1,1,3)
segs = np.concatenate([points[:-1],points[1:]],axis=1)
lc = Line3DCollection(segs, cmap=cmap, norm=norm)
lc.set_array(t3) # color the segments by our parameter
ax.add_collection3d(lc)
ax.plot(c3, s, t3, label='3 cores')
ax.add_collection3d(lc)

points = np.array([c4,s,t4]).transpose().reshape(-1,1,3)
segs = np.concatenate([points[:-1],points[1:]],axis=1)
lc = Line3DCollection(segs, cmap=cmap, norm=norm)
lc.set_array(t4) # color the segments by our parameter
ax.add_collection3d(lc)
ax.plot(c4, s, t4, label='4 cores')
ax.add_collection3d(lc)

points = np.array([c5,s,t5]).transpose().reshape(-1,1,3)
segs = np.concatenate([points[:-1],points[1:]],axis=1)
lc = Line3DCollection(segs, cmap=cmap, norm=norm)
lc.set_array(t5) # color the segments by our parameter
ax.add_collection3d(lc)
ax.plot(c5, s, t5, label='5 cores')
ax.add_collection3d(lc)

points = np.array([c6,s,t6]).transpose().reshape(-1,1,3)
segs = np.concatenate([points[:-1],points[1:]],axis=1)
lc = Line3DCollection(segs, cmap=cmap, norm=norm)
lc.set_array(t6) # color the segments by our parameter
ax.add_collection3d(lc)
ax.plot(c6, s, t6, label='6 cores')
ax.add_collection3d(lc)

points = np.array([c7,s,t7]).transpose().reshape(-1,1,3)
segs = np.concatenate([points[:-1],points[1:]],axis=1)
lc = Line3DCollection(segs, cmap=cmap, norm=norm)
lc.set_array(t7) # color the segments by our parameter
ax.add_collection3d(lc)
ax.plot(c7, s, t7, label='7 cores')
ax.add_collection3d(lc)

points = np.array([c8,s,t8]).transpose().reshape(-1,1,3)
segs = np.concatenate([points[:-1],points[1:]],axis=1)
lc = Line3DCollection(segs, cmap=cmap, norm=norm)
lc.set_array(t8) # color the segments by our parameter
ax.add_collection3d(lc)
ax.plot(c8, s, t8, label='8 cores')
test = ax.add_collection3d(lc)

# Adding labels and title
ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])
ax.set_yticks([64, 128, 256, 512, 1024, 1500])
ax.set_zticks([20,40,60,80,100])
ax.set_xlabel('Number of Cores')
ax.set_ylabel('Packet Sizes (Bytes)')
ax.set_zlabel('Throughput (Gbps)')
ax.set_title('Throughput as a function of number of cores and packet size')

cbar = fig.colorbar(test, shrink=0.4, aspect=5)
cbar.set_label('Throughput (Gbps)')


plt.show()
