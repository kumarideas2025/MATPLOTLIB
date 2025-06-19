import matplotlib.pyplot as plt 
product=['A','B','C','D']
sales=[1000,2000,300,1200]

plt.bar(product,sales,color='hotpink',label='2025 sales')
plt.xlabel('product')
plt.ylabel('sales')

plt.title('product sale comparison')
plt.legend(fontsize='12')
plt.show()

# if we add plt.barh() then it wills show horizontali 