import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Q1: Create two charts using list and dataframe:
plt.plot([1,5,9,4]);
plt.plot(pd.DataFrame([1,4,5,7]));
plt.legend(["List","DataFrame"])

plt.show()
#Q2: Create pie chart with equal explode values.
plt.pie(np.arange(1,5), labels=['Jan','Feb','Mar', 'Apr'], explode = [.1,.1,.1,.1]);
plt.show()
#Q3: Create a scatter chart with circle marker, alpha = 0.4, and size = 50.
x = np.random.randn(150)
y = np.random.randn(150)
plt.scatter(x,y,marker="o",alpha=0.4,s=50)
#Q4: Add the following to your chart:
plt.title("bader",loc="left",c="red")
plt.show()
#Q5: Create three line charts with Legends at left and colors:
plt.plot([1,5,9,4],c ='b')
plt.plot(pd.DataFrame([1,4,5,7]), c ='r')
plt.plot([3,2,4,10],c ='g')
plt.legend(["line1","line2","line3"],loc='upper left')
plt.show()
#Q6: Create subplots with three charts and figsize=20,10:
plt.figure(figsize=[20,10])
plt.subplot(2,3,1)
x = np.random.randn(150)
y = np.random.randn(150)
plt.scatter(x,y,marker="o",alpha=0.4,s=50,c='r')
plt.subplot(2,3,2)
plt.pie(np.arange(1,5), labels=['Jan','Feb','Mar', 'Apr'], explode = [.1,.1,.1,.1])
plt.subplot(2,3,3)
plt.plot([1,5,9,4])
plt.plot(pd.DataFrame([1,4,5,7]))
plt.legend(["List","DataFrame"])
plt.show()