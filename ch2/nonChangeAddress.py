from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *

base = "http://example.com/"

print(urljoin(base,'./hoony'))
print(urljoin(base,'./a/b.png'))
print(urljoin(base,"http://example2.com"))
print(urljoin(base,"//example3.com"))
