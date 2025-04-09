class Voiture:
    # Constructeur des attributs
    def __init__(self, name):
        self.name = name

    def start(self):
        print("Le véhicule a démarré")

# ma_voiture est une instance de la classe Voiture (objet)
ma_voiture = Voiture("Voiture 1") # on initialise ma_voiture
ma_voiture.start() # on va chercher la méthode 'start' de l'objet ma_voiture