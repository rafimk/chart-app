from flask import Flask, Response, request, jsonify
import matplotlib.pyplot as plt
import numpy as np
import io
import os  # Import the os module

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=api_port, debug=False,  threaded=False)
