from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import base64

# Define Flask and CORS
app = Flask(__name__)
CORS(app)

# Define images directory
IMAGES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'images'))

# Define videos directory
VIDEOS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'videos'))


# Endpoint to receive requisitions
@app.route('/api/post/video', methods=['POST'])
def save_videos():
    # Obtain data from frontend
    videos = request.files.getlist('video')  # Receive a list of files
    argument1 = request.form['time']
    argument2 = request.form['rate']
    argument3 = request.form['hierarchical_method']
    argument4 = request.form['cut']

    # Save every file in videos folder
    for video_data in videos:
        video_path = os.path.join(VIDEOS_DIR, video_data.filename)
        video_data.save(video_path)

    # Further processing required...

    # Return a successful message
    return jsonify({'message': 'Vídeo salvo com sucesso!'})


# Endpoint to reply with images
@app.route('/api/get/images', methods=['GET'])
def reply_with_images():
    img = []
    for filename in os.listdir(IMAGES_DIR):
        img.append(f"http://localhost:5000/images/{filename}")
    return jsonify(img), 200


# Serve images
@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory(IMAGES_DIR, filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
