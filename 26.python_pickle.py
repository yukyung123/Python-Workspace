##프로그램 상에서 데이터를 파일 형태로 저장
import pickle
profile_file = open("profile.pickle","wb")#W쓰기,B바이너리 타입
profile={"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile,profile_file)#profile에 있는 정보를 file에 저장
profile_file.close()


profile_file = open("profile.pickle","rb")#r 읽기
profile = pickle.load(profile_file)#file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close() 
