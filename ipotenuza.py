import math

def ipotenuza(c1, c2):
    ip = math.sqrt(c1 * c1 + c2 * c2)
    return ip
  
if __name__ == '__main__':
    print("ipotenuza = ", ipotenuza(3, 4))
