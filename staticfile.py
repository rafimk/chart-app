from flask import Flask, send_from_directory
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log'),
    ]
)

app = Flask(__name__)

@app.route('/images/<filename>')
def serve_image(filename):
    # Define the path to your "static" directory where the images are stored.
    static_dir = 'charts'
    logging.info("Starting the application")

    # Use Flask's send_from_directory function to serve the image.
    # This function will look for the requested file in the "static" directory.
    return send_from_directory(static_dir, filename)

if __name__ == '__main__':
    app.run(debug=True)
