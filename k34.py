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

  def pick4d(self):
    self.pick()
    self.m()
    self.tr()
    self.m()
    self.tl()
    self.pick()
    self.m()
    self.tr()
    self.m()
    self.pick()
    self.tl()
    self.m()
    self.tr()
    self.m()
    self.pick()

  def m5(self):
    """move 5"""
    self.m()
    self.m()
    self.m()
    self.m()
    self.m()
  
def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.m5()
    kt.tl()
    kt.m5()
    kt.m()
    kt.m()
    kt.tr()
    kt.pick4d()
    kt.tr()
    kt.m5()
    kt.m()
    kt.tr()
    kt.tr()
    kt.pick4d()
    kt.tl()
    kt.tl()
    kt.m5()
    kt.tl()
    kt.m()
    kt.ta()
    kt.pick4d()
    kt.tr()
    kt.m5()
    kt.tr()
    kt.m()
    kt.m()
    kt.tr()
    kt.m()
    kt.pick4d()
    pass


if __name__ == "__main__":
    run_karel_program()