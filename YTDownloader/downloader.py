def download(link):
    try:
        import pytube
        url = link
        video = pytube.YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download()
        return 0
    except pytube.exceptions.VideoUnavailable:
        return 1
    except KeyError:
        return 2