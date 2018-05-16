
from konlpy.tag import Twitter

twitter = Twitter()
print("구분할 문장을 입력해주세요")
text = input()
#norm은 현대적인말 그래욬ㅋㅋㅋ 같은 것을 그래요로 바꾸어 주는 것이다. 
#stem은 그래요를 그렇다처럼 원형으로 바꾸어 주는 것이다.
classifiedData = twitter.pos(text,norm=True,stem=True)
print(classifiedData)
