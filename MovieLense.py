
import numpy as np
import pandas as pd

movies = pd.read_csv("ml-latest-small/movies.csv")
links = pd.read_csv("ml-latest-small/links.csv")
tags = pd.read_csv("ml-latest-small/tags.csv")
ratings = pd.read_csv("ml-latest-small/ratings.csv")


#1. 사용자별 평균평점을 산출하여 제일 높은 사용자와, 제일 낮은 사용자 id 출력

#[출력예시]

#1. 최고평점 : 사용자id (복수일 경우 사용자id1, 사용자id2, .....)

#1. 최저평점 : 사용자id (복수일 경우 사용자id1, 사용자id2, .....)

df=ratings.pivot_table(index="userId", values = "rating",aggfunc=np.mean)


# 최고 평점-내림차순정렬 후 순위1 추출
df['rank1']=df['rating'].rank(method='min', ascending=False)
print("1. 최고평점 userId : ", df[df['rank1']==1].index.values )

# 최저 평점-오른차순정렬 후 순위1 추출
df['rank2']=df['rating'].rank(method='min', ascending=True)
print("2. 최저평점 userId : ", df[df['rank2']==1].index.values )



#2. 영화별 평균평점을 산출하여 제일 높은 영화와 제일 낮은 영화의 제목을 출력

#[출력예시]

#2. 최고평점 : Dracula: Dead and Loving It (1995)  (복수일 경우 , 로 이어서 출력)

#2. 최저평점 : Now and Then (1995) (복수일 경우 , 로 이어서 출력)

df1=ratings.pivot_table(index='movieId', values='rating', aggfunc=np.mean)
#df1['movie'] = df1.index.values

df_mer= pd.merge(df1, movies, on = 'movieId', how='left', sort=False)

# 최고 평점-내림차순정렬 후 순위1 추출
df_mer['rank1']=df_mer['rating'].rank(method='min', ascending=False)
print("3. 최고평점 movie : ", df_mer[df_mer['rank1']==1]['title'].values)

# 최저 평점-오른차순정렬 후 순위1 추출
df_mer['rank2']=df_mer['rating'].rank(method='min', ascending=True)
print("4. 최저평점 movie : ", df_mer[df_mer['rank2']==1]['title'].values)

#3. 범죄스릴러(Crime, Thriller) 장르에서 최고 평점을 얻은 영화의 제목을 출력 :  

#[출력예시]

#3. 범죄스릴러 장르 최고평점 : Kiss of Death (1995)

df_mer['containsCrime'] = df_mer['genres'].str.contains("Crime")
df_mer['containsThriller'] = df_mer['genres'].str.contains("Thriller")

df_ct = df_mer[df_mer['containsCrime']&df_mer['containsThriller']]
print("5.범죄 스릴러 최고평점 : ", df_ct[df_ct['rank1']==1]['title'].values)