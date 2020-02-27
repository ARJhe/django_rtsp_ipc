from django.shortcuts import render
from . import tests as t


stream_path = "http://127.0.0.1:8000/static/live/stream1/mystream.m3u8"


def home(request):
    # get thumbnails here
    # t.announce()
    return render(request, 'streaming/index.html', {'stream_path': stream_path})
