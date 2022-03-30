from game.jumper import Jumper
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
        self._jumper = Jumper()
        self._word_bank = Word_bank()
        self._guessed_letters = []
        self._is_playing = True
        self._word_bank.choose_word()
        self._word = list(self._word_bank.get_word())

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._do_updates()
            self._do_outputs()
            self._get_inputs()
        exit()

    def _do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        word_display = ""
        for letter in self._word:
            if letter in self._guessed_letters:
                word_display += letter + " "
            else:
                word_display += "_ "

        print(word_display)
        #If jumper is dead
            #self._is_playing = False
        
        self._jumper.jumper_man()
        print("^^^^^^^^^")
        print()

    def _get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        if not self._is_playing:
            return
        try:
            guess = input("Guess a letter [a-z]: ")[0]
            letter_ascii = ord(guess.lower()) # Converts char string to ascii
                
            if 97 <= letter_ascii <= 122: #[97-122] Lowercase Alphabet
                if guess not in self._guessed_letters:
                    self._guessed_letters.append(guess)

                    if self._check_letter(guess) == False:
                        self._jumper.remove_jumper() 

                else:
                    print("You've already guessed \"" + guess + "\"")                 
            else:
                print("Please enter a valid letter")
        except: #If input is blank
            print("Please try again")
       
    def _do_updates(self):
        """Checks if letters guessed are correct

        Args:
            self (Director): An instance of Director.
        """
        if self._check_win():
            self._is_playing = False

    def _check_win(self):
        for letter in self._word:
            if letter not in self._guessed_letters :
                return False
        return True

    def _check_letter(self, letter):
        if letter in self._word:
            return True
        return False
            