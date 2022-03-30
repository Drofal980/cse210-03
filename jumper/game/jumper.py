class jumper:
  
  def __init__(self):
    #why string1 for first slot?
    self._picture = ["",
      " ___",
      "/___\\",
      "\   /",
      " \ /",
      "  0",
      " /|\\",
      " / \\"
    ]
  
  def __str__(self):
    for line in self._picture:
      print(line)
    return ""
  
  def __repr__(self):
    self.__str__(self)
  
  def remove_line(self, index):
    self._picture.pop(1)

  def if_dead(self):
    if len(self._picture) <= 4:
      self._picture = ["",
      "  x",
      " /|\\",
      " / \\"
    ]
      return True
    return False
