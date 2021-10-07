with open("/tmp/coderdojo-logo.png", "rb") as image:
  f = image.read()
  b = bytearray(f)
  print(b[0])
