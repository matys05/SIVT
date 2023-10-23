
def hledej_mocninu(hl: int,sez: list):
  moc=hl**2
  for i in sez:
    if i==moc:
      return True
  return False
    
