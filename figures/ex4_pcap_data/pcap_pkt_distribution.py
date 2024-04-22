import csv
import matplotlib.pyplot as plt

# Initialize lists to store data
packet_sizes = []
jan_count = []
feb_count = []
mar_count = []
apr_count = []

# Read data from CSV file
with open('pcap_pkt_distribution.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        packet_sizes.append(int(row[0]))
        jan_count.append(float(row[1]))
        feb_count.append(float(row[2]))
        mar_count.append(float(row[3]))
        apr_count.append(float(row[4]))

# Plotting
plt.figure(figsize=(8, 5))
plt.rcParams.update({'font.size': 16})

# Plotting percentage of packet count
plt.plot(packet_sizes, jan_count, label='Dataset 1')
plt.plot(packet_sizes, feb_count, label='Dataset 2')
plt.plot(packet_sizes, mar_count, label='Dataset 3')
plt.plot(packet_sizes, apr_count, label='Dataset 4')

# Adding labels and title
plt.xlabel('Packet Size (Bytes)')
plt.ylabel('Cummulative Percentage')
#plt.title('Packet Size Distribution')
plt.legend()

# Display plot
plt.grid(True)
# plt.savefig("data.pdf")
# plt.savefig("data.png")
plt.show()

