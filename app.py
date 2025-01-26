from flask import Flask, render_template, request, jsonify
import os
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Directory where the uploaded files will be stored
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions (just mp3 for now)
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'flac', 'aac'}

# Check if the file has a valid extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to render the homepage with the playlist
@app.route('/')
def index():
    songs = []
    # Check if metadata.json exists, if not create it
    metadata_file = 'metadata.json'
    if os.path.exists(metadata_file):
        with open(metadata_file, 'r') as f:
            song_metadata = json.load(f)
            songs = song_metadata
    return render_template('index.html', songs=songs)

# Route to handle song upload
@app.route('/upload', methods=['POST'])
def upload_song():
    if 'song' not in request.files:
        return jsonify({"error": "No file part"}), 400

    song_file = request.files['song']
    title = request.form['title']
    artist = request.form['artist']

    if song_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if song_file and allowed_file(song_file.filename):
        filename = secure_filename(song_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        song_file.save(file_path)

        # Save the song metadata (title, artist, filename) in a JSON file
        song_data = {
            'title': title,
            'artist': artist,
            'file': filename
        }

        # Append the new song data to the existing metadata
        metadata_file = 'metadata.json'
        if os.path.exists(metadata_file):
            with open(metadata_file, 'r') as f:
                existing_data = json.load(f)
        else:
            existing_data = []

        existing_data.append(song_data)

        # Write back the updated metadata to the JSON file
        with open(metadata_file, 'w') as f:
            json.dump(existing_data, f)

        return jsonify(song_data)

    return jsonify({"error": "Invalid file format"}), 400

if __name__ == '__main__':
    # Create the upload folder if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    app.run(debug=True)
