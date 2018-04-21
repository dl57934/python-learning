import request
from bs4 import BeautifulSoup as bs

session = requests.session()
loginUrl = "https://nid.naver.com/nidlogin.login"
mailUrl = "https://mail.naver.com/?n=1523348535481&v=f"
inputData = { 
    "enctp":"1",
    "encpw":"4e2cddb992c8f275689979e3303401aeb7ef829ad90ed6f5a0c71a7d0022531101cb2bc619dd89285f1bc2895189a4980a98e326ce9fb6fbbc40e2fb7da690eed7fa3883084b51a80b9b244a30149572c44070d60450fd66c160f31bc484bc7922dfd05975eafaf11043b12f89e8b9dcd32fdaec3b35fc549b3c77ad2aa8a5e5",
    "encnm":"100013097",
    "locale":"ko_KR",
    "id":"dl57934",
    "pw":"dltkdgns"
}
header = {
"cache-control":"max-age=0",
"charset":"utf-8",
"accept":"*/*",
"accept-encoding":"gzip,deflate,br",
"accept-language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
"origin":"https://nid.naver.com",
"referer":"https://nid.naver.com/nidlogin.login",
"upgrade-insecure-requests": "1",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
"cookie":"npic=PQ/XaWMst9AMYkrwJa7yUse5101vF3dnB5VSw7fACwo5m+KP0Prx22OL21sXiWIDCA==; NNB=4K5JCFIV43VVO; nid_buk=4K5JCFIV43VVO; ZDdkNTg4MTItY2RmNi00OTcwLWI3ZDctNTY0ZjU1ZWQwYzI0_iKcfj4Ww=true; _ga=GA1.2.592292526.1500982016; ASID=70a5115b0000015a72f2b1030000004a; NFS=1; nid_enctp=1; nsr_acl=1; nid_slevel=1; nid_sec=LMClMhfaQRZ8BGaP1gB5DU2mtMJh7k7nhf8HffnoVR9qyW3khj1SgeYjuJc432To; nx_ssl=2; nid_iplevel=1; page_uid=TVxoQdpVuEossuIndPhssssssoN-150815; nid_inf=336028950; NID_AUT=eBpjC7lyBUSlmb/sbkCRDmqo3pvaaQxuoIT8XoR6O5aXl1tHsMGA4OEssWtoCpSC; NID_JKL=fRhrWHGUVEPmiaJ290eX3LHLOvrRY+MIa52D266kBHg=; NID_SES=AAABvnV9smIfQPM7dZFK3ceprWDGbSm35HzPSbpr4QgxQSxbiY3AYvNitcTEXjQw0Z3OZ+9SBwiskblOzBfUjS1PDbXjKGytdgm2UKioEdrMukgUm7tKHZethpAj26U1afRbwdhUI4KcHKYaenyND2bkZKfjrHFNk0a26AZM6R+8KpTJUbt/1zZf2U9oK2nIBDnvbZeOUQx1GbEy/uaqje1AOy6jXgOxYb8LqHI/pDUdlqPDWoc78ykHJW155yjoblQI1DLEJX7nD1+/4XlYXbYIp2McgTxxBge3FI4+0tY5YnVjRumcOqILuhWff0SmS8tKkG4oR8T33pTm8GcY5ErS2lBXU5It2BguWVLICpOAWz4pjjyVK6IwC3spA3n9Ht16gr3JBBTnatiysxROcXEmcfdlqEDqbI01GoEypPoMniE52OsgmHJZVGkgodeqylIPs0mxpBcfyM+0DzZQTRN06Yp/0/eBziHc1ZY3QPgBdf8B0bJ1ne8sb7TYv4H2xSmVpyI6NvinBxbYEwzhtgUp/420CqBjIRBmN8+C5V/OlEptbpHoN3hPtQS0kppl0DWsovBIC2JBxhkfSg/HToDdu6w="
}
res = session.post(loginUrl,data = inputData)
res = session.get(mailUrl,headers = header)
soup = bs(res.text,"html.parser")
result = soup.select_one("em._c1(mfCore|clickFolder|0|unread)_m1(mfCore|stopDrag)_m2(mfCore|stopDrag)_stopDefault")
print(res.text)
 
