from django.db import models

# Create your models here.
class Song(models.Model):
    """
    Model representing a piece of music
    """
    title = models.CharField(max_length=512, help_text="Entrez le titre du morceau")

    author = models.CharField(max_length=512, help_text="Entrez l'auteur du morceau")


    def __str__(self):
        """
        String for representing the Song Model object
        """
        return self.title + " (" + self.author + ")"


class Evenement(models.Model):
    """
    Model representing an event : concert, parade, ...
    """
    title = models.CharField(max_length=512, help_text="Entrez le titre de l'événement")

    date = models.DateTimeField(help_text="Date de l'événement")

    place = models.CharField(max_length=512, help_text="Entrez le lieu de l'événement")

    date_arrival = models.TimeField(help_text="Heure d'arrivée des musiciens")
    CLASSIC = 'CL'
    CASUAL = 'CA'
    OUTFIT_CHOICES = (
        (CLASSIC, 'Haut: blanc ; Bas: noir'),
        (CASUAL, 'Décontracté'),
    )
    outfit = models.CharField(
        max_length=2,
        choices=OUTFIT_CHOICES,
        default=CLASSIC,
    )

    songs = models.ManyToManyField(Song)

    def __str__(self):
        """
        String for representing the Evenement Model object
        """
        return self.title

