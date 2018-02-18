# coding=utf-8
import HtmlDownloader
import HtmlOutputer
import GetSongs
import IOUtils
import threading
from time import ctime,sleep
import JsonUtils

def parseJson(html_cont):
    ju = JsonUtils.JsonUtils()
    jsonCont = ju.formatJson(html_cont)
    d = ju.readStr(jsonCont)
    data = d[u"data"]
    infos = data[u'info']
    L = []
    if len(infos)==0:
        return False,L
    for info in infos:
        L.append(info[u'filename'])
    return True,L


io = IOUtils.IOUtils()
ho = HtmlOutputer.HtmlOutputer()
#纯音乐
cyy=u'%e7%ba%af%e9%9f%b3%e4%b9%90'
page=1
#纯音乐
url1=u"http://mobilecdnbj.kugou.com/api/v3/search/song?showtype=14&tag=1&tagtype=%e5%85%a8%e9%83%a8&tag_aggr=1&version=8800&keyword="+cyy+u"&highlight=em&plat=0&sver=5&correct=1&api_ver=1&pagesize=30&with_res_tag=1&page="
#dj
url2=u"http://mobilecdnbj.kugou.com/api/v3/search/song?showtype=14&tag=1&tagtype=%e5%85%a8%e9%83%a8&tag_aggr=1&version=8800&keyword=dj&highlight=em&plat=0&sver=5&correct=1&api_ver=1&pagesize=30&with_res_tag=1&page="
#纯音乐
songDirName1=u'F:\\kgyy\\song3\\纯音乐'
#dj
songDirName2=u'F:\\kgyy\\song3\\dj'
L=[]
t = True
while page<100 and t:
    url = url1+str(page)
    page = page+1
    hd = HtmlDownloader.HtmlDownloader()
    html_cont = hd.download(url)
    while html_cont is None:
        print page,u"retrying..."
        html_cont = hd.download(url)
    t,songs = parseJson(html_cont)
    print t,len(songs)
    L.extend(songs)
print len(L)
io.writeListOrDict2JsonFile(songDirName1+u".json",L)
io.writeList2TxtFile(songDirName1+u'.txt',L)
ho.outputList2html(songDirName1+u'.html',L)
