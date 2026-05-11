f = open("nevek.txt")
i = 1
for sor in f:
  print(f"{i}. --> {sor.strip()}")
  i += 1
