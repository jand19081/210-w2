from game.card import Card

card = Card()

class Dealer:
    """A person who deals the cards. 
    
    The responsibility of the Dealer is to control the sequence of play.

    Attributes:
        guess (str): The user's guess of higher or lower.
        next_card: value of the next card drawn.
        current_card: value of the current card drawn.
        is_playing (str): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Dealer.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.guess = ""
        self.current_card = card.draw()
        self.next_card = card.draw()
        self.is_playing = "y"
        self.score = 0
        self.total_score = 300



    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        while self.is_playing == "y":
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        

    def get_inputs(self):
        """Ask the user if they think the next card will be higher or lower.

        Args:
            self (Dealer): An instance of Dealer.
        """

        print(f"The card is: {self.current_card}")
        self.guess = input("Higher or lower? [h/l] ").lower()
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Dealer): An instance of Dealer.
        """
        if self.is_playing == "n":
            return
 

        # Check the user's guess.

        # Guess high
        if self.guess == "h":
            if self.next_card > self.current_card:
                self.score = 100
            else: 
                self.score = -75
        # Guess low
        elif self.guess == "l":
            if self.next_card < self.current_card:
                self.score = 100
            else:
                self.score = -75
        
        # Add score to total score
        self.total_score += self.score

        # Reset score
        self.score = 0

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to play again. 

        Args:
            self (Dealer): An instance of Dealer.
        """
        if self.is_playing == "n":
            return
        
        print(f"The next card was: {self.next_card}")
        print(f"Your score is: {self.total_score}")

        if self.total_score > 0:
            # See if user wants to play again
            self.is_playing = input("Play again? [y/n]")
            print()
        else:
            self.is_playing = "n"

        # Set new card values
        self.current_card = card.draw()
        self.next_card = card.draw()