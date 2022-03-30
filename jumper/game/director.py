<<<<<<< HEAD
from game.jumper import Jumper
=======
#from game.jumper import Jumper
>>>>>>> parent of 1cfaf6f (take 2)
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
<<<<<<< HEAD
        self._jumper = Jumper()
        self._word_bank = Word_bank()
        self._guessed_letters = []
        self._is_playing = True
        self._word_bank.choose_word()
        self._word = list(self._word_bank.get_word())
=======
        #self.jumper = Jumper()
        self.word_bank = Word_bank()
        self.guessed_letters = []
        self.is_playing = True
        self.word_bank.choose_word()
        self.word = list(self.word_bank.get_word())
>>>>>>> parent of 1cfaf6f (take 2)

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
<<<<<<< HEAD
        #If jumper is dead
            #self._is_playing = False
        
        self._jumper.jumper_man()
        print("^^^^^^^^^")
        print()
=======
        #print(self.jumper)
>>>>>>> parent of 1cfaf6f (take 2)

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
<<<<<<< HEAD
                if guess not in self._guessed_letters:
                    self._guessed_letters.append(guess)

                    if self._check_letter(guess) == False:
                        self._jumper.remove_jumper() 

=======
                if guess not in self.guessed_letters:
                    self.guessed_letters.append(guess)
>>>>>>> parent of 1cfaf6f (take 2)
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
<<<<<<< HEAD
        if self._check_win():
            self._is_playing = False
=======
        if self.check_win():
            self.is_playing = False
        #else:
            #remove line from picture
>>>>>>> parent of 1cfaf6f (take 2)

    def _check_win(self):
        for letter in self._word:
            if letter not in self._guessed_letters :
                return False
        return True
<<<<<<< HEAD

    def _check_letter(self, letter):
        if letter in self._word:
            return True
        return False
            
=======
>>>>>>> parent of 1cfaf6f (take 2)
