# 酷狗音乐的爬虫

## 获取所有歌手的singername 和singerid
* 思路：按照华语男、华语女、华语组合、欧美男、欧美女、欧美组合、日本男、日本女、日本组合、韩国男、韩国女、韩国组合、其他歌手 的不同的type 和 sextype，构造url，进行爬取
* http://mobilecdnbj.kugou.com/api/v5/singer/list?musician=0&type=%s&showtype=2&sextype=%s&with_res_tag=1

## 获取某歌手的歌曲数目，mv数目，简介等
* 思路：按照不同歌手的singerid，构造url，进行爬取
* http://mobilecdnbj.kugou.com/api/v3/singer/info?singerid=%s&with_res_tag=1

## 获取某歌手的所有歌曲
* 思路：按照不同歌手的singerid、page，构造url，分页获取所有的歌曲名
* http://mobilecdnbj.kugou.com/api/v3/singer/song?plat=0&page=%s&sorttype=2&pagesize=30&version=8800&singerid=%s&with_res_tag=1

## 酷狗提供的搜索功能
* 思路：按照不同的keyword、page，构造url，分页获取所有的搜索结果
* http://mobilecdnbj.kugou.com/api/v3/search/song?showtype=14&tag=1&tagtype=%e5%85%a8%e9%83%a8&tag_aggr=1&version=8800&keyword=回忆总想哭&highlight=em&plat=0&sver=5&correct=1&api_ver=1&pagesize=30&with_res_tag=1&page=1