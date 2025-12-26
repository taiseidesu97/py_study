'''def hello(name):
    message = name, '안녕 좋은아침!'
    return message        # 문자열을 돌려줌

result = hello('강태성')
print(result)'''
'''def hello(name):
    message = f'{name} 안녕 좋은아침!'
    print(message)      # 화면에 바로 보여주고
    return message      # 값도 돌려주고

result = hello('강태성')
print("다시 출력:", result)'''
def posttaxprice(price):
  print(price)
  ans=price*1.1
  
  print(f"세후 가격 계산 완료: {ans}원")
  return ans

print(posttaxprice(1000),'원')
print(posttaxprice(1280),'원')