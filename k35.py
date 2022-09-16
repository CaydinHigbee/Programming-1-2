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

  def h(self):
    """print letter H"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.tr()
    self.m()
    self.m()
    self.tr()
    self.put2()
    self.m()
    self.m()
    self.tr()
    self.m()
    self.m()
    self.tl()

  def e(self):
    """print letter E"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.m()
    self.tr()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.put2()

  def l(self):
    self.tl()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()

  def o(self):
      """print letter O"""
      self.tl()
      self.put5()
      self.tr()
      self.m()
      self.put2()
      self.m()
      self.tr()
      self.put5()
      self.tr()
      self.m()
      self.put2()
      self.ta()
      self.m()
      self.m()
      self.m()
      
def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.m()
    kt.tl()
    kt.m()
    kt.tr()
    kt.h()
    kt.m()
    kt.e()
    kt.m()
    kt.m()
    kt.l()
    kt.m()
    kt.m()
    kt.l()
    kt.m()
    kt.m()
    kt.o()
    pass


if __name__ == "__main__":
    run_karel_program()