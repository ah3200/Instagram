__author__ = 'macbookair'
#-*-coding: utf-8 -*-
from instagram.client import InstagramAPI

#Unauthenticated request

api = InstagramAPI(client_id='0a06d69f233d419eb60b7508c4ce2f80', client_secret='ca8423e256cd4d88a66aa00263b1960c')
popular_media = api.media_popular(count=20)

#for media in popular_media:
#    print media
#    print media.images['standard_resolution'].url

tagfind = 'uyuni'
tag1 = api.tag_recent_media(count=20,tag_name=tagfind)
for tag in tag1:
    for media in tag:
        print media.images['standard_resolution'].url
