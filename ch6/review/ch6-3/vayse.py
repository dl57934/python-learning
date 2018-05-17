import os, sys, math 
from konlpy.tag import Twitter

class BayesFilter:
    def __init__(self):
        self.words = set()
        self.word_dic = {}
        self.category_dic = {}

    def fit(self, text, category):
        self.incWord(text,category)
        self.incCategory(category)

    def incWord(self, text,category):
        twitter = Twitter()
        malist = twitter.pos(text,norm=True)
        if category not in self.word_dic:
            self.word_dic[category] = {}
        for word in malist:
            if word[1] not in ["Josa","Eomi","Punctuation"]:
                if word not in self.word_dic[category]:
                    self.word_dic[category][word[0]] = 0
                self.word_dic[category][word[0]]+=1
                self.words.add(word[0])
    def incCategory(self,category):
        if category not in self.category_dic:
            self.category_dic[category] = 0
        self.category_dic[category]+=1
    def word_prob(self, word,category):
        if word not in self.word_dic[category]:
            n = 0
        else:
            n = self.word_dic[category][word]
        return math.log(n+1 / (len(self.words)+sum(self.word_dic[category].values())))
    def category_prob(self, category):
        return math.log(self.category_dic[category] /sum(self.category_dic.values()))

    def predict(self, text):
        maxScore = -sys.maxsize
        for category in self.category_dic.keys():
            score = 0
            categoryScore = self.category_prob(category)
            score += categoryScore
            twitter = Twitter()
            malist = twitter.pos(text,norm = True)
            for word in malist:
                score += self.word_prob(word[0], category)
            if maxScore < score:
                bestCategory = category
                maxScore = score 
        return bestCategory
                

