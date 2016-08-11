import uuid

from main_menu import *
from conversation import *


class Chirp():

  ''' Create Chirp Object. '''

  def __init__(self, message, user_id, private=False, receiver_id=None):

    '''
      Method creates an object with attributes of message, author,
      inital public message, default receiver, and a UUID.

      Args:
        • message(str) -> message of the Chirp object
        • user_id(str) -> user uuid will be set as the author of the chirp
        • private(boolean) -> optional True/False for the private attribute, initally False
        • receiver_id(str) -> user uuid of the receiver of the private chirp, initally a default of None
    '''

    self.message = message
    self.author = user_id
    self.private = private
    self.receiver = receiver_id
    self.chirp_id = str(uuid.uuid4())
    # new_conversation = Conversation(self.message_id)
