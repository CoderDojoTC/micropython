#-----POLYNOMIAL FIT----
x = np.array([1.2,2.5,3.4,4.0,5.4,6.1,7.2,8.1,9.0,10.1,11.2,12.3,13.4,14.1,15.0]) # x coordinates
xplot_values = np.array([(.125, 3000), (.25, 11000), (.5, 17000), (.75, 24000), (.8125, 42000)])
x = xplot_values[:, 0]
y = xplot_values[:, 1]
fit = np.polyfit(x, y, 2)
a = fit[0]
b = fit[1]
c = fit[2]
fit_equation = a * np.square(x) + b * x + c
#Plotting
fig1 = plt.figure()
ax1 = fig1.subplots()
ax1.plot(x, fit_equation,color = 'r',alpha = 0.5, label = 'Polynomial fit')
ax1.scatter(x, y, s = 5, color = 'b', label = 'Data points')
ax1.set_title('Polynomial fit example')
ax1.legend()
plt.show()