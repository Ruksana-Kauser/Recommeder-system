from tkinter.messagebox import YES
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer #gives vector values converting word to numbers
from sklearn.metrics.pairwise import linear_kernel #distance calculation

data = pd.read_csv('anime_new')
data.genre.fillna(" ",inplace=True) #filling null values with space

tfid = TfidfVectorizer(stop_words='english')
vector = tfid.fit_transform(data.genre)

index = pd.Series(data=data.index,index=data.name)

# def recommender(name,n):
#     ind_name = index[name]
#     val_name = list(enumerate(dist[ind_name]))
#     val_name = sorted(val_name,key=lambda x:x[1],reverse=True)
#     l=[]
#     for i in range(1,n):
#         l.append(data.name.loc[val_name[i][0]])
#     return l 

def recommender(name):
    ind_name = index[name]
    dis = linear_kernel(vector[ind_name],vector)
    val_name = list((dis))
    d = pd.DataFrame(val_name)
    d = d.transpose()
    d.columns = ["name"]
    d =d.sort_values(by="name",ascending = False) 
    l = []
    for i in range(0,10):
        l.append(data.name.loc[d.index[i]]) 
    return l

def genre_recommender(name,n):
    ind_name = index[name]
    dis = linear_kernel(vector[ind_name],vector)
    val_name = list((dis))
    d = pd.DataFrame(val_name)
    d = d.transpose()
    d.columns = ["name"]
    d =d.sort_values(by="name",ascending = False) 
    l = []
    for i in range(0,10):
        l.append(data.genre.loc[d.index[i]]) 
    return l  

def rating_recommender(name,n):
    ind_name = index[name]
    dis = linear_kernel(vector[ind_name],vector)
    val_name = list((dis))
    d = pd.DataFrame(val_name)
    d = d.transpose()
    d.columns = ["name"]
    d =d.sort_values(by="name",ascending = False) 
    l = []
    for i in range(0,10):
        l.append(data.rating.loc[d.index[i]]) 
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