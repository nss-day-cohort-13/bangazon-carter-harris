import random
import uuid
from main_menu import *

class User:

  ''' Create User Object. '''

  def __init__(self, full_name, screen_name):
    self.full_name = full_name
    self.screen_name = screen_name
    self.uuid = uuid.uuid4()
    # self.user_id = random.randrange(1, 100000000000)
