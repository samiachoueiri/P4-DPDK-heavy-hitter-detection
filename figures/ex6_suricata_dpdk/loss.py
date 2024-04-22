import matplotlib.pyplot as plt

# Increase font size globally
# fig = plt.figure(figsize=(14, 10))
fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(18, 8))  # 1 row, 2 columns
plt.rcParams.update({'font.size': 24})

s_rate64 = [1,5,10,25,25,25]
s_loss64 = [30.1921,86.2087,94.3573,97.2685,97.2793,97.2793]
s_rate128 = [1,5,10,25,50,50]
s_loss128 = [1.65543,66.682,83.4231,93.2943,96.5554,96.5513]
s_rate = [1,5,10,25,50,100]
s_loss256 = [1.47705,52.8597,75.7346,90.1052,95.056,96.6651]
s_loss512 = [1.33579,2.61612,42.2066,75.9396,87.3723,93.25]
s_loss1024 = [1.44696,1.52628,7.53437,62.5894,81.547,89.7688]
s_loss1500 = [1.91182,1.30614,0.966473,29.2422,62.7438,79.5037]

p_rate64 = [1,5,10,25,25,25]
p_rate128 = [1.8,9,18,38,40,40]
p_rate256 = [3.4,17,34,47,51,71]
p_rate512 = [0.35,1.7,3.5,8.7,17,35]
p_rate1024 = [0.7,3.5,7,17,35,70]
p_rate1500 = [1,5,10,25,50,90]

p_loss64 = [0.00610898428,0.03138541802,22.32378938,67.87949109,68.07459127,68.22771757]
p_loss128 = [0.3144016227,0.4287102495,22.98479993,64.62455104,69.72202008,69.72205077]
p_loss256 = [14.48275862,15.42246459,36.30693965,57.91753159,63.98211684,76.96481012]
p_loss512 = [0.0382848392,0.007704160247,0.004658118025,0.006125574273,0.004725009305,0.02253640496]
p_loss1024 = [0.03881987578,0.008379941771,0.01543448063,0.003487723214,0.04939369003,0.5768330861]
p_loss1500 = [0.001209365325,0.01843371624,0.002283653846,0.003007606333,0.01108482877,0.7963891338]


ax1.plot(s_rate64, s_loss64, marker='o', label='64 Bytes')
ax1.plot(s_rate128, s_loss128, marker='o', label='128 Bytes')
ax1.plot(s_rate, s_loss256, marker='o', label='256 Bytes')
ax1.plot(s_rate, s_loss512, marker='o', label='512 Bytes')
ax1.plot(s_rate, s_loss1024, marker='o', label='1024 Bytes')
ax1.plot(s_rate, s_loss1500, marker='o', label='1500 Bytes')

ax1.set_title('Suricata DPDK')
ax1.set_ylim(0, 100)
ax1.set_xlabel('Rate (Gbps)')
ax1.set_ylabel('Loss (%)')
ax1.grid(True, linestyle='--')
ax1.legend()

ax2.plot(p_rate64, p_loss64, marker='o', label='64 Bytes')
ax2.plot(p_rate128, p_loss128, marker='o', label='128 Bytes')
ax2.plot(p_rate256, p_loss256, marker='o', label='256 Bytes')
ax2.plot(p_rate512, p_loss512, marker='o', label='512 Bytes')
ax2.plot(p_rate1024, p_loss1024, marker='o', label='1024 Bytes')
ax2.plot(p_rate1500, p_loss1500, marker='o', label='1500 Bytes')

ax2.set_title('P4-DPDK')
ax2.set_ylim(0, 100)
ax2.set_xlabel('Rate (Gbps)')
ax2.set_ylabel('Loss (%)')
ax2.grid(True, linestyle='--')
ax2.legend()

# plt.xticks(s_rate)  # Ensure all hash function values are displayed on x-axis
# plt.savefig('exp3_hash_acc.pdf')
# plt.savefig('exp3_hash_acc2.png')

plt.show()

