# Import all the necessary libraries in the code
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# Defining a custom-defined function cubes
def cubes(sides):
    # Creating data points for the sides
    data = np.ones(sides)
    # Creating the figure object
    fig = plt.figure(figsize=(9, 9))
    # Creating axes object to the plot
    ax = fig.add_subplot(111 , projection = '3d')
    # Plotting the figure
    ax.voxels(data, facecolors="yellow")
    # Displaying the figure
    plt.show()
# Creating the main () function
def main():
    # Defining side for the cube
    sides = np.array([ 2, 2, 2 ])
    # Calling the cubes () function
    cubes(sides)
# Calling the main () function
if __name__ == "__main__":
    main ()
