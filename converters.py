def decToHex(dec):
  return hex(int(dec)).split('x')[1].upper()

def decToBin(dec):
  return bin(int(dec)).split('b')[1]

def binToDec(bin):
  return int(bin, 2)

def binToHex(bin):
  return decToHex(int(bin, 2))

def hexToDec(hex):
  return int(hex, 16)

def hexToBin(hex):
  return decToBin(int(hex, 16))