import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['axes.unicode_minus'] = False  # Ensure minus signs are displayed correctly

def plot_cloud_model(Ex, En, He, n, ax, label='', marker='o', color='blue', s=20):
    """
    Plots a cloud model on the given axes.

    Parameters:
    - Ex: Expectation value
    - En: Entropy value
    - He: Hyper-entropy value
    - n: Number of points to generate
    - ax: Matplotlib axes object
    - label: Label for the scatter plot
    - marker: Marker style
    - color: Color of the markers
    - s: Size of the markers
    """
    # Generate En' values from normal distribution N(En, He^2)
    En_prime = np.random.normal(En, He, n)
    # Ensure En' are positive to avoid invalid standard deviations
    En_prime = np.abs(En_prime)
    # Generate X values from normal distribution N(Ex, En'^2)
    X = np.random.normal(Ex, En_prime)
    # Calculate Y values (membership degrees)
    Y = np.exp(-((X - Ex) ** 2) / (2 * (En_prime ** 2)))
    # Plot scatter plot with specified aesthetics
    ax.scatter(X, Y, s=s, alpha=0.6, marker=marker, label=label, color=color)

if __name__ == '__main__':
    # Create a figure and axes with specified size for better aesthetics
    fig, ax = plt.subplots(figsize=(10, 6))

    # Set axis labels
    ax.set_xlabel('Expectation', fontsize=14)
    ax.set_ylabel('Membership Degree', fontsize=14)

    # Define colors, markers, and labels for each evaluation grade
    colors = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F']
    markers = ['o', '^', 's', 'D', '*']
    labels = ['Low', 'Relatively Low', 'Medium', 'Relatively High', 'High']

    # Define parameters for each evaluation grade cloud model
    Ex_list = [0, 3.09, 5, 6.91, 10]
    En_list = [1.308, 0.809, 0.500, 0.809, 1.308]
    He_list = [0.130, 0.080, 0.050, 0.080, 0.130]

    # Plot each evaluation grade cloud model
    for i in range(len(Ex_list)):
        plot_cloud_model(Ex_list[i], En_list[i], He_list[i], 2000, ax,
                         label=labels[i], marker=markers[i], color=colors[i], s=20)

    # Define parameters for Grid_20775 and Grid_11466
    Ex_list_grids = [8.749, 1.732]
    En_list_grids = [0.830, 0.842]
    He_list_grids = [0.082, 0.084]
    labels_grids = ['Grid_20775', 'Grid_11466']
    # Choose colors that are distinctly different
    colors_grids = ['#8B4513', '#FFD700']  # SaddleBrown and Gold
    markers_grids = ['X', 'P']  # Distinct markers for the grids

    # Plot the cloud models for the grids with larger marker sizes
    for i in range(len(Ex_list_grids)):
        plot_cloud_model(Ex_list_grids[i], En_list_grids[i], He_list_grids[i], 2000, ax,
                         label=labels_grids[i], marker=markers_grids[i],
                         color=colors_grids[i], s=40)  # Increased marker size

    # Set legend, limits, grid, and tick parameters
    ax.legend(loc='lower left', fontsize=12)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1.05)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.tick_params(axis='both', which='major', labelsize=12)

    # Save the plot as a PNG file
    plt.savefig('cloud_model_visualization.png', dpi=300, bbox_inches='tight')

    # Display the plot
    plt.show()
