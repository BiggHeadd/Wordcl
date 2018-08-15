from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np

if __name__ == "__main__":
    coloring = np.array(Image.open("timg.jpg"))
    with open("kobe.txt", 'r', encoding='utf-8')as f:
        kobe = f.read()
    jieba_cut = jieba.cut(kobe)
    jieba_result = " ".join(jieba_cut)
    # jieba_result.encode("unicode")
    wordcloud = WordCloud(max_words=10000, font_path="C:/Windows/Fonts/STFANGSO.ttf", mask=coloring, background_color="white").generate(jieba_result)
    image_color = ImageColorGenerator(coloring)

    plt.imshow(wordcloud.recolor(color_func=image_color), interpolation='bilinear')
    plt.axis("off")
    plt.show()