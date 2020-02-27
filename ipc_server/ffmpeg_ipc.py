import os, subprocess

''' we should not call ffmpeg from app side,
    we should activate it from terminal side.
'''


# command run in the background, type this cmd in termianl
# "START /B python ffmpeg_ipc.py": exe and not show exe window
# "START /MIN python ffmpeg_ipc.py": exe and show window

# ffmpeg -i "rtsp://admin:123456@192.168.2.86:554/H264?ch=1&subtype=0"
# -y -an -vcodec copy -f hls -hls_time 10 -hls_list_size 10 -hls_flags delete_segments -start_number 1
# D:\django\djang_rtsp\ipc_server\streaming\static\live\stream1\mystream.m3u8

def exe():
    root = os.getcwd()
    target = root + '\streaming\static\live'
    stream1 = target + '\stream1'
    VID1 = "rtsp://admin:123456@192.168.2.86:554/H264?ch=1&subtype=0"
    VIDEO_OPTS = "-vcodec copy"
    OUTPUT_HLS = "-f hls -hls_time 10 -hls_list_size 10 -hls_flags delete_segments -start_number 1"
    OUTPUT_PATH = "D:\django\djang_rtsp\ipc_server\streaming\static\live\stream1\mystream.m3u8"
    if not os.path.isdir(stream1):
        try:
            os.mkdir(stream1)
        except Exception as e:
            print(e)
    print(stream1)
    cmd = f'ffmpeg -i "{VID1}" -y -an {VIDEO_OPTS} {OUTPUT_HLS} {stream1}\mystream.m3u8'
    print('\033[43m \033[0m ' + cmd)
    # check_call(cmd, stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)
    os.system(cmd)

exe()


def announce():
    # print out on console
    print('\033[42m \033[0m loading streaming.test.py.')


def open_player():
    vids = 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov'
    cmd = f'ffplay.exe -rtsp_transport tcp -loglevel debug "{vids}"'
    print(cmd)
    subprocess.check_output(cmd, shell=True)
