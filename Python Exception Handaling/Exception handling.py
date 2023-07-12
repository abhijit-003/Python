try:
  x,y=100,2
  z=x/2
  if z > 10:
    raise ValueError(z)
except ValueError:
  print(z, "is out of allowed range")
else:
  print(z, "is within the allowed range")
