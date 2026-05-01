

class Foo:
    def __init__(self):
        self.public = 'isso e publico'
        self._protected = 'isso é protegido'

    def metodoPublico(self):
        self._medoto_protegido()
        return 'metodo publico'
    
    def _medoto_protegido(self):
        print('_medoto protegido')
        return '_medoto_protegido'
    

f = Foo()

#print(f._protected)
print(f.metodoPublico())