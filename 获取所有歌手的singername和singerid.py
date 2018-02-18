# coding=utf-8
paras = [{u"类别":u"华语男",u"参数":{u"type":1,u"sextype":1}},{u"类别":u"华语女",u"参数":{u"type":1,u"sextype":2}},{u"类别":u"华语组合",u"参数":{u"type":1,u"sextype":3}},{u"类别":u"欧美男",u"参数":{u"type":2,u"sextype":1}},{u"类别":u"欧美女",u"参数":{u"type":2,u"sextype":2}},{u"类别":u"欧美组合",u"参数":{u"type":2,u"sextype":3}},{u"类别":u"日本男",u"参数":{u"type":5,u"sextype":1}},{u"类别":u"日本女",u"参数":{u"type":5,u"sextype":2}},{u"类别":u"日本组合",u"参数":{u"type":5,u"sextype":3}},{u"类别":u"韩国男",u"参数":{u"type":6,u"sextype":1}},{u"类别":u"韩国女",u"参数":{u"type":6,u"sextype":2}},{u"类别":u"韩国组合",u"参数":{u"type":6,u"sextype":3}},{u"类别":u"其他歌手",u"参数":{u"type":4,u"sextype":0}}]
import HtmlDownloader,HtmlOutputer
import JsonUtils
import IOUtils
def parseJson(html_cont):
    ju = JsonUtils.JsonUtils()
    jsonCont = ju.formatJson(html_cont)
    d = ju.readStr(jsonCont)
    info = d[u"data"][u"info"]
    i =1
    L=[]
    while i<28:
        theInfo = info[i]
        title = theInfo[u'title']
        singers = theInfo[u'singer']
        #print title+" "+str(len(singers))
        for singer in singers:
            singername = singer[u"singername"]
            singerid = singer[u'singerid']
            d={u"singername":singername,u"singerid":unicode(str(singerid),'utf-8')}
            L.append(d)
        i = i+1
    return L
#只对华语组合解析 并写入文件
'''
url = "http://mobilecdnbj.kugou.com/api/v5/singer/list?musician=0&type=%s&showtype=2&sextype=%s&with_res_tag=1" %(1,3)
hd = HtmlDownloader.HtmlDownloader()
html_cont = hd.download(url)
L = parseJson(html_cont)
#print "total: "+str(len(L))

io = IOUtils.IOUtils()
io.writeListOrDict2JsonFile("f:\\artis.json",L)
io.writeListOrDict2TxtFile("f:\\artis.txt",L)
ho = HtmlOutputer.HtmlOutputer()
ho.output_html("f:\\artis.html",L)
'''
#读取文件 得到之前写入的华语组合的信息
'''
io = IOUtils.IOUtils()
L = io.getListOrDictFromFile("f:\\artis.json")
print len(L)
'''
# 获取所有歌手的singername 和singerid
io = IOUtils.IOUtils()
ho = HtmlOutputer.HtmlOutputer()
for para in paras:
    dirName = u"F:\\kgyy\\artist\\"+para[u'类别']
    type = para[u'参数'][u'type']
    sextype = para[u'参数'][u'sextype']
    url = "http://mobilecdnbj.kugou.com/api/v5/singer/list?musician=0&type=%s&showtype=2&sextype=%s&with_res_tag=1" %(type,sextype)
    hd = HtmlDownloader.HtmlDownloader()
    html_cont = hd.download(url)
    L = parseJson(html_cont)
    io.writeListOrDict2JsonFile(dirName+u".json",L)
    io.writeList2TxtFile(dirName+u'.txt',L)
    ho.output_html(dirName+u'.html',L)
