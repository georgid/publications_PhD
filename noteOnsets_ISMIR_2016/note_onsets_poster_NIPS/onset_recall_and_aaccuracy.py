# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size': 22})

cF = [5,	4.5,	4.0,	3.5,	3.0]

fig, ax1 = plt.subplots()

plt.plot(cF, [57.2,	59.7,	66.8,	72.3,	73.2], 'ro-') # acapella onset recal
# plt.plot(cF, [52.8,	58.2,	65.9,	66.2,	68.4,], 'rs-') # poly onset recall


ax1.axis([2.8, 5.2, 50, 85])
plt.xlabel('cF of Gaussian filter')
ax1.set_ylabel('onset recall', color='r')

ax2 = ax1.twinx()
ax2.axis([2.8, 5.2, 50, 85])
ax2.set_ylabel('alignment accuracy', color='b')
ax2.plot(cF, [76.1,	78.7,	79.5,	81.7,	77.0], 'bx-') # a cappella  aa
# ax2.plot(cF, [61.2,	63.3,	64.8,	64.6,	60.3], 'bx-') # poly  aa

plt.show()
# <codecell>


