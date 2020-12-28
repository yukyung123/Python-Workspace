
# def man(answer):
#     global height
#     height=answer*answer*22
#     print("키 {}cm남자의 표준 체중은 {}입니다.".format(height))
# man(170)


def std_weight(height,gender):#키는 m단위(실수),성별 "남자"/"여자"
    if gender == "남자":
        return height *height*22
    else:
        return height *height*21

height= 175 #cm
gender="남자"
weight=round(std_weight(height/100,gender),2)#반올림 
print("키 {}cm{}의 표준 체중은 {}입니다.".format(height,gender,weight))