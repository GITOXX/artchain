#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import time, urllib2, json

## last page of feed shows []
# wget "https://hack.ether.camp/api/feed?group=ALL&page=345"
# []
#so page starts at 344
# wget "https://hack.ether.camp/api/feed?group=ALL&page=344"
# [{"id":2,"createdAt":1479388923295,"jsonData":"{\"header\":\"Code Dweller, alex are new members of Demo Camp\",\"description\":\"\",\"code\":\"DEM\",\"avatarUrls\":[\"api/files/images/7\",\"api/files/images/8\"],\"usernames\":[\"Code Dweller\",\"alex\"],\"campName\":\"Demo Camp\"}","votesTotal":2,"upvoted":null,"type":"MEMBER_JOINED","commentsCount":1,"comments":[{"id":1,"userId":26960,"itemId":2,"createdAt":1479388963545,"text":"Nice selfie :-D&nbsp;","avatarUrl":"api/files/images/469","nickname":"tyrl"}],"urlForShare":"https://hack.ether.camp/feed-item/2","campSlug":"demo-camp"},{"id":3,"createdAt":1479388896156,"jsonData":"{\"header\":\"Published a new presentation\",\"description\":\"The platform of <hack.ether.camp> is ongoing experiment \\naiming to give any person on the planned financial potential \\nto create a startup. We are connecting the worlds of the \\nsocial networks and smart contracts, we study how filter and \\npush real innovation to front lines to give backers a good \\nchase to identify the best opportunities upfront.\",\"code\":\"DEM\",\"campName\":\"Demo Camp\",\"coverUrl\":\"/api/files/images/5\",\"presentation\":\"<iframe src=\\\"https://docs.google.com/presentation/d/1GvcN04nwVLL7nilC2QrPp5V9MLdCN2WbJv0EbMdLTQ4/embed?start=false&loop=false&delayms=3000\\\" frameborder=\\\"0\\\" width=\\\"960\\\" height=\\\"569\\\" allowfullscreen=\\\"true\\\" mozallowfullscreen=\\\"true\\\" webkitallowfullscreen=\\\"true\\\"></iframe>\",\"presentationThumbnailUrl\":\"/api/files/images/6\"}","votesTotal":2,"upvoted":null,"type":"PRESENTATION_UPLOADED","commentsCount":null,"comments":null,"urlForShare":"https://hack.ether.camp/feed-item/3","campSlug":"demo-camp"},{"id":1,"createdAt":1479388609561,"jsonData":"{\"header\":\"New camp Demo Camp was created\",\"description\":\"The platform of <hack.ether.camp> is ongoing experiment \\naiming to give any person on the planned financial potential \\nto create a startup. We are connecting the worlds of the \\nsocial networks and smart contracts, we study how filter and \\npush real innovation to front lines to give backers a good \\nchase to identify the best opportunities upfront.\",\"code\":\"DEM\",\"coverUrl\":\"/api/files/images/5\",\"campName\":\"Demo Camp\"}","votesTotal":1,"upvoted":null,"type":"CAMP_CREATED","commentsCount":null,"comments":null,"urlForShare":"https://hack.ether.camp/feed-item/1","campSlug":"demo-camp"}]
## ok let's fetch every page of the feed and insert into file.
## pages of the feed relay events, such as signup time, vote time and more.
## we can find the correlation with events on the smart contract for kudos later on, 
## then find out which votes belong to which facebook id, voting partern and more.
def feedpageContent(pageNum):
	pagecontent = urllib2.urlopen("https://hack.ether.camp/api/feed?group=ALL&page="+str(pageNum))
	return pagecontent.read()
# firstpage = feedpageContent(344)
# print firstpage
# [{"id":2,"createdAt":1479388923295,"jsonData":"{\"header\":\"Code Dweller, alex are new members of Demo Camp\",\"description\":\"\",\"code\":\"DEM\",\"avatarUrls\":[\"api/files/images/7\",\"api/files/images/8\"],\"usernames\":[\"Code Dweller\",\"alex\"],\"campName\":\"Demo Camp\"}","votesTotal":2,"upvoted":null,"type":"MEMBER_JOINED","commentsCount":1,"comments":[{"id":1,"userId":26960,"itemId":2,"createdAt":1479388963545,"text":"Nice selfie :-D&nbsp;","avatarUrl":"api/files/images/469","nickname":"tyrl"}],"urlForShare":"https://hack.ether.camp/feed-item/2","campSlug":"demo-camp"},{"id":3,"createdAt":1479388896156,"jsonData":"{\"header\":\"Published a new presentation\",\"description\":\"The platform of <hack.ether.camp> is ongoing experiment \\naiming to give any person on the planned financial potential \\nto create a startup. We are connecting the worlds of the \\nsocial networks and smart contracts, we study how filter and \\npush real innovation to front lines to give backers a good \\nchase to identify the best opportunities upfront.\",\"code\":\"DEM\",\"campName\":\"Demo Camp\",\"coverUrl\":\"/api/files/images/5\",\"presentation\":\"<iframe src=\\\"https://docs.google.com/presentation/d/1GvcN04nwVLL7nilC2QrPp5V9MLdCN2WbJv0EbMdLTQ4/embed?start=false&loop=false&delayms=3000\\\" frameborder=\\\"0\\\" width=\\\"960\\\" height=\\\"569\\\" allowfullscreen=\\\"true\\\" mozallowfullscreen=\\\"true\\\" webkitallowfullscreen=\\\"true\\\"></iframe>\",\"presentationThumbnailUrl\":\"/api/files/images/6\"}","votesTotal":2,"upvoted":null,"type":"PRESENTATION_UPLOADED","commentsCount":null,"comments":null,"urlForShare":"https://hack.ether.camp/feed-item/3","campSlug":"demo-camp"},{"id":1,"createdAt":1479388609561,"jsonData":"{\"header\":\"New camp Demo Camp was created\",\"description\":\"The platform of <hack.ether.camp> is ongoing experiment \\naiming to give any person on the planned financial potential \\nto create a startup. We are connecting the worlds of the \\nsocial networks and smart contracts, we study how filter and \\npush real innovation to front lines to give backers a good \\nchase to identify the best opportunities upfront.\",\"code\":\"DEM\",\"coverUrl\":\"/api/files/images/5\",\"campName\":\"Demo Camp\"}","votesTotal":1,"upvoted":null,"type":"CAMP_CREATED","commentsCount":null,"comments":null,"urlForShare":"https://hack.ether.camp/feed-item/1","campSlug":"demo-camp"}]
i = 0 # number of first page of feed.
# quick test before large feed.
# while i > 342:
# 	print feedpageContent(i)
# 	i = i-1
# 	[{"id":2,"createdAt":1479388923295,"jsonData":"{\"header\":\"Code Dweller, alex are new members of Demo Camp\",\"description\":\"\",\"code\":\"DEM\",\"avatarUrls\":[\"api/files/images/7\",\"api/files/images/8\"],\"usernames\":[\"Code Dweller\",\"alex\"],\"campName\":\"Demo Camp\"}","votesTotal":2,"upvoted":null,"type":"MEMBER_JOINED","commentsCount":1,"comments":[{"id":1,"userId":26960,"itemId":2,"createdAt":1479388963545,"text":"Nice selfie :-D&nbsp;","avatarUrl":"api/files/images/469","nickname":"tyrl"}],"urlForShare":"https://hack.ether.camp/feed-item/2","campSlug":"demo-camp"},{"id":3,"createdAt":1479388896156,"jsonData":"{\"header\":\"Published a new presentation\",\"description\":\"The platform of <hack.ether.camp> is ongoing experiment \\naiming to give any person on the planned financial potential \\nto create a startup. We are connecting the worlds of the \\nsocial networks and smart contracts, we study how filter and \\npush real innovation to front lines to give backers a good \\nchase to identify the best opportunities upfront.\",\"code\":\"DEM\",\"campName\":\"Demo Camp\",\"coverUrl\":\"/api/files/images/5\",\"presentation\":\"<iframe src=\\\"https://docs.google.com/presentation/d/1GvcN04nwVLL7nilC2QrPp5V9MLdCN2WbJv0EbMdLTQ4/embed?start=false&loop=false&delayms=3000\\\" frameborder=\\\"0\\\" width=\\\"960\\\" height=\\\"569\\\" allowfullscreen=\\\"true\\\" mozallowfullscreen=\\\"true\\\" webkitallowfullscreen=\\\"true\\\"></iframe>\",\"presentationThumbnailUrl\":\"/api/files/images/6\"}","votesTotal":2,"upvoted":null,"type":"PRESENTATION_UPLOADED","commentsCount":null,"comments":null,"urlForShare":"https://hack.ether.camp/feed-item/3","campSlug":"demo-camp"},{"id":1,"createdAt":1479388609561,"jsonData":"{\"header\":\"New camp Demo Camp was created\",\"description\":\"The platform of <hack.ether.camp> is ongoing experiment \\naiming to give any person on the planned financial potential \\nto create a startup. We are connecting the worlds of the \\nsocial networks and smart contracts, we study how filter and \\npush real innovation to front lines to give backers a good \\nchase to identify the best opportunities upfront.\",\"code\":\"DEM\",\"coverUrl\":\"/api/files/images/5\",\"campName\":\"Demo Camp\"}","votesTotal":1,"upvoted":null,"type":"CAMP_CREATED","commentsCount":null,"comments":null,"urlForShare":"https://hack.ether.camp/feed-item/1","campSlug":"demo-camp"}]
# 	[{"id":8,"createdAt":1479392389727,"jsonData":"{\"header\":\"New camp HackerGoldCard was created\",\"description\":\"Exclusive Hackergold club card for Hackers.\\n\\nDistributed Hacker Sourcing: Pay less anywhere anytime\\n\\n24/7 365 Global Concierge Service, \\nAccess to Hacking / Coding WorkSpace with high speed Internet\\nHackerHouse Airbnb but cooler\\n\\n\\nWe aim to mesh together\\n\\nWework\\nAirBnB\\nJust Eat\\nUber\\n\\nThen Customise it just for your needs.\",\"code\":\"007\",\"coverUrl\":\"/api/files/images/21\",\"campName\":\"HackerGoldCard\"}","votesTotal":6,"upvoted":null,"type":"CAMP_CREATED","commentsCount":null,"comments":null,"urlForShare":"https://hack.ether.camp/feed-item/8","campSlug":"hackergoldcard"},{"id":7,"createdAt":1479392199392,"jsonData":"{\"header\":\"LoveStory.io - Register your Relationships in Blockchain ÔÇö join to team or connecting like fan! We -...\",\"description\":\"LoveStory.io - Register your Relationships in Blockchain ÔÇö join to team or connecting like fan! We - Best! We - Win! Watch livestream with developer! More info later ))\",\"code\":\"LRN\",\"campName\":\"LoveStory.io - Register your Relationships in Blockchain\",\"message\":\"LoveStory.io - Register your Relationships in Blockchain ÔÇö join to team or connecting like fan! We - Best! We - Win! Watch livestream with developer! More info later ))\"}","votesTotal":1,"upvoted":null,"type":"CAMP_MESSAGE","commentsCount":null,"comments":null,"urlForShare":"https://hack.ether.camp/feed-item/7","campSlug":"lovestoryio---register-your-relationships-in-blockchain"},{"id":6,"createdAt":1479392068004,"jsonData":"{\"header\":\"New camp LoveStory.io - Register your Relationships in Blockchain was created\",\"description\":\"Create your LoveCoin and divide it with ourlove. Open and secure. The real proof of your relationship or check the integrity of your partner!\\n\\nIdea\\nThink of this. IsnÔÇÖt it would be fun to marry in blockchain? You and your partner will be having your own personal spot in blockchain community where you will always be together. Maybe not always, because nobody is ensured from divorce, but isnÔÇÖt it cool to have that opportunity? \\n\\n\\nThe problem\\nA lot of people does not trust the government local institutions of marriage or does not like that you need to marry in Chirch even though people have their own belief outside the christian religion, some people does not see significance in marrying by government rules..\\n\\n\\nThe soultion\\nWhat if there will be no rules in marrying, like a couple will have their own statement between each other and only they wll know this, and this will be stored permanently in the global information network\\n\\n\\nGoals\\nCreate the service that provides the ability to get married with the power of blockchain network\\nMake it look simple and beautiful\\n\\nRoadmap  v 1.0\\nComing Soon!!\\n\\n\\nPersonal statement\\nWe believe that many aspects of our lives will be reflected in blockchain networks in one way or another. We believe that making something in blockchain is more valuable other than on a simple paper written by some dudes and that are stored in some centralized place from where it could be changed, stolen or lost. When you make this on blockchain everyone is witness of your will to say something to people and yourself and this will not be lost. We are the guys that want to participate in this technological revolution by giving to you the piece of our contribution in blockchain society. \\n\\nLovestory.camp https://hack.ether.camp/public/lovestoryio---register-your-relationships-in-blockchain\\nWebsite http://lovestory.io\\nExplorer http://lovechain.io\",\"code\":\"LRN\",\"coverUrl\":\"/api/files/images/521\",\"campName\":\"LoveStory.io - Register your Relationships in Blockchain\"}","votesTotal":1,"upvoted":null,"type":"CAMP_CREATED","commentsCount":1,"comments":[{"id":2,"userId":26960,"itemId":6,"createdAt":1479392161066,"text":"First camp besides our demo, good luck !!!","avatarUrl":"api/files/images/469","nickname":"tyrl"}],"urlForShare":"https://hack.ether.camp/feed-item/6","campSlug":"lovestoryio---register-your-relationships-in-blockchain"},{"id":5,"createdAt":1479391087315,"jsonData":"{\"header\":\"Mikhail is a new member of Demo Camp\",\"description\":\"\",\"code\":\"DEM\",\"avatarUrls\":[\"api/files/images/10\"],\"usernames\":[\"Mikhail\"],\"campName\":\"Demo Camp\"}","votesTotal":2,"upvoted":null,"type":"MEMBER_JOINED","commentsCount":null,"comments":null,"urlForShare":"https://hack.ether.camp/feed-item/5","campSlug":"demo-camp"},{"id":4,"createdAt":1479389756879,"jsonData":"{\"header\":\"tyrl just bought a beer to the Demo Camp\",\"description\":\"The platform of <hack.ether.camp> is ongoing experiment \\naiming to give any person on the planned financial potential \\nto create a startup. We are connecting the worlds of the \\nsocial networks and smart contracts, we study how filter and \\npush real innovation to front lines to give backers a good \\nchase to identify the best opportunities upfront.\",\"code\":\"DEM\",\"campName\":\"Demo Camp\",\"coverUrl\":\"/api/files/images/5\",\"avatarUrl\":\"api/files/images/469\"}","votesTotal":1,"upvoted":null,"type":"BEER_BOUGHT","commentsCount":null,"comments":null,"urlForShare":"https://hack.ether.camp/feed-item/4","campSlug":"demo-camp"}]
f = open("./feed.hack.ether.camp.all.txt", 'w')
# fech all feed items, each page has 5, the last page is 344. count to 345.
while i < 345:
 	# print feedpageContent(i)
 	f.write("%s\n" % feedpageContent(i))
 	print i
 	i = i+1