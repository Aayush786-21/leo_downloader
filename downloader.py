import yt_dlp as youtube_dl

def download_video(url, quality):
    ydl_opts = {
        'format': quality,  # Use the selected quality option
        'outtmpl': '%(title)s.%(ext)s',
    }

    # Mapping quality preferences to format codes if needed
    if quality == "best":
        ydl_opts['format'] = 'best'
    elif quality == "highest":
        ydl_opts['format'] = 'bestaudio/best'
    elif quality == "lowest":
        ydl_opts['format'] = 'worst'
    else:
        ydl_opts['format'] = f'bestvideo[height<={quality}]+bestaudio/best' if quality.isdigit() else 'best'

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"Downloaded: {url} in quality: {quality}")
