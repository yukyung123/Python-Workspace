score_file = open('score.txt','w',encoding='utf8')
#w= write 쓰기,encoding='utf8'한국어
print('수학:0',file=score_file)
print('영어 :50',file=score_file)
score_file.close()

score_file = open('score.txt','a',encoding='utf8')
#a=append불러오기
score_file.write("과학:80")
score_file.write("\n코딩:100")
score_file.close()

score_file = open('score.txt','r',encoding='utf8')
#r=read 읽기
print(score_file.read())
score_file.close
