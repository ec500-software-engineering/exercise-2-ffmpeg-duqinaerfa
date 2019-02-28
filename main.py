import os
import queue
import asyncio


input_path = '/Users/duqinmei/Github/exercise-2-ffmpeg-duqinaerfa/input_video'
output_path = '/Users/duqinmei/Github/exercise-2-ffmpeg-duqinaerfa/output_video'


async def convert(q):
    file = q.get()
    os.system("ffmpeg -i " + input_path + "/" + file + ' -r 30 -b 2M -s 1280x720 ' + output_path + "/" + file[:-4] + "720.mp4")
    os.system("ffmpeg -i " + input_path + "/" + file + ' -r 30 -b 1M -s 720x480 ' + output_path + "/" + file[:-4] + "480.mp4")
    print('Convert ' + file + ' to 720P' + ' complete!')
    print('Convert ' + file + ' to 480P' + ' complete!')
    return 'done!'


def main():
    q = queue.Queue()
    i = 0

    try:
        for file in os.listdir(input_path):
            if file.endswith('.mp4'):
                i = i + 1
                q.put(file)
        q.get()
    except Exception as e:
        print(e)

    coroutine = convert(q)

    tasks = [asyncio.ensure_future(coroutine)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
        print('Task: ', task.result())

if __name__ == '__main__':
    main()
