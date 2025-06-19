import matplotlib.pyplot as plt 

hours_study=[1,2,3,4,5,6,7,8]
exam_scores=[20,40,10,60,30,50,55,44]

plt.scatter(hours_study,exam_scores,color='red',marker='o',label='student Data')

plt.xlabel('hours studies')
plt.ylabel('exams score')
plt.title('relationship between study time and exam score')
plt.legend(fontsize='15')
plt.grid(True)
plt.show()
