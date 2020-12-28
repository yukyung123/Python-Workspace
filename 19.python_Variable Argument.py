# def profile(name, age, lang1,lang2,lang3,lang4,lang5):
#     print("이름:{}\t 나이 : {}\t".format(name, age),end=" ")
#     #and=" " 그다음 print 문장이 넘어가지않고 " "로됨 
#     print(lang1,lang2,lang3,lang4,lang5)
    
 #5개의 언어 말고 만약 언어를 더 추가하고싶다면 
def profile(name, age, *lang):  #*lang :가변인자
    print("이름:{}\t 나이 : {}\t".format(name,age), end=" ") 
    for lang in lang:
        print(lang,end=" ")
    print()

profile("유재석",20, "python","java","c","c++","c#","javascript")
profile("김태호",25,"kotlin","swift" )
