from datetime import date
from main_menu import *


class Chirp:

  def __init__(
              self,
              message,
              chirp_origin,
              private=None,
              receiver_id=None
              ):
    self.message = message
    self.chirp_origin = chirp_origin
    self.private = private
    self.receiver_id = receiver_id


