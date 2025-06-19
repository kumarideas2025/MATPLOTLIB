# plt.plot(x,y,color='color name', linestyle='line_style',linewidth==1/2/3,marker='marker symbol',label='label name') use google to know more about marker symbol

import matplotlib.pyplot as plt
months=[1,2,3,4]
sales=[100,200,300,340]
plt.plot(months,sales,color='green',linestyle='--',linewidth=2,marker='o',label='2025 sales data')
plt.xlabel('months ')
plt.ylabel('sales')
plt.title('monthly sales data report')


# add a box legend............(upper left / lower right)....we can use legend after label .
plt.legend(loc='upper left',fontsize='12')
plt.grid(color='gray',linestyle=':',linewidth=1)


# plt.lim(star,end)
plt.xlim(1,4)
plt.ylim(0,340)


# plt.xticks will add new default list data in place of 1.5,1,2,2.5
plt.xticks([1,2,3,4],['M1','M2','M3','M4'])

plt.show() 