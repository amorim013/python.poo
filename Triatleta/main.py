from atleta import *

if __name__ == "__main__":
    avancini = Ciclista("Henrique Avancini", 35, 67.0)
    print(avancini)
    print(avancini.aquecer())
    print(avancini.pedalar())

    bolt = Corredor("Usain Bolt", 38, 86.0)
    print(bolt)
    print(bolt.aquecer())
    print(bolt.correr())

    phelps = Nadador("Michael Phelphs", 39, 88.0)
    print(phelps)
    print(phelps.aquecer())
    print(phelps.nadar())

    avancini = Ciclista("Henrique Avancini", 35, 67.0)
    print(avancini)
    print(avancini.aquecer())
    print(avancini.pedalar())

    keller = Triatleta("Fernanda Keller", 61, 56.0)
    print(keller)
    print(keller.aquecer())
    print(keller.realizar_maratona())



