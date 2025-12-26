'''score = 90
if score<80:
  print('true')
else:
  print('false')
#if문에대해서..
#if문은 만일 @@하면 $$한다. 즉 이 조건이 참이면 실행하고 아니라면 중지라는식의 조건이 있다. 예를들어 밑의 예시를 보자
plus = 1+1==2
print(plus)
if plus :
  print('참')
else:
  print('허')'''
#이렇듯 파이썬에서는 데이터형을 알아서 지정해주기 때문에 데이터형을 쓰지않아도 된다.
#우선은 프로그램의 if문 즉 조건을 통해 컴퓨터가 판단을 하기위해서는 boolean데이터형을 잘 알아야한다. 그래서 일차원적으로 비교 연산자가 쓰인다.
#자바나 파이썬이나 연산자의 역할은 비슷하지만 복습차원에서 적자면

#산술연산자 + - * / 차례대로 더하기 빼기 곱하기 나누기이다
#비교연산자 == != > < >= <= 이것은 == 왼쪽 오른쪽이 동일한가  != 왼쪽 오른쪽이 틀린가 < 오른쪽이 왼쪽보다 큰가
# >왼쪽이 오른쪽보다 큰가 >=왼쪽이 오른쪽보다 크거나 같은가 <= 오른쪽이 왼쪽보다 크거나 같은가

#기본 할당 연산자 = 가장 기본이자 많이 쓰이는것이다 왼쪽: 변수명 오른쪽 :넣고싶은값 ex pie = 3.14
#복합 할당 연산자 += 더한 후 대입 ex 2 += 5 -> 2 = 2+5 -= 뺀 후 대입 ex 10 -=3 -> 10 = 10-3
#나머지는 *= 곱한 후 대입 /= 나눈후 대입등이 있다. 이렇게만 하면 이해가 안되니 예시를 만들어보자
'''money=9500
pachinko_dama=4
sando =  money/pachinko_dama
print(sando)#粗品のパチンコ算

wallet=30000 #最初の軍資金
invest=6000 #パチンコの投資金額
wallet-=invest #財布に残った金
jackpot= 10500#いきなり当たって10500発引いた
victory=pachinko_dama*jackpot#計算すると
wallet+=victory #残った金と勝った分を合わせる
print(wallet)''' #すなわち66,000になったぞう！
#상당히 뭐랄까 음...아무튼 복합 할당 연산자에서 더하고 대입과 빼고 대입을 알아보았다.
#계산이나 삶에서 참만 있다면 if를 사용하지 않도되겠지 하지만 현실세계에선 원하는대로 이루어지는 법이란건 없다 그러니
#이게 아니라면? 라는 생각에 else라는 개념을 사용해 참이 아닌 거짓일때의 결과를 나타낼수 있다.

'''human_age = range(1, 101)
me=human_age[28]
entry_limit=human_age[23]
print("나의 나이는",me,'살이다...')
print('회사의 지원은',entry_limit,'살 까지이다.')
if me <=entry_limit:
  print('나에게도 이런 기회가 오다니')
else:
  print('중간에는 눈물을 흘리지만 마지막에는 모두가 웃는다')
  print('그러니 지금은 이 꽉깨물고 힘낼 수 밖에없어')'''

jlpt=range(0,61)
listen=(jlpt[59])
kanji=(jlpt[40])
reading=(jlpt[13])

passing_score_N1=100
passing_score_N1_listen=(jlpt[19])
passing_score_N1_kanji=(jlpt[19])
passing_score_N1_reading=(jlpt[19])
total= listen+kanji+reading
print('총합',total,'점입니다.')
if passing_score_N1<total:
  print('jlpt합격')
else:
  print('불합격')

if passing_score_N1_listen<listen:
  print('청해 점수',listen,'합격')
else:
  print('청해 점수 과락')
if passing_score_N1_kanji<kanji:
  print('한자지식 점수',kanji,'합격')
else:
  print('한자지식 점수 과락')
if passing_score_N1_reading<reading:
  print('독해 점수',reading, '합격')
else:
  print('독해 점수 과락')
if passing_score_N1<total and passing_score_N1_listen<listen and passing_score_N1_kanji<kanji and passing_score_N1_reading<reading:
  print("최종합격")
else:
  print('점수 미달 불합격')

