
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0, 2 * np.pi, 100)
y = np.cos(x)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #正常显示负号
plt.title(r'$f(x)=cos(x)$') 
plt.plot(x, y)

plt.figure()
x1 = np.arange(0,20,1)
y1 = np.zeros_like(x1)
y1[10] = 1
y1[5] = -1
y1[0] = 1
y1[15] = -1
plt.stem(x1,y1)

plt.title(r'离散信号') 

plt.grid(True)
plt.show()