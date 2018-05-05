import pandas as pd 

cityName = pd.Series(['San Fransisco','San Jose','Sacramento'])
print(cityName)
population = pd.Series([852469,1015785,485199])
print(population)
dataFrame = pd.DataFrame({'cityName':cityName,'population':population})
print(dataFrame)
print(dataFrame['population'].apply(lambda a :a > 130) & dataFrame['cityName'].apply(lambda s: s.startswith('San')))
