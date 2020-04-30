# -*- coding:utf-8 -*-
import threading
import urllib.request
import networkx as nx
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup

import importlib, sys
importlib.reload(sys)

DEEP = 5

def addListUrl(url,upTitle = None,upName = None,upMap = None,deep = 0):
    if deep == DEEP:
        return {}

    map = {}

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')

    liResutl = soup.findAll('a', attrs={"nslog-type": "10000302"})

    l = list(range(len(liResutl)))
    for i in l:
        name = liResutl[i].find('span', attrs={"class": "name"}).get_text()
        title = liResutl[i].find('span', attrs={"class": "title"}).get_text()
        href = liResutl[i].get('href')
        if title not in G.nodes:
            size.append((DEEP-deep)*500)
            color.append(colorList[deep+1])
        G.add_edge(upTitle,title)
        TabelList[(upTitle,title)] = upName
        addListUrl("https://baike.baidu.com" + href,title, name, map, deep + 1)

    if upMap == None or upTitle == None or upName == None:
        return map
    else:
        upMap[upTitle] = [upName, map]


G = nx.DiGraph()
TabelList = {}
size = [DEEP*1000]
colorList = [(255/255,127/255,0),(234/255,213/255,110/255),(47/255,135/255,62/255),(67/255,160/255,180/255),(57/255,154/255,232/255),(36/255,83/255,146/255)]
color = [colorList[0]]
print(addListUrl("https://baike.baidu.com/item/%E6%9C%B1%E5%85%83%E7%92%8B/25626?fr=aladdin",upTitle = '朱元璋'))
pos=nx.spring_layout(G, k=10/(len(G.nodes)**0.5),scale=2,pos={'朱元璋':[0,0]})
nx.draw_networkx(G,pos,font_family ="SimHei",font_size = 10,node_size=size,node_color=color)
nx.draw_networkx_edge_labels(G,pos=pos, font_family ="SimHei",edge_labels = TabelList,font_size=6)
plt.show()

