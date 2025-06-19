# we use it to show distribution of ****continuos*** data by dividing it into 2 ranges (bins) 
# plt.hist(data,bins=number_of_bins,color='color-name', edge-color='black')

import matplotlib.pyplot as plt 
scores=[45,66,77,88,12,44,50,70,79,90,48,34,56,78]
plt.hist(scores, bins=5,color='purple',edgecolor='black')
plt.xlabel('score range')
plt.ylabel('number of students')
plt.title('socre distribution of student')
plt.show()


# bins=5 it means frequency and 10-20....are categlory
