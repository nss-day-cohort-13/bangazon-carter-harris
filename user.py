import random
from main_menu import *

class User:
# read and write inside this class
  def __init__(self, full_name, screen_name):

    self.full_name = full_name
    self.screen_name = screen_name

    self.uid = random.randrange(1, 100000000000)


  def writer(self):
    pass

  def readers(self):
    pass
