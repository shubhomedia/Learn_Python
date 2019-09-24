import matplotlib.pyplot as plt

fig = plt.figure("Histogram")
ax = fig.add_subplot(1,1,1)
ax.hist([21,12,23,35,45,60,33,22,56,34,28,40,41],bins=7,facecolor ='g',density=False)

plt.title("Distribution")
plt.xlabel("Range")
plt.ylabel("Amount")
plt.show()

#Box Plot
fig2 = plt.figure("Box-Plot")
ax1 = fig2.add_subplot(1,1,1)
ax1.boxplot([21,12,23,35,45,60,33,22,56,34,28,40,41])
plt.show()

#Bar Plot
fig3 = plt.figure("Bar Plot")
ax2 = fig3.add_subplot(1,1,1)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title("Bars")
ax2.bar([0,1,2,3],[5,10,15,5],[0.5,1,1.3,1],color=['b','r'])
plt.show()

#Line Plot
fig4 = plt.figure("Line")
ax3 = fig4.add_subplot(1,1,1)
ax3.set_xlim([-2,10])
ax3.set_ylim([-2,10])
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_title("Lines")
ax3.plot([-1,2,4,7,8],[5,2,3,4,3],['r'])
plt.show()