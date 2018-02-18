# coding=utf-8
paras = [{u"类别":u"华语男",u"参数":{u"type":1,u"sextype":1}},{u"类别":u"华语女",u"参数":{u"type":1,u"sextype":2}},{u"类别":u"华语组合",u"参数":{u"type":1,u"sextype":3}},{u"类别":u"欧美男",u"参数":{u"type":2,u"sextype":1}},{u"类别":u"欧美女",u"参数":{u"type":2,u"sextype":2}},{u"类别":u"欧美组合",u"参数":{u"type":2,u"sextype":3}},{u"类别":u"日本男",u"参数":{u"type":5,u"sextype":1}},{u"类别":u"日本女",u"参数":{u"type":5,u"sextype":2}},{u"类别":u"日本组合",u"参数":{u"type":5,u"sextype":3}},{u"类别":u"韩国男",u"参数":{u"type":6,u"sextype":1}},{u"类别":u"韩国女",u"参数":{u"type":6,u"sextype":2}},{u"类别":u"韩国组合",u"参数":{u"type":6,u"sextype":3}},{u"类别":u"其他歌手",u"参数":{u"type":4,u"sextype":0}}]
paras = [{u"类别":u"日本组合",u"参数":{u"type":5,u"sextype":3}},{u"类别":u"韩国男",u"参数":{u"type":6,u"sextype":1}},{u"类别":u"韩国女",u"参数":{u"type":6,u"sextype":2}},{u"类别":u"韩国组合",u"参数":{u"type":6,u"sextype":3}},{u"类别":u"其他歌手",u"参数":{u"type":4,u"sextype":0}}]

import HtmlDownloader,HtmlOutputer
import JsonUtils
import IOUtils
def parseJson(html_cont):
    ju = JsonUtils.JsonUtils()
    jsonCont = ju.formatJson(html_cont)
    d = ju.readStr(jsonCont)
    data = d[u"data"]
    return data[u'songcount']
    


io = IOUtils.IOUtils()
ho = HtmlOutputer.HtmlOutputer()
for para in paras:
    dirName = u"F:\\kgyy\\artist\\"+para[u'类别']+u"_带歌曲数"
    artists = io.getListOrDictFromJsonFile(u"F:\\kgyy\\artist\\%s.json"  %(para[u'类别']))
    L=[]
    for artist in artists:
        #print id,num
        name = artist[u'singername']
        id = artist[u'singerid']
        url = u"http://mobilecdnbj.kugou.com/api/v3/singer/info?singerid=%s&with_res_tag=1" %(id)
        hd = HtmlDownloader.HtmlDownloader()
        html_cont = hd.download(url)
        while html_cont is None:
            print id,u"retrying..."
            html_cont = hd.download(url)
        num = parseJson(html_cont)
        num = unicode(str(num))
        d = {u'singername':name,u'singerid':id,u'num':num}
        L.append(d)

    io.writeListOrDict2JsonFile(dirName+u".json",L)
    io.writeList2TxtFile(dirName+u'.txt',L)
    ho.output_html(dirName+u'.html',L)
