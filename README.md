# Grove Garden - Music Playlist Web App

**Grove Garden** is an interactive web application that allows users to upload, manage, and play their favorite songs. Users can create their personalized playlists by uploading audio files, complete with song titles and artist names. The application provides a simple and fun user interface with dynamic background effects, making music management enjoyable and visually appealing.

## Features

- **Song Upload**: Upload audio files (MP3, WAV, FLAC, AAC) along with song title and artist information.
- **Playlist Display**: Display uploaded songs in a clean and user-friendly playlist format.
- **Audio Playback**: Play, pause, or replay songs directly from the playlist.
- **Responsive Design**: The app works across various devices, ensuring a seamless experience on both desktop and mobile.
- **Animated Gradient Background**: A dynamic, animated gradient background to enhance the user interface.

## Technologies Used

- **Frontend**:
  - HTML, CSS (with animations)
  - JavaScript
- **Backend**:
  - Python (Flask)
- **File Handling**:
  - Werkzeug (for secure file upload and management)
- **Audio Formats**: MP3, WAV, FLAC, AAC

## Requirements

- Python 3.7.9
- Flask 2.2.5
- Werkzeug 2.2.3
- Flask-Bootstrap 3.3.7.1
- Pygame 2.5.0
- A web browser (for testing)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/onenishitrathod/grove-garden.git

2. **Navigate to the project folder:**

   ```bash
   cd grove-garden

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt

4. **Create a directory for uploads if it doesn't exist:**

   ```bash
   mkdir static/uploads

7. **Run the Flask app:**

   ```bash
   python app.py

8. **Open your web browser and go to:**

   ```bash
   http://127.0.0.1:5000

## Contributing

Feel free to fork this project, make improvements, and create pull requests. If you encounter any issues or have suggestions, please open an issue in the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
