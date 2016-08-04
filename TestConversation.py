import unittest
from user import *
from main_menu import *
from chirp import *
from conversation import *


class TestConversation(unittest.TestCase):

  # -------------------  ---------------------
  def test_conversation_has_chirp_id(self):
    chirp = Chirp('hjhjhjh', 1234, False, None)
    convo = Conversation(chirp.message_id)
    self.assertEqual(convo.chirp_id, chirp.message_id)



if __name__ == '__main__':
    unittest.main()













