import pickle

with open('datas.txt','wb') as f:
    li = ['강아지','고양이','닭']
    dic = {1:'사과',2:'딸기',3:'수박'}
    pickle.dump(li,f)
    pickle.dump(dic,f)

with open('datas.txt','rb') as f:
    li = pickle.load(f)
    dic = pickle.load(f)
    print(li)
    print(dic)