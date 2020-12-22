#튜플: 리스트와 달리 내용변경,추가 불가능 but 속도가 빠르다

menu = ("돈까스","치즈까스")
print(menu[0])

#menu.add("생선까스")#불가능

#기존
name ="김종국"
age =20 
hobby="코딩"
print(name,age,hobby)
 
#tuple
(name,age,hobby)= ("김종국",20,"코딩")
print(name,age,hobby)