# coding=utf-8
import multiprocessing
import tulingRobot
import snowBoy
import time
import faceRecog
import status

def face_chat():
    # when face over, chat will over
    event = multiprocessing.Event()

    tuling_chat = multiprocessing.Process(target=tulingRobot.chat, args=(event,))
    tuling_chat.daemon = True
    tuling_chat.start()
    print('chat begin...')

    tuling_chat.join()
    print('chat over...')

    return


def watch_listen():
    # watching and listening
    while True:
        event = multiprocessing.Event()

        listen = multiprocessing.Process(target=snowBoy.listen, args=(event,))
        listen.daemon = True
        listen.start()
        print('listening...')

        watch = multiprocessing.Process(target=faceRecog.watch, args=(event,))
        watch.daemon = True
        watch.start()
        print('watching...')

        status.write0()

        event.wait()
        print('waited')
        if listen.is_alive():
            listen.terminate()
        if watch.is_alive():
            watch.terminate()
        print('terminated')
        time.sleep(1.24)
        face_chat()
        print('chat over here')
        time.sleep(1.24)

# face_chat()

