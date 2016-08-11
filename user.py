import random
import uuid
from main_menu import *

class User:

  ''' Create User Object. '''

  def __init__(self, full_name, screen_name):

    '''
      Method creates an object with attributes of full_name, screen_name, and a UUID

      Args:
        • full_name(str)
        • screen_name(str)
    '''

    self.full_name = full_name
    self.screen_name = screen_name
    self.user_id = uuid.uuid4() # creates unique id for each user via the 'import uuid' from line 2
