import matplotlib.pyplot as plt
import numpy as np

def draw_stylish_wheel_of_life(data, categories, title="Wheel of Life"):
    N = len(categories)
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = data
    width = np.pi / 4 * np.ones(N)

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw={'projection': 'polar'})
    bars = ax.bar(theta, radii, width=width, bottom=0.0, align='center', edgecolor='gray', linewidth=0.5)

    # A clearer color palette - can be customized
    colors = ["#FF9999", "#66B2FF", "#99FF99", "#FFCC99", "#FFD700", "#C71585", "#20B2AA", "#FF4500"]
    for bar, color in zip(bars, colors):
        bar.set_facecolor(color)
        bar.set_alpha(0.7)

    # Remove gridlines and outer circle (spine)
    ax.yaxis.grid(False)
    ax.xaxis.grid(False)
    ax.spines["polar"].set_visible(False)

    # Remove ytick labels and set xtick labels with padding and custom font properties
    ax.set_yticklabels([])
    ax.set_xticks(theta)
    ax.set_xticklabels(categories, fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': '#555555'})

       # Set title with custom font properties
    ax.set_title(title, va='bottom', fontdict={'fontsize': 14, 'fontweight': 'bold'})

    # Add padding to the image
    plt.tight_layout()

    # Save as a high-res image with a transparent background
    plt.savefig("stylish_wheel_of_life.png", dpi=300, bbox_inches='tight', transparent=True)
    plt.show()

data_points = [5, 7, 3, 8, 9, 4, 7, 6]
areas = ["Health", "Relationships", "Career", "Finance", "Learning", "Leisure", "Physical Environment", "Personal Growth"]

draw_stylish_wheel_of_life(data_points, areas)

