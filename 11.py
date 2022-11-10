q = int(input("Первая сторона: "))
w = int(input("Вторая сторона: "))
e = int(input("Третья сторона: "))
qw = q + w
qe = q + e
we = w + e
if qw > e and qe > w and we > q:
  print( "есть такой) ")
else:
  print( "нету такова( ")