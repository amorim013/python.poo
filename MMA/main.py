from lutadores import *

if __name__ == "__main__":

    popo = Boxeador('Popo')
    bambam = Boxeador('Bambam')
    popo.soco(bambam)
    print(popo)
    print(bambam)
    popo.gancho(bambam)
    print(popo)
    print(bambam)

    gracie = Jujitsu('Roler Gracie')
    gracie.soco(popo)
    gracie.chave_braco(popo)
    print(gracie)
    print(popo)

    charles = MMA('Charles do Bronx')
    charles.chute_alto(gracie)
    charles.superman_punch(gracie)
    print(charles)
    print(gracie)

    tailandes = Muay_Thai('Tailandes Maluco')
    tailandes.chute_alto(charles)
    charles.chave_braco(tailandes)
    print(charles)
    print(tailandes)