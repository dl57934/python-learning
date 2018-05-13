import math,sys
from konlpy.tag import Twitter

class BayesianFilter:
    def __init__(self):
        self.words = set()
        self.words_dict = {}
        self.category_dict = {}

    def split(self,text):
        result = []
        twitter = Twitter()
        words = twitter.pos(text)
        for word in words:
            if word[1] not in ["Josa","Eomi","Punctuation"]:
                result.append(word[0])
                if word[0] not in words:
                    self.words.add(word[0])
        return result

    def fit(self,text,category):
        self.setCategory(category)
        words = self.split(text)
        self.setWord(words,category)

    def setCategory(self,category):
        if category not in self.category_dict:
            self.category_dict[category] = 0
        else: 
            self.category_dict[category] += 1
    def setWord(self,words,category):
        if category not in self.words_dict:
            self.words_dict[category] = {}
        for word in words:
            if word not in self.words_dict[category]:
                self.words_dict[category][word] = 0
            else:
                self.words_dict[category][word] += 1
    def getCategoryCal(self,category):
        return self.category_dict[category] / sum(self.category_dict.values())

    def getWordCal(self, word, category):
        if word in self.words_dict[category]:
            front = self.words_dict[category][word]
        else:
            front = 0
        return (front+1) / (len(self.words) + sum(self.words_dict[category].values()))

    def predict(self,text):
        score = 0
        returnKey = ""
        words =self.split(text)
        max_data = -sys.maxsize
        for key in self.category_dict.keys():
            score= 0
            score += math.log(self.getCategoryCal(key))
            for word in words:
                score += math.log(self.getWordCal(word,key))
            if max_data < score:
                max_data = score
                returnKey = key
        return returnKey
