# coding=utf-8
import time
import sys
sys.path.append('./ImagesRecognition')
import requests
import json
import BaiduSdk
import client
import common
import vadSound
import robot
import status
import time
import weather
import psutil

# def tuling(text='I said nothing'):
#     # tuling Robot
#     tuling_url = 'http://www.tuling123.com/openapi/api'
#     tuling_date = {
#         'key': '4527c40***********92cf020847be',
#         'info': text
#     }  # 当你申请了自己的图灵机器人后，请将key换为你自己的
#     r = requests.post(tuling_url, data=tuling_date)
#     # print(r.text)
#     return json.loads(r.text)['text']


def chat(event):
    # chat with tuling Robot
    no_time = 0
    people = None
    robot.handShake()
    if BaiduSdk.text2sound('你好，我是钢蛋儿，很高兴为你服务。'):
        vadSound.play_sound()
        status.write1()
        
    print('机器人：你好。')

    while True:
        if event.is_set() and no_time >= 4:
            break
        if vadSound.record_sound():
            print('语音识别中。。。')
            ret, content = BaiduSdk.sound2text()
            # people = client.classify_people_image()['face_recognition_label_result']
            print('you say:'+str(content))
        elif event.is_set():
            break
        else:
            continue

        if not content:
            no_time += 1
            continue
        if ret:
            if content == '休息一下':
                print('你说：' + content)
                if BaiduSdk.text2sound('我坐下了'):
                    print('机器人：我坐下了')
                    vadSound.play_sound()
                    robot.rest()
            elif content == '人脸识别启动':
                print('你说：' + content)
                people = "或者".join([ common.getChineseName(i)  for i in client.classify_people_image()])
                if BaiduSdk.text2sound(f'你好，人脸识别后，我判断你是{people}'):
                    print(f'你好，你是{people}')
                    vadSound.play_sound()
            elif content == '图书识别启动':
                print('你说：' + content)
                book = "或者".join([ common.getChineseName(i) for i in client.classify_book_image()])
                if BaiduSdk.text2sound(f'你好，图书识别后，我判断这本书可能是{book}'):
                    print(f'你好，这本书可能是{book}')
                    vadSound.play_sound()
            elif content == '向前走两步':
                print('你说：' + content)
                if BaiduSdk.text2sound('好嘞，钢蛋儿要向前走了'):
                    print('机器人：向前走两步')
                    vadSound.play_sound()
                    robot.forward()
                    time.sleep(2)
                    robot.stopFB()
            elif content == '向后走两步':
                print('你说：' + content)
                robot.backward()
                time.sleep(2)
                robot.stopFB()
                if BaiduSdk.text2sound('好嘞，钢蛋儿要向后走了'):
                    print('机器人：向后走两步')
                    vadSound.play_sound()
            elif content == '跳一下':
                print('你说：' + content)
                if BaiduSdk.text2sound('好嘞，但我跳的不高哦'):
                    print('机器人：我跳了一下')
                    vadSound.play_sound()
                    robot.jump()
            elif content == '握个手':
                print('你说：' + content)
                if BaiduSdk.text2sound('好嘞，来握手啊'):
                    print('机器人：来握手啊')
                    vadSound.play_sound()
                    robot.handShake()
            elif content == '握左手':
                print('你说：' + content)
                if BaiduSdk.text2sound('好嘞，来握左手啊'):
                    print('机器人：来握左手啊')
                    vadSound.play_sound()
                    robot.leftHandShake()
            elif content == '狗狗撒尿':
                print('你说：' + content)
                if BaiduSdk.text2sound('怪不好意思的'):
                    print('机器人：撒尿了')
                    vadSound.play_sound()
                    robot.pee()
            elif content == '介绍一下自己':
                print('你说：' + content)
                robot.lightCtrl(1)
                robot.lightCtrl(2)
                robot.lightCtrl(3)
                robot.lightCtrl(4)
                if BaiduSdk.text2sound('你好，我是钢蛋儿，我会做很多动作，识别主人，也很听话哦。目前是钢蛋儿1.0，未来功能会更加丰富的.'):
                    print('机器人：我会走路握手爬下等动作')
                    vadSound.play_sound()
            elif content == '现在几点':
                time_tup = time.localtime(time.time())
                print('你说：' + content)
                if BaiduSdk.text2sound('你好，当前时间为{}年{}月{}日{}点{}分{}秒'.format(time_tup[0],time_tup[1],time_tup[2],time_tup[3],time_tup[4],time_tup[5])):
                    print(f'机器人：报时间')
                    vadSound.play_sound()
            elif content == '太酷啦':
                print('你说：' + content)
                if BaiduSdk.text2sound('泰裤啦，泰裤啦，钢蛋儿，泰裤啦'):
                    print(f'机器人：泰裤啦')
                    vadSound.play_sound()
            elif content == '太酷了':
                print('你说：' + content)
                if BaiduSdk.text2sound('泰裤啦，泰裤啦，钢蛋儿，泰裤啦'):
                    print(f'机器人：泰裤啦')
                    vadSound.play_sound()
            elif content == '喊个口号':
                print('你说：' + content)
                if BaiduSdk.text2sound('G F T 最棒'):
                    print(f'机器人：口号')
                    vadSound.play_sound()
            elif content == '讲个笑话':
                print('你说：' + content)
                if BaiduSdk.text2sound('从前有座山，山里有座庙，庙里有个老和尚，和一个小和尚，有一天老和尚对小和尚，讲着一个故事，故事的内容是: 从前有座山，山里有座庙'):
                    print(f'机器人：笑话')
                    vadSound.play_sound()
            elif content == '你的主人是谁':
                print('你说：' + content)
                if BaiduSdk.text2sound('大家都是我的主人，嘿嘿。快来给我下指令吧'):
                    print(f'机器人：主人')
                    vadSound.play_sound()
            elif content == '你现在认识谁':
                print('你说：' + content)
                if BaiduSdk.text2sound('我现在认识陆老板，李涛，于一飞，贾博淳。快联系我的开发，将你加入我的朋友圈！'):
                    print(f'机器人：认识')
                    vadSound.play_sound()
            elif content == '今天天气怎么样':
                print('你说：' + content)
                today=weather.getWeatherInfoToday()
                if BaiduSdk.text2sound(f'你好，{today}'):
                    print(f'机器人：今天天气')
                    vadSound.play_sound()
            elif content == '明天天气怎么样':
                tmr=weather.getWeatherInfoTomorrow()
                print('你说：' + content)
                if BaiduSdk.text2sound(f'你好，{tmr}'):
                    print(f'机器人：明天天气')
                    vadSound.play_sound()
            elif content == '处理器占用情况':
                print('你说：' + content)
                cpu=psutil.cpu_percent()
                print(cpu)
                if BaiduSdk.text2sound(f'你好，处理器使用率：{cpu}%'):
                    print(f'机器人：明天天气')
                    vadSound.play_sound()
            elif content == '内存占用情况':
                print('你说：' + content)
                mem=psutil.virtual_memory().percent
                print(mem)
                if BaiduSdk.text2sound(f'你好，内存使用率：{mem}%'):
                    print(f'机器人：明天天气')
                    vadSound.play_sound()
            elif content == '太空步':
                print('你说：' + content)
                if BaiduSdk.text2sound('我还没完全学会，可以先给你来一段'):
                    print('机器人：太空步')
                    vadSound.play_sound()
                    robot.spaceSteps()
            elif content == '下犬式':
                print('你说：' + content)
                if BaiduSdk.text2sound('好嘞'):
                    print('机器人：下犬式')
                    vadSound.play_sound()
                    robot.DDogPose()
            elif content == '上犬式':
                print('你说：' + content)
                if BaiduSdk.text2sound('好嘞'):
                    print('机器人：上犬式')
                    vadSound.play_sound()
                    robot.UDogPose()
            elif content == '跳个舞':
                print('你说：' + content)
                if BaiduSdk.text2sound('狗 界 舞王就是我'):
                    print('机器人：跳舞')
                    vadSound.play_sound()
                    robot.dance()
                    time.sleep(3)
                    if BaiduSdk.text2sound('谢谢'):  
                        vadSound.play_sound()
                        robot.thankYou()              
            else:
                if BaiduSdk.text2sound('不好意思，我现在还听不懂这个指令哦'):
                    vadSound.play_sound()
                print('机器人：我现在听不懂哦。')
            no_time = 0
        else:
            BaiduSdk.text2sound('语音识别出错')
            vadSound.play_sound()
            print('机器人：语音识别出错[{}]'.format(content))
            no_time += 1
            continue

        if event.is_set() and content == '再见':
            if BaiduSdk.text2sound('再见，要再找我玩哦'):
                vadSound.play_sound()
            print('机器人：再见。')
            break

        # tuling_text = tuling(content)
        # print('机器人：{}'.format(tuling_text))

        # if BaiduSdk.text2sound(tuling_text):
        #     vadSound.play_sound()
        # else:
        #     vadSound.play_sound('resources/fail_TTS.wav')
        #     print('语音合成出错。。。')

    return


#the followings are used to debug
# chat()
#result = tuling('hello')
#print(result)

