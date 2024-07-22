"""
2. **Classe Instrumento e Subclasses**
    
    - Crie uma classe `Instrumento` com um método `tocar`. Crie subclasses 
    `Violao` e `Piano` que sobrescrevem o método `tocar` com sons específicos.
"""


class Instrumentos:
    def tocar(self):
        raise NotImplementedError("Este método deve ser sobrescrito")


class Violao(Instrumentos):
    def tocar(self):
        return "Bam bam bam"


class Piano(Instrumentos):
    def tocar(self):
        return "Tim Tim Tim"


violao = Violao()
piano = Piano()

print(violao.tocar())
print(piano.tocar())
