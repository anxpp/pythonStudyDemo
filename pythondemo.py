from flask import Response, Flask
import matplotlib.pyplot as plt
from io import BytesIO
from wordcloud import WordCloud
import urllib.request
import jieba
import re
import numpy as np
from PIL import Image

app = Flask(__name__)


@app.route('/')
def hello_world():
    fp = urllib.request.urlopen("http://www.en8848.com.cn/article/beauty/health/71449.html")
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    print(mystr)
    fp.close()
    wordlist_after_jieba = jieba.cut(mystr, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)
    # abel_mask = np.array(Image.open("c:/2.jpg"))
    wc = WordCloud()
    my_wordcloud = wc.generate(wl_space_split)
    plt.imshow(my_wordcloud)
    # plt.fill()
    plt.axis("off")
    img = BytesIO()
    plt.savefig(img, dpi=314)
    img.seek(0)
    return Response(img, mimetype='image/png')


if __name__ == '__main__':
    app.run()
