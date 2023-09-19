import http.server
import socketserver

# Define the port at which the server will listen.
PORT = 8080

# Define the subfolder containing your static files (images).
subfolder = "charts"

# Create a handler for serving static files.
handler = http.server.SimpleHTTPRequestHandler

# Set the current working directory to the root directory.
# This is important to ensure the server serves files from the correct folder.
handler.directory = "/"

# Create a socket server with the specified handler.
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving static files from the '{subfolder}' subfolder on port {PORT}...")
    try:
        # Start the server and keep it running until interrupted.
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
