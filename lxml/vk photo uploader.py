#!/usr/bin/python 
# -*- coding: utf-8 -*-

import vkontakte
#http://oauth.vk.com/authorize?client_id=3005027&scope=photos&response_type=token
access_token='b87a1590f672af6bb9fc2208ccb9bc565dbb991b9918c3acb198b51fb8a763e'
vk = vkontakte.API('3005027', 'CCPBRlLqZaSb2pY1LaU2')
vk = vkontakte.API(token=access_token)
upload_url_=vk.photos.getUploadServer(aid=vk.photos.getAlbums()[0]['aid'])['upload_url']
import requests
img_from=1832
blocks=1
block_size=1
img = img_from
import json
print 'well connected, start upload by blocks of '+str(block_size)+' files'
while img<img_from+blocks*block_size:
   ok = False
   while not ok:
      try:
         files = {}
         for f in range(1,block_size+1):
            files['file'+str(f)]= open('/home/argon/py/lxml/artkritka/'+str(img+f-1)+'.jpg', 'rb')
         #print files.__str__()+"\n\n"
         r=requests.post(upload_url_,files=files)
         s=json.loads(r.text)
         vk.photos.save(aid=s['aid'],server=s['server'],photos_list=s['photos_list'],hash=s['hash'])
         img+=block_size
         print 'last uploaded file:'+str(img-1)+'.jpg'
         ok = True
      except Exception, e:
         print 'error, try again'
