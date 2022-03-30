class Jumper():
    def __init__(self):
        self._picture = ["",
        "   ___",
        "  /___\\",
        "  \   /",
        "   \ /",
        "    0",
        "   /|\\",
        "   / \\"
        ]
        # maybe we could add a variable and a function to 
        # return if jumper is dead?

    def jumper_man(self):
        for line in self._picture:
            print(line)

    def remove_jumper(self):
        #check whats left of the picture or if dead
            #self._picture = ["",
            # "    x",
            # "   /|\\",
            # "   / \\"
            # ]
        #else
        self._picture.pop(1)

# For testing purposes, remove #
# jumper = Jumper()
# jumper.jumper_man()

# jumper.remove_jumper()
# jumper.jumper_man()