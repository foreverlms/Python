# -*- coding:utf-8 -*-
# import pickle
# d=dict(name='Bob',age=22,major='Mech')
# with open(r'C:\Users\Bobliao\PycharmProjects\Learning\text_pickle.txt','wb') as f :
#     f.write(pickle.dumps(d))
# f=open(r'.\text_pickle.txt','rb')
# c=f.read()
# e=pickle.loads(c)
# print(e)
import os
def split_songs_name(s) :
    '''
    拆分歌曲名，去掉歌手和一些其他信息，只保留歌曲名
    :param s: 歌曲文件名
    :return: 歌曲名
    '''
    if isinstance(s,str) :
        if s.find('-') :
            return s.split('-')[-1].strip()
        else:
            return s
def get_all_mp3(path) :
    '''
    获取指定目录下所有的.mp3文件，存入一个list中
    :param path: 指定路径
    :return: 歌曲名list
    '''
    songs_list=[]
    for f in os.listdir(path) :
        file_path=os.path.join(path,f)
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1]=='.mp3':
            songs_list.append(split_songs_name(os.path.basename(file_path).split('.')[0]))
        elif os.path.isdir(file_path) :
            get_all_mp3(file_path)
    return songs_list
songs_list=get_all_mp3(r'D:\KuGou')
#指定路径
with open(r'D:\song1.txt','w',encoding='utf-8') as  f:
    '''
    写入指定的txt文件中
    '''
    for s in songs_list:
        f.write(s+'\n')