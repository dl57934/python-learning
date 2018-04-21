from urllib import request

url = "http://cfs4.tistory.com/upload_control/download.blog?fhandle=YmxvZzEyNDM3NEBmczQudGlzdG9yeS5jb206L2F0dGFjaC8wLzA5MDAwMDAwMDAwMC5qcGc%3D"
savename = "test.png"

request.urlretrieve(url,savename)
print("저장되었습니다.")