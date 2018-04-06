from urllib import request

savename = "test2.png"
url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRj7_Z5lTiu7QE5Rt_Kz7WqOlNtNARAOHxwzc9htl8crpZPqN7a"

mem = request.urlopen(url).read()
with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다.")