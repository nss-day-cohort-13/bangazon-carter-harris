from main_menu import *
from chirp import *

class Conversation:

  def __init__(self, chirp_id):
    '''
      Method creates an object with attributes a converstation id and a
      chirp list that adds the chirp id passed from the init.

      Args:
        • chirp_id(str) -> chirp unique id from the creation of a chirp
    '''

    self.conversation_id = uuid.uuid4()
    self.chirp_list = [chirp_id]


  def add_reply_to_conversation(self, chirp_id):
    '''
      Method adds a chirp to the chirp list with the value of the chirp id.
      It appends to the list to organize chirps in order of replys.

      Args:
        • chirp_id(str) -> chirp unique id from the creation of a chirp
    '''
    self.chirp_list.append(chirp_id)

