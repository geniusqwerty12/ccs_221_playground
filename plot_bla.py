import matplotlib.pyplot as plt

# Configure the PyPlot Window params
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

# Set the start and end points
point1 = [15, 18] # left most point
point2 = [30, 26]

# determine left most side point
# add as x0, y0
final_points = [] + [point1]

# Calculate the change in x and y
x_delta = point2[0] - point1[0]
y_delta = point2[1] - point1[1]

# solve for slope
m = y_delta / x_delta
print("slope is: ", m)
print(abs(m) < 1)
# calculate other constants
# usage will depend on the absolute value of slope
dy_2 = 2 * y_delta
dx_2 = 2 * x_delta

# if slope is less than 1
dy2_dx2 = dy_2 - dx_2 
# if slope is greater than 1
dx2_dy2 = dx_2 - dy_2

# get the initial value of p
p_value = 0

if abs(m) < 1:
    p_value = dy_2 - x_delta
else:
    p_value = dx_2 - y_delta

for i in range(x_delta):
    print("K at ", i)
    print("p with value of ", p_value)
    # calculate other values of points
    x_new = 0
    y_new = 0

    if p_value < 0:
        # update either x or y depending on the value
        # of slope
        # update value of p depending on the slope
        if abs(m) < 1:
            x_new = final_points[i][0] + 1
            y_new = final_points[i][1]
            # update value of p
            p_value = p_value + dy_2
        else:
            x_new = final_points[i][0]
            y_new = final_points[i][1] + 1
            p_value = p_value + dx_2
         
    else: 
        x_new = final_points[i][0] + 1
        y_new = final_points[i][1] + 1
            
        if abs(m) < 1:
            p_value = p_value + dy2_dx2
        else:
            p_value = p_value + dx2_dy2
    
    final_points += [[x_new, y_new]]

print(final_points)

# This separates the x and y values
# So that it can be plotted on the graph
x_values = []
y_values = []
for i in range(len(final_points)):
    x_values.append( final_points[i][0] )
    y_values.append( final_points[i][1] )

# Plot the values and 
# and setup of the PyPlot figure
plt.plot(x_values, y_values, 'bo')
plt.text(point1[0]-0.015, point1[1]+0.25, "Point1")
plt.text(point2[0]-0.050, point2[1]-0.25, "Point2")
# Adjust the max values of x and y
# plt.xticks(np.arange(0, 20))
# plt.yticks(np.arange(0, 20))
plt.grid()
plt.show()