from bs4 import BeautifulSoup

html = """
<html>
<body>
<div>
    <h1 id="title">후니의 컴퓨터</h1>
    <ul class ="item">
        <li>node.js</li>
        <li>python</li>
        <li>dataStructure</li>
    </ul>
</div>
</body>
</html>"""

soup = BeautifulSoup(html,'html.parser')

h1 = soup.select_one("div > h1#title").string
li_list = soup.select("div > ul.item > li")
p = soup.find(id="title")
print(h1)
print(p)
for li in li_list:
    print(li.string)
