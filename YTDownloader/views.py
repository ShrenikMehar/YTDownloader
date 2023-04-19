from django.shortcuts import render
import pytube
from django.http import HttpResponse, HttpResponseRedirect
import os

def index(request):
    if(request.method=="POST"):
        video_url = request.POST.get("url")
        try:
            video = pytube.YouTube(video_url)
            stream = video.streams.get_highest_resolution()
            video_file = stream.download()
            with open(video_file, 'rb') as f:
                response = HttpResponse(f.read(), content_type='video/mp4')
                response['Content-Length'] = str(os.path.getsize(video_file))
                filename = video.title or 'video'
                response['Content-Disposition'] = f'attachment; filename="{filename}.mp4"'
                return response
        except pytube.exceptions.VideoUnavailable:
            return HttpResponse("Sorry, the requested video is unavailable.")
        except KeyError:
            return HttpResponse("Sorry, an error occurred while processing your request. Please try again later.")
    return render(request,"index.html")