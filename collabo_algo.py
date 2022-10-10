import pandas as pd
import numpy as np
import numpy as np

#데이터 준비
rating_data = pd.read_csv('./ratings.csv')
wine_data = pd.read_csv('./wines.csv')

#필요없는 컬럼삭제
rating_data.drop('컬럼명 이름을 적어주세요', axis=1, inplace=True)

wine_data.drop('컬럼명 이름을 적어주세요', axis=1, inplace=True)

#와인데이터와 평점데이터를 머지
user_wine_data = pd.merge(rating_data, wine_data, )
