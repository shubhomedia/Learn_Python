import matplotlib.pyplot as plt

data = {'Player': ['Wade','James','Kobe','Curry'],
        'First': [10,10,8,12],
        'Second':[12,8,13,8],
        'Third':[15,12,8,8],
        'Fourth':[18,20,15,8]}
fig1 = plt.figure('Stacked Bar')
ax1 = fig1.add_subplot(1,1)
bar_width = 0.5
bars = [i+1 for i in range(len(data['First']))]
ticks = [i + (bar_width/2)for i in bars]
ax1.bar(bars,)