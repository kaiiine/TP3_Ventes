print("Bonjour, je suis vendeur d'ordinateur porable et voici notre tout nouveau pc ultraperformant, il coute cependant 26000$, avez-vous assez ?")

wallet = int(input("Quelle somme possedez-vous ?"))
if wallet >= 2600:
    answer_1 = input("Vous avez visiblement assez, voulez-vous l'acheter ?")
    if answer_1 == "oui" :
        answer_2 = input("Souhaitez-vous regler par carte ou espece ?")
        if answer_2 == "carte":
            print("*Bip Bip*")
            print("paiment accepte")
            print("retirez votre carte")
            print("Tenez, je vous ai mis un essai gratuit Deezer pendant 3mois. Bonne journee !")
            wallet = wallet - 2600
            print("Merci beaucoup, Au revoir !!")
        if answer_2 == "espece":
            print("*Gling Gling*")
            print("Tenez, je vous ai mis un essai gratuit Deezer pendant 3mois. Bonne journee !")
            print("Merci beaucoup. Au revoir !")
            wallet = wallet - 2600
    if answer_1 == "non":
        print("Dommage vous passez devant une belle occasion")
        print("A une prochaine fois je l'espere")
else:
    answer_3 = input("Vous n'avez pas assez, je peux sinon vous proposer un autre pc moins performant coutant seulement 700$. Seriez-vous interesse(e)")
    if answer_3 == "oui":
        if wallet >= 700:
            answer_3 = input("Souhaitez-vous regler par carte ou espece ?")
            if answer_3 == "carte":
                print("*Bip Bip*")
                print("paiment accepte")
                print("retirez votre carte")
                print("Tenez, je vous ai mis un essai gratuit Deezer pendant 3mois. Bonne journee !")
                wallet = wallet - 700
                print("Merci beaucoup, Au revoir !!")
            if answer_3 == "espèce":
                print("*Gling Gling*")
                print("Tenez, je vous ai mis un essai gratuit Deezer pendant 3mois. Bonne journee !")
                print("Merci beaucoup. Au revoir !")
                wallet = wallet - 700
        else:
            answer_4 = input("VOUS M'AVEZ MENTIS VOUS N'AVEZ PAS ASSEZ !!! SORTEZ DE MON MAGASIN AVANT QUE CELA NE DEGENERE !!!")
            if answer_4 == "non":
                print("D'ACCORD, J'APPELLE IMMEDIATEMENT LA SECURITE")
                print("SECURITE !!!!")
                print("*Vous etes entoure(e) par 3 personnes de la securite*")
                answer_5 = "Que souhaitez-vous faire ? "
                print(answer_5)
                print("Parler de facon diplomatique")
                print("fuir")
                print("se battre")
                answer_5 = input("Que faites-vous ?")
                if answer_5 == "se battre":
                    print("*Le premier s'approche de vous et vous colle une droie en plein front")
                    answer_6 = "Que souhaitez-vous faire ?"
                    print(answer_6)
                    print("esquiver")
                    print("bloquer")
                    print("encaisser le coup")
                    answer_6 = input("Que faites-vous ?")
                    if answer_6 == "encaisser le coup":
                        print("*Calmos amigos, vous n'etes pas Dwayne Johnson. La patate que vous vous etes pris vous a assome d'un coup. Vous Vous etes retrouve a� l'hopital avec votre portefeuille*")
                        print("Vous ouvrez votre portefeuille")
                        wallet = 0
                        print("Vous reperdez conscience...")
                    if answer_6 == "bloquer":
                        print("*La puissance du coup vous propulse en arriere et vous fait perdre conscience*")
                        print("Vous venez de vous reveiller. que voulez vous faire ?")
                        print("Vous reperdez connaissance")
                        wallet = 0
                    if answer_6 == "esquiver":
                        print("*Waow incroyable, vous esquivez le coup avec une telle agilite*")
                    
        if answer_3 == "non":
            print("Dommage vous passez devant une belle occasion")
            print("A une prochaine fois je l'espere")
            print("*Vous partez tout(e) triste*")
    print("Il vous reste {}$".format(wallet))
       