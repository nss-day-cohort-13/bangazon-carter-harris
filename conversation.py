from main_menu import *
from chirp import *

class Conversation:

  def __init__(self, chirp_id):
    self.conversation_id = uuid.uuid4()
    self.chirp_list = []
    self.chirp_list[0] = chirp_id


  def add_reply_to_conversation(self, chirp_id):
    self.chirp_list.append(chirp_id)

