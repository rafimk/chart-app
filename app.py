import os
import io
import matplotlib.pyplot as plt
import numpy as np
import uuid  # Import the uuid module
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

# Directory to store generated chart images
CHARTS_DIR = 'charts'

# Ensure the charts directory exists
os.makedirs(CHARTS_DIR, exist_ok=True)

api_port = int(os.environ.get('API_PORT', 80))


@app.route('/chart', methods=['POST'])
def generate_chart():
    try:
        # Get data from the request JSON
        data = request.json

        # Ensure that the request contains 'labels', 'sizes', and 'colors' keys
        if 'data' not in data or 'categories' not in data or 'title' not in data:
            return jsonify({"error": "Invalid data format"}), 400

        data_points = data['data']
        areas = data['categories']
        title = data['title']

        N = len(areas)
        theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
        radii = data_points
        width = np.pi / 4 * np.ones(N)

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={
                               'projection': 'polar'})
        bars = ax.bar(theta, radii, width=width, bottom=0.0,
                      align='center', edgecolor='gray', linewidth=0.5)

        # A clearer color palette - can be customized
        colors = ["#FF9999", "#66B2FF", "#99FF99", "#FFCC99",
                  "#FFD700", "#C71585", "#20B2AA", "#FF4500"]
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
        ax.set_xticklabels(areas, fontdict={
                           'fontsize': 10, 'fontweight': 'bold', 'color': '#555555'})

        # Set title with custom font properties
        ax.set_title(title, va='bottom', fontdict={
                     'fontsize': 14, 'fontweight': 'bold'})

        # Add padding to the image
        plt.tight_layout()

        # Save the chart as bytes in memory
        img_data = io.BytesIO()
        plt.savefig(img_data, format='png')
        img_data.seek(0)
        plt.close()

        # Return the image binary data as a Flask response
        return Response(img_data.getvalue(), content_type='image/png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/ikigai', methods=['POST'])
def draw_ikigai():
    try:
        # Get data from the request JSON
        data = request.json

        # Ensure that the request contains 'labels', 'sizes', and 'colors' keys
        if 'labels' not in data or 'overlap' not in data or 'title' not in data:
            return jsonify({"error": "Invalid data format"}), 400

        labels = data['labels']
        overlap_labels = data['overlap']
        title = data['title']

        fig, ax = plt.subplots(figsize=(10, 10))

        # Define circle radius and centers for a diagonal orientation
        r = 1.25
        offset = 0.6  # Adjusted for central intersection
        centers = [(0, offset), (-offset, 0), (0, -offset), (offset, 0)]

        # Colors for the circles
        colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

        # Create circles
        circles = [plt.Circle(center, r, color=color, alpha=0.4)
                   for center, color in zip(centers, colors)]
        for circle in circles:
            ax.add_patch(circle)

        # Adjusted positions for each circle's label to the outer edge
        label_positions = [(0, offset + r - 0.1), (-offset - r + 0.1, 0),
                           (0, -offset - r + 0.1), (offset + r - 0.1, 0)]
        for position, label in zip(label_positions, labels):
            ax.text(position[0], position[1], label, ha='center',
                    va='center', fontsize=9, fontweight='bold')

        # Set text for the overlaps
        overlap_positions = [
            (-offset, offset), (-offset, -offset), (offset, -offset), (offset, offset)]
        for position, label in zip(overlap_positions, overlap_labels):
            ax.text(position[0], position[1], label, ha='center', va='center',
                    fontsize=9, fontweight='bold', backgroundcolor='white', zorder=5)

        # Highlight central IKIGAI text
        ax.text(0, 0, title, ha='center', va='center', fontsize=20,
                fontweight='bold', color='#555555', zorder=5, backgroundcolor='white')

        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.5, 2.5)
        ax.set_aspect('equal', 'box')
        ax.axis('off')

        # Add padding to the image
        plt.tight_layout()

        # Save the chart as bytes in memory
        img_data = io.BytesIO()
        plt.savefig(img_data, format='png')
        img_data.seek(0)
        plt.close()

        # Return the image binary data as a Flask response
        return Response(img_data.getvalue(), content_type='image/png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/chartb', methods=['POST'])
def generate_chartb():
    try:
        # Get data from the request JSON
        data = request.json

        # Ensure that the request contains 'labels', 'sizes', and 'colors' keys
        if 'data' not in data or 'categories' not in data or 'title' not in data:
            return jsonify({"error": "Invalid data format"}), 400

        data_points = data['data']
        areas = data['categories']
        title = data['title']

        N = len(areas)
        theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
        radii = data_points
        width = np.pi / 4 * np.ones(N)

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={
                               'projection': 'polar'})
        bars = ax.bar(theta, radii, width=width, bottom=0.0,
                      align='center', edgecolor='gray', linewidth=0.5)

        # A clearer color palette - can be customized
        colors = ["#FF9999", "#66B2FF", "#99FF99", "#FFCC99",
                  "#FFD700", "#C71585", "#20B2AA", "#FF4500"]
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
        ax.set_xticklabels(areas, fontdict={
                           'fontsize': 10, 'fontweight': 'bold', 'color': '#555555'})

        # Set title with custom font properties
        ax.set_title(title, va='bottom', fontdict={
                     'fontsize': 14, 'fontweight': 'bold'})

        # Add padding to the image
        plt.tight_layout()

        # Save the chart as bytes in memory
        img_data = io.BytesIO()
        plt.savefig(img_data, format='png')
        img_data.seek(0)
        plt.close()

       # Encode the image data as base64 and return it as a string
        base64_img = base64.b64encode(img_data.read()).decode('utf-8')

        # Return the base64-encoded image as a string in the response
        return base64_img
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/ikigaib', methods=['POST'])
def draw_ikigaib():
    try:
        # Get data from the request JSON
        data = request.json

        # Ensure that the request contains 'labels', 'sizes', and 'colors' keys
        if 'labels' not in data or 'overlap' not in data or 'title' not in data:
            return jsonify({"error": "Invalid data format"}), 400

        labels = data['labels']
        overlap_labels = data['overlap']
        title = data['title']

        fig, ax = plt.subplots(figsize=(10, 10))

        # Define circle radius and centers for a diagonal orientation
        r = 1.25
        offset = 0.6  # Adjusted for central intersection
        centers = [(0, offset), (-offset, 0), (0, -offset), (offset, 0)]

        # Colors for the circles
        colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

        # Create circles
        circles = [plt.Circle(center, r, color=color, alpha=0.4)
                   for center, color in zip(centers, colors)]
        for circle in circles:
            ax.add_patch(circle)

        # Adjusted positions for each circle's label to the outer edge
        label_positions = [(0, offset + r - 0.1), (-offset - r + 0.1, 0),
                           (0, -offset - r + 0.1), (offset + r - 0.1, 0)]
        for position, label in zip(label_positions, labels):
            ax.text(position[0], position[1], label, ha='center',
                    va='center', fontsize=9, fontweight='bold')

        # Set text for the overlaps
        overlap_positions = [
            (-offset, offset), (-offset, -offset), (offset, -offset), (offset, offset)]
        for position, label in zip(overlap_positions, overlap_labels):
            ax.text(position[0], position[1], label, ha='center', va='center',
                    fontsize=9, fontweight='bold', backgroundcolor='white', zorder=5)

        # Highlight central IKIGAI text
        ax.text(0, 0, title, ha='center', va='center', fontsize=20,
                fontweight='bold', color='#555555', zorder=5, backgroundcolor='white')

        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.5, 2.5)
        ax.set_aspect('equal', 'box')
        ax.axis('off')

        # Add padding to the image
        plt.tight_layout()

        # Save the chart as bytes in memory
        img_data = io.BytesIO()
        plt.savefig(img_data, format='png')
        img_data.seek(0)
        plt.close()

       # Encode the image data as base64 and return it as a string
        base64_img = base64.b64encode(img_data.read()).decode('utf-8')

        # Return the base64-encoded image as a string in the response
        return base64_img
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/charturl', methods=['POST'])
def generate_chart_url():
    try:
        # Get data from the request JSON
        data = request.json

        # Ensure that the request contains 'data', 'categories', and 'title' keys
        if 'data' not in data or 'categories' not in data or 'title' not in data:
            return jsonify({"error": "Invalid data format"}), 400

        data_points = data['data']
        areas = data['categories']
        title = data['title']

        N = len(areas)
        theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
        radii = data_points
        width = np.pi / 4 * np.ones(N)

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={
                               'projection': 'polar'})
        bars = ax.bar(theta, radii, width=width, bottom=0.0,
                      align='center', edgecolor='gray', linewidth=0.5)

        colors = ["#FF9999", "#66B2FF", "#99FF99", "#FFCC99",
                  "#FFD700", "#C71585", "#20B2AA", "#FF4500"]
        for bar, color in zip(bars, colors):
            bar.set_facecolor(color)
            bar.set_alpha(0.7)

        ax.yaxis.grid(False)
        ax.xaxis.grid(False)
        ax.spines["polar"].set_visible(False)
        ax.set_yticklabels([])
        ax.set_xticks(theta)
        ax.set_xticklabels(areas, fontdict={
                           'fontsize': 10, 'fontweight': 'bold', 'color': '#555555'})
        ax.set_title(title, va='bottom', fontdict={
                     'fontsize': 14, 'fontweight': 'bold'})

        plt.tight_layout()

        # Generate a random GUID for the image name
        chart_filename = f"{uuid.uuid4()}.png"
        chart_path = os.path.join(CHARTS_DIR, chart_filename)

        # Save the chart as a PNG image
        plt.savefig(chart_path, format='png')
        plt.close()

        # Construct the URL for the saved chart image
        chart_url = f"/{CHARTS_DIR}/{chart_filename}"

        # Return the URL in the response
        return jsonify({"chart_url": chart_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/ikigaiurl', methods=['POST'])
def draw_ikigai_url():
    try:
        # Get data from the request JSON
        data = request.json

        # Ensure that the request contains 'labels', 'sizes', and 'colors' keys
        if 'labels' not in data or 'overlap' not in data or 'title' not in data:
            return jsonify({"error": "Invalid data format"}), 400

        labels = data['labels']
        overlap_labels = data['overlap']
        title = data['title']

        fig, ax = plt.subplots(figsize=(10, 10))

        # Define circle radius and centers for a diagonal orientation
        r = 1.25
        offset = 0.6  # Adjusted for central intersection
        centers = [(0, offset), (-offset, 0), (0, -offset), (offset, 0)]

        # Colors for the circles
        colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

        # Create circles
        circles = [plt.Circle(center, r, color=color, alpha=0.4)
                   for center, color in zip(centers, colors)]
        for circle in circles:
            ax.add_patch(circle)

        # Adjusted positions for each circle's label to the outer edge
        label_positions = [(0, offset + r - 0.1), (-offset - r + 0.1, 0),
                           (0, -offset - r + 0.1), (offset + r - 0.1, 0)]
        for position, label in zip(label_positions, labels):
            ax.text(position[0], position[1], label, ha='center',
                    va='center', fontsize=9, fontweight='bold')

        # Set text for the overlaps
        overlap_positions = [
            (-offset, offset), (-offset, -offset), (offset, -offset), (offset, offset)]
        for position, label in zip(overlap_positions, overlap_labels):
            ax.text(position[0], position[1], label, ha='center', va='center',
                    fontsize=9, fontweight='bold', backgroundcolor='white', zorder=5)

        # Highlight central IKIGAI text
        ax.text(0, 0, title, ha='center', va='center', fontsize=20,
                fontweight='bold', color='#555555', zorder=5, backgroundcolor='white')

        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.5, 2.5)
        ax.set_aspect('equal', 'box')
        ax.axis('off')

        # Add padding to the image
        plt.tight_layout()

         # Generate a random GUID for the image name
        chart_filename = f"{uuid.uuid4()}.png"
        chart_path = os.path.join(CHARTS_DIR, chart_filename)

        # Save the chart as a PNG image
        plt.savefig(chart_path, format='png')
        plt.close()

        # Construct the URL for the saved chart image
        chart_url = f"/{CHARTS_DIR}/{chart_filename}"

        # Return the URL in the response
        return jsonify({"chart_url": chart_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=api_port, debug=False,  threaded=False)
