#어떤 일을 하는 명령을 모아 놓은 것 = 함수 
#모음으로써 쉽고 사용할 수 있다.
#지금까지 print() range() 등 모두 파이썬 내부에 내장되어있는 함수이다. 그렇다면 직접 함수를 만들어 
#본격적인 나만의 프로그래밍을 작성해보자.
#함수는 '함수명'을 정하고 'def 함수명():' 이라고 지정한 뒤 그 {함수에서 수행할 처리}를 지정하여 만든다. 함수명은 카운터 변수명이나 다른 변수명처럼 아무렇게나 자유롭게 작성해도 되지만
#최대한 내가 알아보고 쉽고 다른이들도 알아보기 쉽게 작성해야한다.
#{함수에서 수행할 처리}는 하나로 묶은 처리이므로 if문,for문과 똑같이 '블록'으로 만든다.그러니 들여쓰기로 작성한다.

#가장 대표적인 인사의 함수를 작성해보자
def say_hello():
  print('hello world')

say_hello()

def hello(name):
  print(f'{name} 안녕 좋은아침!')
hello('강태성')
def posttaxprice(price):
  ans=price*1.1
  return ans

print(posttaxprice(1000),'원')
print(posttaxprice(1280),'원')


def hello(name):
    print(f'{name} 안녕 좋은아침!')

result = hello('강태성')
print(result)          # 뭐가 출력될까?