import numpy as np
import matplotlib.pyplot as plt


horiz = np.array(range(100))/100.0
y1 = np.ones(100)
plt.plot(horiz , y1, 'b')
vert = np.array(range(100))/100.0
x1 = np.ones(100)
plt.plot(x1 , vert, 'b')

import random
inside = 0
count=1
numPoints=int(input("Enter the total number of points: "))
while (count<=numPoints):
  x = random.random()
  y = random.random()
  if ((x**2)+(y**2))<=1:
    inside+=1
    plt.plot(x , y , 'go')
  else:
    plt.plot(x , y , 'ro')
  count+=1
pi=(4*inside)/numPoints
print ("The value of pi is:")
print(pi)
plt.show()
