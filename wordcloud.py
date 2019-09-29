# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:52:53 2019

@author: Vlad
"""

import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

df = pd.read_csv('articles.csv', encoding='cp1252', header = None)

stopwords = set(STOPWORDS)

def Mywordcloud(data, title = None):
    wordcloud= WordCloud(
            background_color = 'white',
            stopwords = stopwords,
            max_words = 50,
            max_font_size = 40,
            scale = 3,
            random_state = 1).generate(str(data))
    
    fig = plt.figure(1, figsize = (20, 20))
    plt.axis('off')
    if title:
        fig.subtitle(title, fontsize = 20)
        fig.subplots_adjust(top = 2.3)
        
    plt.imshow(wordcloud)
    plt.show()
    
    Mywordcloud(df[0].dropna())