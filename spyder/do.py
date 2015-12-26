import urllib.request
import re

def getHtml(url):
        page = urllib.request.urlopen(url)
        html = page.read()
        #print(html)
        return html

def getImg(html):
        regObj = re.compile('src="([http:\/\/]{0,7}[\/_\w,&=\.]+\.[jpngif]{3})"')
        imgList = re.findall(regObj, html)
        x=0
        print(imgList)
        for imgUrl in imgList:
                imgUrl = "http://management.dlut.edu.cn/" + imgUrl
                print(imgUrl)
                urllib.request.urlretrieve(imgUrl, './%s.jpg'%x)
                x+=1
        pass

html = getHtml('http://management.dlut.edu.cn/')
#getImg('src="http://img2.bdstatic.com/static/home/widget/search_box_home/shitu/images/camera_b659d28.png")')
#getImg('src="http://baidu.png"')
getImg(str(html))
input()
