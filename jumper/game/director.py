from game.jumper import jumper
from game.word_bank import Word_bank

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.jumper = jumper()
        self.word_bank = Word_bank()
        self.guessed_letters = []
        self.is_playing = True
        self.word_bank.choose_word()
        self.word = list(self.word_bank.get_word())

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.do_updates()
            self.do_outputs()
            self.get_inputs()
        exit()

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        word_display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                word_display += letter + " "
            else:
                word_display += "_ "

        print(word_display)
        if self.jumper.if_dead():
            self.is_playing = False
        
        print(self.jumper)
        print("^^^^^^^^^")
        print()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        try:
            guess = input("Guess a letter [a-z]: ")[0]
            letter_ascii = ord(guess.lower()) # Converts char string to ascii
                
            if 97 <= letter_ascii <= 122: #[97-122] Lowercase Alphabet
                if guess not in self.guessed_letters:
                    self.guessed_letters.append(guess)

                    if self.check_letter(guess) == False:
                        self.jumper.remove_line(0) 

                else:
                    print("You've already guessed \"" + guess + "\"")                 
            else:
                print("Please enter a valid letter")
        except: #If input is blank
            print("Please try again")
       
    def do_updates(self):
        """Checks if letters guessed are correct

        Args:
            self (Director): An instance of Director.
        """
        if self.check_win():
            self.is_playing = False

    def check_win(self):
        for letter in self.word:
            if letter not in self.guessed_letters :
                return False
        return True

    def check_letter(self, letter):
        if letter in self.word:
            return True
        return False
            