# JLPT N1 채점 기준 시뮬레이션 (내 실제 점수로)

# 점수 범위 (각 영역 0~60점)
score_range = range(0, 61)

# 내 실제 점수
listen = score_range[59]   # 청해: 59점
kanji = score_range[40]    # 언어지식(한자/어휘/문법): 40점
reading = score_range[23]  # 독해: 23점

# N1 합격 기준
PASSING_TOTAL = 100                  # 전체 100점 이상
PASSING_SECTION = 19                 # 각 영역 19점 이상 (과락 기준)

# 총점 계산
total = listen + kanji + reading

# 결과 출력
print(f"=== JLPT N1 점수 결과 ===")
print(f"청해(聴解): {listen}점")
print(f"언어지식(漢字/語彙/文法): {kanji}점")
print(f"독해(読解): {reading}점")
print(f"총점: {total}/180점")
print()

# 전체 합격 판단
if total >= PASSING_TOTAL and listen >= PASSING_SECTION and kanji >= PASSING_SECTION and reading >= PASSING_SECTION:
    print("🎉 JLPT N1 합격입니다!! 🎉")
    print("정말 고생 많았어요. 이 노력은 절대 헛되지 않아요!")
else:
    print("📌 불합격입니다...")
    if total < PASSING_TOTAL:
        print(f"   - 총점이 {total}점으로 기준({PASSING_TOTAL}점)에 미달했습니다.")
    
    # 각 영역 과락 체크
if listen < PASSING_SECTION:
    print(f"   - 청해 과락 ({listen}점 < {PASSING_SECTION}점)")
else:
    print('청해 패스!')
if kanji < PASSING_SECTION:
  print(f"   - 언어지식 과락 ({kanji}점 < {PASSING_SECTION}점)")
else:
    print('언어지식 패스!')
if reading < PASSING_SECTION:
  print(f"   - 독해 과락 ({reading}점 < {PASSING_SECTION}점)")
else:
  print('독해 패스!')
#print("그래도 포기하지 마세요. 다음엔 더 잘할 수 있어요 💪")