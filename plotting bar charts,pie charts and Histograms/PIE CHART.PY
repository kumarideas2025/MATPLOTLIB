import matplotlib.pyplot as plt 
#  plt,pie(values,labels=label_list,color=color_list,autopct='%1.1f%%') ......'%1.1 f%%'--> % format specifaction start...1.1f= 1digit before decimal 1 digit after decimal
# %% means output will show like 35.5%
region=['north','south','east','west']
revenue=[3000,2000,1500,1000]

plt.pie(revenue,labels=region,autopct='%1.1f%%',colors=['green','pink','coral','gold'])
plt.title('revenue contribution by region')
plt.show() 