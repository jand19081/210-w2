import random


# Add the class declaration.
class Card:
    """A deck of 13 cards ranging in value from 1-13

    When a card is drawn a value is shown.
   
    Attributes:
        value (int): The value of the card drawn.
    """

# Create the class constructor.
    def __init__(self):
        """Constructs a new instance of Card with a value attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
        

# Create the draw(self) method.
    def draw(self):
        """Generates a new random value.
        
        Args:
            self (Card): An instance of Card.
        """
        # Draw a card
        self.value = random.randint(1,13)
        return self.value