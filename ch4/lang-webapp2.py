from sklearn.externals import joblib
import cgi, os.path

loc = './root/cgi-bin/freq.pkl'
clf = joblib.load(loc)

def showhtml(text,msg=""):
    print('Content-Type:text/html;charset=euc_kr')
    print("")
    print("""<body><h1>언어 판별기</h1>
                <textarea name="text">{0}</textarea>
                <p><input type="submit" value="판정"><p>
                <p>{1}</p>
                """.format(cgi.escape(text),msg))

def distinct(text):
    text = text.lower()
    orda,ordz = (ord('a'),ord('z'))
    lang = [0 for n in range(26)]
    for ch in text:
        ordch = ord(ch)
        if orda <= ordch <= ordz:
            lang[ordch-orda] += 1
    totla = sum(lang)
    freq = list(map(lambda a :a/total,lang)
    pre = clf.predict([freq])
    lang = {'en':'영어','fr':'프랑스어','id':'인도네시아어','tl':'타갈로그어'}
    return lang[pre[0]]

form = cgi.FieldStorage()
text = form.getvalue("text",default = "")
if text != "":
    resultData = distinct(text)
    msg = '결과는 '+resultData
showhtml(text,msg)
            
