class PuntoXY:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norma(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return "Punto con x = {} e y = {}".format(self.x, self.y)

#ADAPTER
class PuntoVector:
    def __init__(self, cords):
        self.puntoxy = PuntoXY(cords[0], cords[1])

    def norma(self):
        return self.puntoxy.norma()

    def at(self, pos):
        if pos == 0:
            return self.puntoxy.x
        elif pos == 1:
            return self.puntoxy.y
        else:
            raise BaseException("Out of index")

    def __str__(self):
        return self.puntoxy.__str__()


def productoInterno(vec1, vec2):
  return vec1.at(0) * vec2.at(0) + vec1.at(1)*vec2.at(1)

def ano(v):
    return v.__str__()


puntoC = PuntoVector([1,1])
puntoD = PuntoVector([-1,-1])
print(puntoC)
print(puntoD)
print(productoInterno(puntoC,puntoD))