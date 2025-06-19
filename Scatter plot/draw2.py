import matplotlib.pyplot as plt 

# [1,2,3] all are fpr hours of study and 2nd of both columns are numbers of students

plt.scatter( [1,2,3],[40,45,50],color='red',marker='o',label='class A')
plt.scatter( [1,2,3],[50,55,60],color='blue',marker='s',label='class B')


plt.xlabel('hours studies')
plt.ylabel('exams score')
plt.title('relationship between study time and exam score')
plt.legend(fontsize='15')
plt.grid(True)
plt.show()
