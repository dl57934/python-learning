import codecs 
from konlpy.tag import Twitter
from gensim.models import word2vec 
from bs4 import BeautifulSoup
fp = codecs.open('toji.txt','r',encoding = 'utf-16')
bsData = BeautifulSoup(fp,'html.parser')
text = bsData.select_one('body > text')
lines = text.getText()
lines = lines.split('\n')
twitter = Twitter()
result = []
for line in lines:
    r = []
    words = twitter.pos(line,norm = True)
    for word in words:
        if word[1] not in ['Eomi', 'Josa', 'Punctuation']:
            r.append(word[0])
    result.append(" ".join(r))

wakatiFile = "toji2.wakati"

with open(wakatiFile,'w',encoding='utf-8') as fp:
    fp.write('\n'.join(result))

lines = word2vec.LineSentence(wakatiFile)
model = word2vec.Word2Vec(lines ,size=200 ,window = 10,
        hs=1,min_count=2,sg=1)

model.save("toji2.model")



