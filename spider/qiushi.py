import urllib
from time import sleep

import requests
from lxml import etree



try:
    def all_links(url,page):
        # if "900.html" in url:
        #     print("结束");
        #     return None
        url = url + str(page) + ".html";
        response = requests.get(url)
        print(url, response.status_code)
        html = etree.HTML(response.content.decode('gbk'))
        ## 获取图片 并且保存
        imgs = html.xpath('.//div[@id="wrapper"]//div[@class="ui-module"]//img/@src')
        for img in imgs:
            file_name = img.split('/')[-1]
            first = img.split('/')[0]
            if first != 'http:' and first != 'https:':
                print("错误图片"+img)
            else:
                dir_path = "/www/spider/images/"
                try:
                    file_content = requests.get(img)
                    if file_content.status_code != 200:
                        print(img,"下载失败")
                    else:

                        #urllib.request.urlretrieve(img, dir_path + file_name)
                        with open(dir_path+file_name,"wb") as f:
                            f.write(file_content.content)
                            print("保存图片" + dir_path + file_name + "成功")
                except Exception as ee:
                    print(str(ee))
        # links = html.xpath('.//div[@class="page"]//a[contains(text(),"下一页")]/@href')
        # print(links)
        # if len(links) < 1:
        #     pass
        # else:
        sleep(1)
        host = 'http://www.qiubaichengren.net/'
        next_page = page + 1
        all_links(host,next_page)

    for i in range(1,991):
        all_links("http://www.qiubaichengren.net/",626)
except Exception as e:
    print(str(e))