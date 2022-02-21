from tkinter.messagebox import YES
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer #gives vector values converting word to numbers
from sklearn.metrics.pairwise import linear_kernel #distance calculation

data = pd.read_csv('anime_new')
data.genre.fillna(" ",inplace=True) #filling null values with space

initialize = TfidfVectorizer(stop_words='english')
var = initialize.fit_transform(data.genre)
dist = linear_kernel(var,var) #finding correlation distance
index = pd.Series(data=data.index,index=data.name)

def recommender(name,n):
    ind_name = index[name]
    val_name = list(enumerate(dist[ind_name]))
    val_name = sorted(val_name,key=lambda x:x[1],reverse=True)
    l=[]
    for i in range(1,n):
        l.append(data.name.loc[val_name[i][0]])
    return l 

def genre_recommender(name,n):
    ind_name = index[name]
    val_name = list(enumerate(dist[ind_name]))
    val_name = sorted(val_name,key=lambda x:x[1],reverse=True)
    l=[]
    for i in range(1,n):
        l.append(data.genre.loc[val_name[i][0]])
    return l  

def rating_recommender(name,n):
    ind_name = index[name]
    val_name = list(enumerate(dist[ind_name]))
    val_name = sorted(val_name,key=lambda x:x[1],reverse=True)
    l=[]
    for i in range(1,n):
        l.append(data.rating.loc[val_name[i][0]])
    return l    

def checker(name):
    if name in index:
        return ['a','b','c','d','e']
    else:
        return ['x','y']     

def list_name():
    return data.name

def list_genre():
    return data.genre

def list_rating():
    return data.rating
 



    
#recommender("Death Note",20)