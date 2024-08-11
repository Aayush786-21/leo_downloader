# LeoDownLoader

LeoDownLoader is a Python-based YouTube video downloader application with a graphical user interface (GUI) built using PyQt5. The application allows users to download YouTube videos in their preferred quality using the `yt-dlp` library.

## Features

- **Download YouTube Videos**: Quickly download videos from YouTube.
- **Quality Selection**: Choose from various quality options for the video download.
- **User-Friendly Interface**: Simple and intuitive GUI for ease of use.

## Requirements

- Python 3.7 or later
- PyQt5
- yt-dlp

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Aayush786-21/leo_downloader.git
   cd leo_downloader

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Install yt-dlp

bash
Copy code
pip install yt-dlp
Usage
Run the Application

bash
Copy code
python main.py
Using the GUI

Enter YouTube Video URL: Input the URL of the video you want to download.
Select Quality: Choose the desired video quality from the dropdown list.
Start Download: Click the "Download" button to start the video download.
Quality Options
best: Highest quality available.
highest: Best audio quality and video quality.
lowest: Lowest quality available.
144p, 360p, 720p, 1080p: Specific resolutions (adjustments may be needed based on available formats).

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
PyQt5 Documentation
yt-dlp Documentation
