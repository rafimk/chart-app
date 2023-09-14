import matplotlib.pyplot as plt

def draw_ikigai():
    fig, ax = plt.subplots(figsize=(10, 10))

    # Define circle radius and centers for a diagonal orientation
    r = 1.25
    offset = 0.6  # Adjusted for central intersection
    centers = [(0, offset), (-offset, 0), (0, -offset), (offset, 0)]
    
    # Colors for the circles
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
    
    # Create circles
    circles = [plt.Circle(center, r, color=color, alpha=0.4) for center, color in zip(centers, colors)]
    for circle in circles:
        ax.add_patch(circle)

    # Adjusted positions for each circle's label to the outer edge
    label_positions = [(0, offset + r - 0.1), (-offset - r + 0.1, 0), (0, -offset - r + 0.1), (offset + r - 0.1, 0)]
    labels = ['Love', 'World Needs', 'Good At', 'Paid For']
    for position, label in zip(label_positions, labels):
        ax.text(position[0], position[1], label, ha='center', va='center', fontsize=9, fontweight='bold')

    # Set text for the overlaps
    overlap_labels = ['Passion', 'Mission', 'Profession', 'Vocation']
    overlap_positions = [(-offset, offset), (-offset, -offset), (offset, -offset), (offset, offset)]
    for position, label in zip(overlap_positions, overlap_labels):
        ax.text(position[0], position[1], label, ha='center', va='center', fontsize=9, fontweight='bold', backgroundcolor='white', zorder=5)

    # Highlight central IKIGAI text
    ax.text(0, 0, 'IKIGAI', ha='center', va='center', fontsize=20, fontweight='bold', color='#555555', zorder=5, backgroundcolor='white')

    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal', 'box')
    ax.axis('off')

    plt.savefig("ikigai_diagram_edge_labels.png", dpi=300, bbox_inches='tight', transparent=True)
    plt.show()

draw_ikigai()