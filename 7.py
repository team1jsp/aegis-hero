chisla = [1111, 22, 890, 2132, 8777, 1]
chet = []
nechet = []
q = len(chisla)
for i in range(q):
  qwe = chisla[i]
  if qwe % 2 == 0:
    chet.append(qwe)
  elif qwe % 2 == 1:
    nechet.append(qwe)
print(chet)
print(nechet)
