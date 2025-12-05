print("끝말잇기 게임 시작!\n")
d = input("글자를 입력해 주세요\n>>>")
used = []
used.append(d)
d = list(d)
last_word = d[len(d) - 1]
time = 3
h = False
while time > 0:
  h = False
  d = input("\n글자를 입력해 주세요\n>>>")
  for i in range(len(used)):
    if used[i] == d:
      time -= 1
      print(f"이미 사용한 글자입니다.\n남은 횟수 : {time}\n")
      h = True
      continue
  if h:
    continue
  else:
    used.append(d)
    d = list(d)
    if d[0] != last_word:
      time -= 1
      print(f"끝말이 같지 않습니다.\n남은 횟수 : {time}\n")
    elif len(d) < 2:
      print("최소 두글자 이상을 입력해주세요.\n")
    else:
      last_word = d[len(d) - 1]
      time = 3
print("횟수 초과!")
