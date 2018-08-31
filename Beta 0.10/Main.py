from pydub import AudioSegment as AS
import os

'''
This is a simple Software. U can use it to cut .mp3 or .wav

pydub https://github.com/jiaaro/pydub
FFmpeg http://www.ffmpeg.org/download.html
Github https://github.com/huxiao14/CutCat
Thanks:)HF
CutCat

'''
def cut_Mp3(where,begin,stop,db,name):
    Mp3 = AS.from_mp3(where)  
    Seconds = int(begin * 1000)
    Seconds2 = int(stop * 1000)
    Mp3 = Mp3[Seconds:Seconds2]
    Mp3.export(name+'.mp3',format='mp3',bitrate='192k',tags={'artist':'None','album':'None'}) 
    
    return

def cut_Wav(serf,where,begin,stop,db,name):
    pass
    return

def add_Mp3(serf,where1,where2,name):
    pass
    return

def add_Wav(serf,where1,where2,name):
    pass
    return

LeiXing = '0'
while LeiXing != '3':
    LeiXing = str(input('请选择要裁剪的文件类型 1.mp3 2.wav 3.退出'))
    if LeiXing == '3':
        pass
    if LeiXing != '1' and LeiXing != '2' and LeiXing != '3':   #这里写的怎么zz是因为else会出问题
        print ('请输入对应的数字...')
        os.system ('pause')

    
    LuJing = str(input('请输入文件的绝对路径...'))
    Begin = str(input('请输入想要裁剪文件的开始节点时间（以秒为单位）...'))
    Stop = str(input('请输入想要裁剪文件的结束节点时间...'))
    DB = str(input('是否需要放大或缩小音量，需要请输入放大或缩小的db数，缩小请用负数表示,不需要请输入0...'))
    Name = str(input('请输入新文件的名字'))
    if LeiXing == '1' or LeiXing == '2':
        os.system('cls')
        print ('正在操作...')
        if LeiXing == '1':
            cut_Mp3(LuJing,Begin,Stop,DB,Name)
        if LeiXing == '2':
            cit_Wav(LuJing,Begin,Stop,DB,Name)
        print ('操作完成,新文件已在CutCat的根目录下')
        os.system('pause')
    
    
