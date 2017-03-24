import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

# text_from_file_with_apath = open('hello.txt').read()

wordlist_after_jieba = jieba.cut("sdf asdf dfh dsfg sda fsadf saf dfgsdfsdb sd", cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud().generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
# plt.show()
plt.savefig("c:/1.jpg")
