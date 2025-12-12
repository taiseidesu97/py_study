#리스트의 값을 가져오거나,변경 그리고 추가 삭제를 활용하여 개념을 통집합한 예제를 작성해보자.
candies = ['초코','바나나','홍삼','누룽지','박하']
print(candies)
del candies[4]
candies.append('민트')
candies.insert(1,'복숭아')
candies[0]= '바닐라'
del candies[2:4]
print(candies)
print(candies[0])
print(candies[0:3])

week = ['월','화','수','목','금','토','일']
print(week)

print(week[0:5])#평일
print(week[5:7])#주말

#리스트를 활용하여 간단한 일기를 작성해보자
workday=week[0:5]
weekend=week[5:7]
print('나는 학원에',workday,'요일에 간다')
print('나는',weekend,'날 쉰다' )
print('나는 예전에',week[0],week[2],week[4],'에 일하는 요일 알바를 했고')
del week[1],week[3]

print('예전에 서비스 업을 할때는',week,'날 일했다.')
holiday='주말'
hardday='평일인', week[0:5]
print('역시 서비스업은',holiday,'에 쉴수 없다..')
print('일본에서는',hardday,'이날 중 하루만 쉬어야 했다.')