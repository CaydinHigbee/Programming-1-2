from stanfordkarel import *


class ktools:
  def m(self):
    """move"""
    move()

  def tl(self):
    """turn left"""
    turn_left()

  def tr(self):
    """turn right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """turn around"""
    self.tl()
    self.tl()

  def pick(self):
    """pick beeper"""
    pick_beeper()

  def put(self):
    """put beeper"""
    put_beeper()

  def put2(self):
    """put 2 beepers in line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """puts 5 beepers in line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def m5(self):
    self.m()
    self.m()
    self.m()
    self.m()
    self.m()

  def fic(self) -> bool:
    """front is clear"""
    return front_is_clear()

  def fib(self) -> bool:
    """front is blocked"""
    return not self.fic()

  def rib(self) -> bool:
    """right is blocked"""
    return not self.ric()

  def ric(self) -> bool:
    """right is clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True  # Immediatley leaves the function
    self.tl()
    return False

  def mazemove(self):
    """maze move"""
    if self.fib():
      self.tl()
    else:
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()
    pass

def main():
    """ Karel code goes here! """
    kt = ktools()
  
    pass


if __name__ == "__main__":
    run_karel_program()