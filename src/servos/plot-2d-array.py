import plotly.graph_objs as go
import numpy as np

# Create 2D data
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create 3D plot
fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])

# Set plot layout
fig.update_layout(title='3D Plot of Highs', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

# Show plot
fig.show()