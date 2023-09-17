from pytube import YouTube


def download(video_url):
    youtube = YouTube(video_url)

    video = youtube.streams.get_highest_resolution()
    path = ('./videos')
    video.download(path)

    print(
        f' video: {youtube.title}\n size: {video.filesize_gb}GB\n file type: {video.subtype}\n downloaded at directory: {path}\n ')
