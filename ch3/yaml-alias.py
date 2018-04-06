import yaml 

yaml_str = """
color_def:
    - &color1 "#FF0000"
    - &color2 "#00FF00"
    - &color3 "#0000FF"

color: 
    title: *color1
    name: *color2
    link: *color3
"""
data2 = yaml.dump(yaml_str)
data = yaml.load(yaml_str)
print(data2)
print("title", data["color"]["title"], "name",data["color"]["name"],"link",data["color"]["link"])
