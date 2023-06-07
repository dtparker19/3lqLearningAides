from django.db import models
from django.contrib.auth.models import User


# FlashCard Model
class FlashCard(models.Model):
	category = models.CharField(max_length=50)
	front = models.TextField()
	back = models.TextField()
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.IntegerField(default=0)
	known = models.IntegerField(default=0)

	def __str__(self):
		return self.front


class Decks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deck_name = models.CharField(max_length=200)
    flashcards = models.ManyToManyField(FlashCard, related_name="DeckFlashcards")
    def __str__(self):
        return self.deck_name
    
    
class UserFlashcards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flashcard = models.ForeignKey(FlashCard, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username + " - " + self.flashcard.title
 