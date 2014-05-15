#coding=utf-8
'''
Created on 2014年5月15日

@author: 常峰
'''
from PIL import Image

maxLen = 100.0
fontSize = 7
imgname = "r.jpg"

def getIn():
    print u"请输入图像文件名："
    try:
        imgname = raw_input()
    except:
        imgname = "r.jpg"
    print u"请输入最大字符画高/宽："
    try:
        maxLen = input()
    except:
        maxLen = 100.0
    print u"请输入字体："
    try:
        fontSize = input()
    except:
        fontSize = 7

def clearWindow():
    print u" " * 100;
    print   u"""
  *****************************************************************************
                        ASCII码绘图
  *****************************************************************************

                        轻点回车即可开始运行"""
    raw_input()

def gao():
    print u"读取图片文件：%s\n" % imgname
    try:
        img = Image.open(imgname)
    except:
        print u"读取图片出错"
        return
    width, height = img.size
    print u"图片的宽为：%s，高为：%s\n" % (width, height)
    rate = maxLen / max(width, height)
    print u"缩放比例为：%s\n" % rate
    width = int(rate * width)
    height = int(rate * height)
    print u"缩小后的图片宽为：%s，高为：%s\n" % (width, height)
    img = img.resize((width, height))
    pixel = img.load()
    color = "MNHQ$OC?7>!:-;. "
    string = ""
    for h in xrange(height):
        for w in xrange(width):
            rgb = pixel[w, h]
            string += color[int(sum(rgb)/3.0/256.0*16)]
        string += "\n"
    template = """<!DOCTYPE HTML>
    <html>
        <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <style type="text/css" media="all">
        pre {
            white-space: pre-wrap;       /* css-3 */
            white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */
            white-space: -pre-wrap;      /* Opera 4-6 */
            white-space: -o-pre-wrap;    /* Opera 7 */
            word-wrap: break-word;       /* Internet Explorer 5.5+ */
            font-family: 'Inconsolata', 'Consolas'!important;
            line-height: 1.0;
            font-size: %dpx;
        }
        </style>
        </head>
        <body>
        <pre>%s</pre>
        </body>
    </html>
"""
    html = template % (fontSize, string)
    f = open("out.html","w")
    f.write(html)
    f.close()
    #sys.stdout.write(html)
    #sys.stdout.flush()
clearWindow()
getIn()
gao()

    