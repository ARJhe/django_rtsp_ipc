from django.shortcuts import render

stream_path = "http://127.0.0.1:8000/static/live/stream/mystream.m3u8"


def home(request):
    return render(request, 'streaming/index.html', {'stream_path': stream_path})
