from wordcloud import WordCloud

from temp import 网易云音乐歌曲热门评论 as hot
text = " ".join(hot.getcomments(439915614))

wordcloud = WordCloud(random_state=1, font_path = r'C:/Users/Windows/fonts/simkai.ttf').generate(text)

import matplotlib.pyplot as plt
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()