# -*- coding: utf-8 -*-
"""Pengs_art.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xyc98EfX84_yRn4aoxCHxLLMU7bSK2rG
"""

from google.colab import drive
drive.mount('/content/gdrive')

import pandas as pd
import seaborn as sns

penguin_file = "/content/gdrive/My Drive/Colab Notebooks/penguins.csv"
penguins = pd.read_csv(penguin_file)

pengs = penguins.dropna()

pengs.columns =['sp','is','bl','bd','fl','ms','sx','yr']

import plotnine as pn

"""#첫 번째 작품: 녹색펭귄
---

감명깊게 읽었던 책 중에 <b>핑크펭귄</b> 이라는 책이 있습니다.

"평범하면 까인다"라는 문장이 서브 타이틀인데요,

무수히 많은 펭귄 중에서 핑크색 펭귄이 한마리라도 있으면 그 펭귄은 어디서든 주목받는 다는 것입니다.  

마케팅에서 핑크펭귄은 굉장히 중요하다고 합니다.

무수히 많은 기업들 중에 하필이면 우리 기업을 골라야할만한 이유를 부여하는 것이기 때문입니다.

저는 반대로 <i>[핑크펭귄]</i> 만 있는 공간에서 핑크색의 보색인 <i>[녹색 펭귄]<i>이 있다면 어떨까 라는 생각을 하게 되었고 이를 그림으로 표현하였습니다.

<u>핑크펭귄도 무수히 많아지면 그저 핑크색펭귄일 뿐인 듯 합니다..!</u>

"""

pn.ggplot(data=pengs, mapping=pn.aes(x='sp', y='yr')) + pn.geom_tile(mapping=pn.aes(fill='ms')) + pn.scale_fill_gradientn(colors=['#FCE4EC','#F8BBD0','#CCFF00','#F06292','#EC407A','#8E24AA','#D81B60','#C2185B','#AD1457','#880E4F','#B71C1C']) + pn.theme_classic() + pn.theme_void() + pn.theme(legend_position='none') + pn.geom_quantile(mapping=pn.aes(x='sp',y='yr'))

"""#두 번째 작품: 상보성
---

<u>서로의 부족함을 채워주는</u> <b>상보성</b>을 그림으로 표현하였습니다.

두 그림을 자세히 보시면, 서로의 빈 공간을 조금씩 채우고 있는 것을 보실 수 있습니다. 

서로가 맞닿으면서 부족함을 채워주는 관계, <b>그리고 그 속에서 긍정의 색인 노란색을 분출</b>하여 상보성이라는 개념을 그림으로 표현하고자 하였습니다.
"""

pengs_bd_ms = pn.ggplot(data=pengs, mapping=pn.aes(x='bd',y='ms',color='yr')) 
pengs_bd_ms + pn.geom_tile(mapping=pn.aes(x='sx',y='ms')) + pn.theme_void() + pn.theme(legend_position='none') + pn.scale_fill_brewer(palette="YIOrRd")