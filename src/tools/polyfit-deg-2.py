import numpy as np
import plotly.express as px

xplot_values = np.array([(.125, 3000), (.25, 11000), (.5, 17000), (.75, 24000), (.8125, 42000)])
x = xplot_values[:, 0]
y = xplot_values[:, 1]

fit = np.polyfit(x, y, 2)

a = fit[0]
b = fit[1]
c = fit[2]
x_fit = np.linspace(x.min(), x.max(), 100)
y_fit = a * np.square(x) + b * x + c

# Create a Plotly scatter plot of the data
fig = px.scatter(x=x, y=y)

# Add the fitted line to the plot
fig.add_scatter(x=x_fit, y=y_fit, mode='lines', name='Fit')

# Show the plot
fig.show()

#Plotting
# fig1 = plt.figure()
# ax1 = fig1.subplots()
# ax1.plot(x, fit_equation,color = 'r',alpha = 0.5, label = 'Polynomial fit')
# ax1.scatter(x, y, s = 5, color = 'b', label = 'Data points')
# ax1.set_title('Polynomial fit example')
# ax1.legend()
# plt.show()