import numpy as np
import plotly.express as px

# Input data
xplot_values = np.array([(0,0), (.125, 3000), (.25, 11000), (.5, 17000), (.75, 24000), (.8625, 42000), (1.0, 65536)])
x = xplot_values[:, 0]
y = xplot_values[:, 1]

# Fit a linear regression model
model = np.polynomial(x, y, 2)

print(model)

# Generate a list of x values for the fitted line
x_fit = np.linspace(x.min(), x.max(), 100)
y_fit = 
# Calculate the y values for the fitted line
#y_fit = slope * x_fit + intercept

# Create a Plotly scatter plot of the data
#fig = px.scatter(x=x, y=y)

# Add the fitted line to the plot
#fig.add_scatter(x=x_fit, y=y_fit, mode='lines', name='Fit')

# Show the plot
#fig.show()
