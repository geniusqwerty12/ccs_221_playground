import matplotlib.pyplot as plt

# Configure the PyPlot Window params
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

# Set the start and end points
point1 = [15, 18]
point2 = [30, 26]

# List that will store all of the points
final_points = [] + [point1]

# Calculate the change in x and y
x_delta = point2[0] - point1[0]
y_delta = point2[1] - point1[1]

# Steps, this will determine the number of points to be created
steps = 20

# solve for slope
m = y_delta / x_delta
# print(m)

for i in range(steps):
    # calculate other values of points
    x_new = 0
    y_new = 0

    if abs(m) < 1:
        # Calculate the steps
        if m > 0 :
            x_new = final_points[i][0] + 1
            y_new = final_points[i][1] + m
        else :
            x_new = final_points[i][0] - 1
            y_new = final_points[i][1] - m

        final_points += [[x_new, y_new]]
    else:
        # Calculate the steps
        if m > 0 :
            x_new = final_points[i][0] + 1/m
            y_new = final_points[i][1] + 1
        else:
            x_new = final_points[i][0] - 1/m
            y_new = final_points[i][1] - 1

        final_points += [[x_new, y_new]]

    if x_new == point2[0] or y_new == point2[1]:
        print("End point reached, stopping the loop...")
        break

# Finally add the final point
final_points += [[point2[0], point2[1]]]

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