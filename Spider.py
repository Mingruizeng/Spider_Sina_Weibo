import requests
import json
from config import headers,Cookie
import time
import os
from urllib import request
from hashlib import md5
import cryptography
#import pyopenssl
import certifi

def save_video(url):
    video_path = 'Weibo_data' + os.path.sep + '湖北' + os.path.sep + id
    if not os.path.exists(video_path):
        os.makedirs(video_path) # 生成目录文件夹
    try:
        resp = requests.get(url)
        if requests.codes.ok == resp.status_code:
            file_path = video_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(),
                file_suffix='mp4')  # 单一文件的路径
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded video path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except Exception as e:
        print(e,'none123')

def save_image(id,url):
    img_path = 'Weibo_data' + os.path.sep + '湖北' + os.path.sep + id
    if not os.path.exists(img_path):
        os.makedirs(img_path) # 生成目录文件夹
    try:
        resp = requests.get(url)
        if requests.codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(),
                file_suffix='jpg')  # 单一文件的路径
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except Exception as e:
        print(e,'none123')

def write_into_files(text, reposts_count, comments_count, attitudes_count, author_name): #写入函数
    data_path = 'Weibo_data' + os.path.sep + '湖北' + os.path.sep + id
    if not os.path.exists(data_path):
        os.makedirs(data_path) # 生成目录文件夹
    with open(data_path + os.path.sep + 'data.txt', 'a+', encoding='utf-8') as f:
        f.write('微博正文:' + str(text) + '\n')
        f.write('转发数:' + str(reposts_count) + '\n')
        f.write('评论数:' + str(comments_count) + '\n')
        f.write('点赞数:' + str(attitudes_count) + '\n')
        f.write('发布作者:' + str(author_name) + '\n')

def get_comments(url_comment,headers):  # 进入每条微博的第一页评论并获取信息
    response = requests.get(url_comment,headers=headers,cookies=Cookie,timeout=120,verify=False)  # 进入微博评论区
    data = response.json()  # 取出字典
    data_path = 'Weibo_data' + os.path.sep + '湖北' + os.path.sep + id
    #print('返回状态' + str(response.status_code))
    if data['ok'] == 0:#判断微博是否有评论
        return 0
    else:
        max_id = data['data']['max_id']  # 获取max_id为判断是否需要翻页操作做准备
    users = data.get('data', None)
    if users:        #每一页的评论信息
        users = users['data']
        for user in users:
            created_time = user['created_at']  # 评论时间
            text_comment = user['text']  # 评论内容
            user_name = user['user']['screen_name']  # 用户昵称
            print('评论时间：' + str(created_time))
            print('评论内容：' + str(text_comment))
            print('用户昵称：' + str(user_name))
            with open(data_path + os.path.sep + 'data.txt', 'a+', encoding='utf-8') as f:
                f.write('评论时间:' + str(created_time)+'\n')
                f.write('评论内容:' + str(text_comment)+'\n')
                f.write('用户昵称:' + str(user_name)+'\n')
        time.sleep(5)
        return max_id

#热搜检索关键字——新冠肺炎网址
url_weibo = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E6%B9%96%E5%8C%97&page_type=searchall&page={i}'
 #循环page获取每页url
for i in range(0,100,1):
    response = requests.get(url_weibo.format(i=i),headers=headers,cookies=Cookie,timeout=120,verify=False)
    ob_json = response.json()
    list_cards = ob_json['data']['cards']
    for card in list_cards:
        if card.get('card_type') == 9:
        #获取每条微博id，为爬取对应评论做准备
            id = card['mblog']['id']
            print('id', id)
            if card['mblog'].get('page_info',None):
                if card['mblog']['page_info'].get('media_info',None):
                    video_url = card['mblog']['page_info']['media_info']['stream_url']
                    save_video(video_url)   #保存视频
                    time.sleep(5)
            if card['mblog'].get('pics', None):  # 判断是否有图片，并获取图片的url
                for pic in card['mblog']['pics']:
                    pic_url = pic['url']  # 获取图片url
                    save_image(id,pic_url)  #保存图片
                    time.sleep(5)
            if card['mblog']['isLongText']:#判断是否为查看全文
                text = card['mblog']['longText']['longTextContent']  # 长微博正文
            else:
                text = card['mblog']['text']                      #短微博正文
            reposts_count = card['mblog']['reposts_count']        #转发数
            comments_count = card['mblog']['comments_count']      #评论数
            attitudes_count = card['mblog']['attitudes_count']    #点赞数
            author_name = card['mblog']['user']['screen_name']    #发布作者
            write_into_files(text, reposts_count, comments_count, attitudes_count, author_name)
            #time.sleep(1)
            print('微博正文:' + str(text))
            print('转发数:' + str(reposts_count))
            print('评论数:' + str(comments_count))
            print('点赞数:' + str(attitudes_count))
            print('发布作者:' + str(author_name))

            #进入每条微博评论url
            url_comment = 'https://m.weibo.cn/comments/hotflow?id={id}&mid={id}&max_id_type=0'.format(id=id)
            max_id = get_comments(url_comment,headers)

            while max_id != 0:
                url_comment = 'https://m.weibo.cn/comments/hotflow?id={id}&mid={id}&max_id={max_id}&max_id_type=0'.format(id=id,max_id=max_id)
                max_id = get_comments(url_comment,headers)
    print('-----------------------------------------------------------------第',i+1,'篇微博信息爬取完毕-------------------------------------------------------------')
print('执行完毕，当前时间为： ',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))









