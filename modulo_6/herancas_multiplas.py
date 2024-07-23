class Ave:
    def voar(self):
        return "Voar"


class Aquatico:
    def nadar(self):
        return "Nadar"


class Pinguin(Ave, Aquatico):
    def __init__(self, nome) -> None:
        self.nome = nome


pingu = Pinguin("Pingu")

print(pingu.voar())
print(pingu.nadar())
