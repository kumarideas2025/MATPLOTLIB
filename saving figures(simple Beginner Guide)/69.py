# savefig('filename.extension',dpi=value,bbox_inches='tight')
# savefig() means name+format+plot png / graph.pdf 
# dpi value=image resolution counter..dots pe inches 
# dpi=300----will save image in high quality
# bbox-- crop and fitted plot

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,30,40,50]

plt.plot(x,y,color='blue',marker='o')
plt.title('simple line plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.savefig('line_plot.png',dpi=300,bbox_inches='tight')
plt.show()