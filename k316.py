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

  def pick3(self):
    """put 2 beepers in line"""
    self.pick()
    self.m()
    self.pick()
    self.m()
    self.pick()
    self.m()
    self.tr()

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

def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.m()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.pick3()
    kt.pick3()
    kt.pick3()
    kt.pick3()
    pass


if __name__ == "__main__":
    run_karel_program()