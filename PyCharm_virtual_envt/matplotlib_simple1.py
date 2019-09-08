import matplotlib.pyplot as plt

data = {'Player': ['Wade','James','Kobe','Curry'],
        'First': [10,10,8,12],
        'Second':[12,8,13,8],
        'Third':[15,12,8,8],
        'Fourth':[18,20,15,8]}
fig1 = plt.figure('Stacked Bar')
ax1 = fig1.add_subplot(1,1,1)
bar_width = 0.5
bars = [i+1 for i in range(len(data['First']))]
ticks = [i + (bar_width/2)for i in bars]
ax1.bar(bars,
        data['First'],
        width = bar_width,
        label = 'First Quarter',
        color = '#AA5439'),
ax1.bar(bars,
        data['Second'],
        width = bar_width,
        bottom = data['First'],
        label = 'Second Quarter',
        color = '#FFD600')
ax1.bar(bars,
        data['Third'],
        width = bar_width,
        bottom = [i+j for i,j in zip(data['First'],data['Second'])],
        label = 'Third Quarter',
        color = '#FF9200')
ax1.bar(bars,
        data['Fourth'],
        width = bar_width,
        bottom = [i+j+k for i,j,k in zip(data['First'],data['Second'],data['Third'])],
        label ='Fourth Quarter',
        color ='r')
plt.xticks(ticks,data['Player'])
ax1.set_xlabel("Total")
ax1.set_ylabel("Player")
plt.legend(loc = 'upper right')
plt.xlim([min(ticks) - bar_width, max(ticks)+bar_width])
plt.show()


