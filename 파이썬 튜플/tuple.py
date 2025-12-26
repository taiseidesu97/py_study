#튜플은 리스트의 읽기 전용 버젼이라 표현하면 편하다.
#튜플의 가장 큰 특징은 처음 정의를 할때를 제외하면 추가,삭제,변경이 안된다는 점이다.
#그럼으로 값의 순서도 바뀔 수 없다.
#작성법은 튜플명=(값1,값2) 이와 같이 리스트는 대괄호[] 딕셔너리는{} 튜플은() 이런식으로 구분짓는다.
#예를 작성해보자
profile=("강태성",29,"취준생")
print(profile)
#튜플은 인덱스로 확인이 가능하다. 
print(profile[1]) #0번째는 이름 1번째는 나이 2번째는 직업
#다수의 변수로 설정하는것도 가능하다.
(name, age, hooby)="강태성",29,"게임"
print(name,age)
#다만 이런것이 가능하다
morning=('토스트','맥모닝','소고기무국')
lunch=('짜장면','냉면','백반','햄버거')
dinner=('양꼬치','스테이크','아구찜')
meal=morning,lunch,dinner
print(meal)
front=(f'html,javascript,react,css')
back=(f'java,python,ruby,docker,mysql,database')
fullstack=front,back
print(fullstack)
#이렇듯 튜플은 인덱스의 순서변경을 못하지만 튜플을 여러개 작성한 후 작성한 튜플을 하나의 튜플로 합칠 수 있는데 
# 이때 합쳐질때의 튜플의 순서에 따라 합쳐진 인덱스의 순서가 바뀌게 된다
#