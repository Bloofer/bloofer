fil = open("/home/jmyang/www/blooferblog/static/reviews/post1.md", "r")
nfil = []
for line in fil:
  nfil.append(line)
  if len(nfil) == 3: break

for n in nfil:
  print n
