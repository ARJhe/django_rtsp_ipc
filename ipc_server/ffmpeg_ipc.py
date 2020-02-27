import os, subprocess
import parameter as p
''' we should not call ffmpeg from app side,
    we should activate it from terminal side.
    parameters hide on parameter.py
'''


# command run in the background, type this cmd in termianl
# "START /B python ffmpeg_ipc.py": exe and not show exe window
# "START /MIN python ffmpeg_ipc.py": exe and show window

# ffmpeg -i "ipc_addr"
# -y -an -vcodec copy -f hls -hls_time 10 -hls_list_size 10 -hls_flags delete_segments -start_number 1
# output_path

def exe():
    ipc_addr = p.ipc_addr
    root = os.getcwd()
    target = root + p.target_dir
    stream1 = target + '\stream1'
    VIDEO_OPTS = "-vcodec copy"
    HLS_SETTING = "-f hls -hls_time 10 -hls_list_size 10 -hls_flags delete_segments -start_number 1"
    if not os.path.isdir(stream1):
        try:
            os.mkdir(stream1)
        except Exception as e:
            print(e)
    print(stream1)
    cmd = f'ffmpeg -i "{ipc_addr}" -y -an {VIDEO_OPTS} {HLS_SETTING} {stream1}\mystream.m3u8'
    print('\033[43m \033[36m Execute ffmpeg cmd: \033[0m' + cmd)
    # check_call(cmd, stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)
    os.system(cmd)

exe()


def announce():
    # print out on console
    print('\033[42m \033[0m loading streaming.test.py.')

# announce()

def test_ffmpeg():
    vids = 'rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov'
    cmd = f'ffplay.exe -rtsp_transport tcp -loglevel debug "{vids}"'
    print(cmd)
    subprocess.check_output(cmd, shell=True)
