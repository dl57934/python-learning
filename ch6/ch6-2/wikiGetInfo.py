from gensim.model import word2vec

model = word2vec.Word2Vec.load('wiki.model')

= print("관계있는것을 쳐주세요") 
model = word2vec.Word2vec.most_similar(p
