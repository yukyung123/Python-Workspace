score_file = open('score.txt','r',encoding='utf8')
print(score_file.readline(),end="")#줄별로 읽기, 한줄 일고 커서 다음 줄로 이동 
print(score_file.readline())
print(score_file.readline())
print(score_file.readline()) 
score_file.close()

#몇줄인지 모를 때
score_file = open('score.txt','r',encoding='utf8')
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close

#list에 값을 넣어 처리 
score_file = open('score.txt','r',encoding='utf8')
lines = score_file.readlines() #list 형태로 저장 
for line in lines:
    print(line,end="")
score_file.close()
