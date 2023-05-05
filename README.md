# AI_Dog_Raspberry-pi


A robot dased on raspiberry pi who can see, listen, speak, chat, face recognition
  

## 它怎么工作？

1.程序运行后，首先进入睡眠模式，可以使用关键词唤醒它；  
2.唤醒后它会向你问好，然后就可以跟它聊天了（支持VAD，也就是没有固定录音时间）；  
3.当它有一定时间没有声音，它会再次进入睡眠模式（想停止只能强行关闭进程）。

## 背后的技术(python)
 
语音识别与语音合成：百度云语音（在线）  
关键词检测：snowboy  
语音端点检测（VAD）: webrtcvad + github上找的代码    

## 实现

### 硬件

基于微雪的WAVEGO-RPi+麦克风+音响

### 需要安装的python库


pyaudio, webrtc, baidu-aip等（实际运行如果还需要什么，可以根据`报错提示`和各种`搜索引擎`安装相应的包）

### 具体实现



### 文件解释
 

总体结构：  
1.together.py是主程序
2.其他py文件都是库，除了snowboydecoder.py（snowboy官方提供的），其他文件都像它们的名字一样好理解  
3.temp.wav是暂时存放的语音文件，每次都会换  

## 其他注意事项

代码里的密钥，密码什么的我都改了一下，可以到相应的官网申请，都是免费的。  

时间：2023年5月

