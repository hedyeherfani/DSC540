# Hedyeh Erfani
# Weeks 1 and 2
# DSC 540
# Create line 

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

# Header from table was removed beforehand
x, y = np.loadtxt('world-population (1).csv', unpack=True, delimiter=',')

plt.plot(x, y)

plt.title('World Population Over Time')
plt.ylabel('Population (In Billions)')
plt.xlabel('Year')
plt.xticks(np.arange(min(x), max(x)+5, 5.0))
plt.show()


