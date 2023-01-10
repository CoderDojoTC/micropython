import numpy as np

# Input data
xplot_values = np.array([(.125, 3000), (.25, 11000), (.5, 17000), (.75, 24000), (.8125, 42000)])
x = xplot_values[:, 0]
y = xplot_values[:, 1]

# Fit a linear regression model
model = np.polyfit(x, y, 2)

print(model)

# Get the slope and intercept of the line
slope, intercept, sq = model

# Print the equation of the line
print(f"y = {slope:.2f}x + {intercept:.2f}")
