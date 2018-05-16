from gensim.models import word2vec 

getModel = word2vec.Word2Vec.load("toji2.model")

things = getModel.most_similar(positive=["집"])
print(things)
