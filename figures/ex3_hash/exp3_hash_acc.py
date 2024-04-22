import matplotlib.pyplot as plt

accuracy = [63.2,86.4,95,98.1,99.3,99.7,99.9]
hash_functions = [2, 3, 4, 5, 6, 7, 8]

# Increase font size globally
fig = plt.figure(figsize=(14, 10))
plt.rcParams.update({'font.size': 24})

plt.plot(hash_functions, accuracy, marker='o')

# plt.title('Accuracy vs Number of Hash Functions')
plt.xlabel('Number of Hash Functions')
plt.ylabel('Accuracy (%)')
plt.grid(True, linestyle='--')  # dashed grid lines

plt.xticks(hash_functions)  # Ensure all hash function values are displayed on x-axis

# plt.savefig('exp3_hash_acc.pdf')
# plt.savefig('exp3_hash_acc2.png')
plt.show()

