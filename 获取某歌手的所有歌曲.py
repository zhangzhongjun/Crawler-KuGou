# coding=utf-8
import IOUtils
import JsonUtils
import HtmlDownloader
class GetSongs(object):
    def __init__(self,singerid,num):
        self.singerid = singerid
        self.num = num
    
    def __getUrl__(self,page):
        return u'http://mobilecdnbj.kugou.com/api/v3/singer/song?plat=0&page=%s&sorttype=2&pagesize=30&version=8800&singerid=%s&with_res_tag=1' %(unicode(str(page),'utf-8'),unicode(str(self.singerid),'utf-8'))
    
    def getUrls(self):
        if not isinstance(self.num,int):
            num = int(self.num)
        else:
            num = self.num
        if num%30==0:
            pageNum = num/30
        else:
            pageNum = num/30+1
        i = 1
        L=[]
        while i<=pageNum:
            L.append(self.__getUrl__(i))
            i= i+1
        return L

    def parseJson(self,html_cont):
        ju = JsonUtils.JsonUtils()
        jsonCont = ju.formatJson(html_cont)
        d = ju.readStr(jsonCont)
        
        infos = d[u"data"][u'info']
        L = []
        for info in infos:
            filename = info[u'filename']
            L.append(filename)
        return L

    def getSongs(self):
        L=[]
        urls = self.getUrls()
        for url in urls:
            hd = HtmlDownloader.HtmlDownloader()
            html_cont = hd.download(url)
            while html_cont is None:
                print id,u"retrying..."
                html_cont = hd.download(url)
            res = self.parseJson(html_cont)
            L.extend(res)
        return L

