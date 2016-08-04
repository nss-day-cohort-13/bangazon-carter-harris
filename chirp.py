from main_menu import *
from conversation import *

class Chirp:

  def __init__(
              self,
              message,
              chirper_id,
              private=True,
              receiver_id=None
              ):
    self.message = message
    self.chirper_id = chirper_id
    self.private = private
    self.receiver_id = receiver_id
    self.message_id = uuid.uuid4()
    new_conversation = Conversation(self.message_id)


