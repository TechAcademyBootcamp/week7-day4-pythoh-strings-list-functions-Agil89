color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]


s = set(color1)
s1 = set(color2)

s3 = s-s1
# print(s-(s-s1))
print(list(s&s1))