from google_images_download import google_images_download   #importing the library
import re

regex = "\(.+\)|\s-\s.+"
response = google_images_download.googleimagesdownload()   #class instantiation

f = open("40names.txt", "r", encoding='UTF-8')
read = f.read()
splitname = read.split('\n')
# print(splitname)

SGL = ['유재석', '이광수', '하하 가수', '지석진', '송지효', '강호동', '전소민', '양서찬', '정준하', '박명수', '박나래', '전현무',
         '노홍철', '송은이', '소녀시대 티파니', '마마무 화사', '장도연', '마마무 솔라', '김준현', '이경규', '데프콘', '김태희', '전지현', '송강호',
         '광희', '소녀시대 써니', '박혜미', '이순재', '신동엽', '주현영', '안영미', '엄정화', '박미선', '조혜련', '수지 가수', '지드레곤',
         '양세형', '이승기', '김소연', '엄기준', '조수민', '강동원', '원빈', '장동건', '안정환', '서장훈', '현영', '오지헌', '소녀시대 태연',
         '정종철', '박준형', '이수민', '이수근', '탁재훈', '김종국', '전소미', '강하나', '오나미', '김지민', '김준호', '한지민', '소녀시대 윤아',
         '박민영', '구준엽', '김현중', '김우빈', '정우성', '황정민', '박수진', '이지아', '아이린', '장원영', '제시', '이이경',
         '손나은', '노사연', '이무송', '한채영', '최수종', '장나라', '문근영', '박보영', '신세경', '황정음', '윤시윤', '최지우',
         '고두심', '윤여정', '하지원', '강하늘', '김혜수', '진지희', '송혜교', '박보검', '차은우', '김희선', '현빈', '손예진', '베성재', '이민호']

targetname = splitname 

keyword_40 = ""
for onename in targetname:
    thename = re.sub(regex, '', onename)
    print(onename,'==>',thename)
    keyword_40 = keyword_40 + "," +thename

print(keyword_40[1:])

arguments = {"keywords":keyword_40[1:],"limit":40,"print_urls":True, "format": "jpg"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images