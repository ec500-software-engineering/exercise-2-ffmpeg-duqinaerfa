import os
import subprocess
import queue
import threading

input_path = '/Users/duqinmei/Github/exercise-2-ffmpeg-duqinaerfa/input_video'
output_path = '/Users/duqinmei/Github/exercise-2-ffmpeg-duqinaerfa/output_video'


def convert(file):
    video_720 = "ffmpeg -i " + input_path + "/" + file + ' -r 30 -b 2M -s 1280x720 ' + output_path + "/" + file[:-4] + "720.mp4"
    video_480 = "ffmpeg -i " + input_path + "/" + file + ' -r 30 -b 1M -s 720x480 ' + output_path + "/" + file[:-4] + "480.mp4"
    subprocess.call(video_720, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
    print('Convert ' + file + ' to 720P' + ' complete!')
    subprocess.call(video_480, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
    print('Convert ' + file + ' to 480P' + ' complete!')


def main():
    q = queue.Queue()
    thread_list = []
    i = 0

    try:
        for file in os.listdir(input_path):
            if file.endswith('.mp4'):
                i = i + 1
                q.put(file)
                thread_list.append(threading.Thread(target=convert, args=(file, )))
    except Exception as e:
        print(e)

    print(str(i) + ' to convert')

    for thread in thread_list:
        thread.start()

if __name__ == '__main__':
    main()
