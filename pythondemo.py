from flask import Response, Flask
import matplotlib.pyplot as plt
from io import BytesIO
from wordcloud import WordCloud
import urllib.request
import jieba

app = Flask(__name__)


@app.route('/')
def hello_world():
    fp = urllib.request.urlopen("http://www.python.org")
    mybytes = fp.read()
    # note that Python3 does not read the html code as string
    # but as html code bytearray, convert to string with
    mystr = mybytes.decode("utf8")
    fp.close()
    wordlist_after_jieba = jieba.cut(mystr, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)
    my_wordcloud = WordCloud().generate(wl_space_split)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    img = BytesIO()
    plt.savefig(img, dpi=324)
    img.seek(0)
    return Response(img, mimetype='image/png')

if __name__ == '__main__':
    app.run()