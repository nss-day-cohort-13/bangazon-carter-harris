import unittest
from user import *
from main_menu import *
from chirp import *
from conversation import *


class TestConversation(unittest.TestCase):

  # -------------------  ---------------------
  def test_conversation_has_chirp_id(self):
    chirp = Chirp('lol', 1234, False, None)
    convo = Conversation(chirp.chirp_id)
    self.assertEqual(convo.chirp_list, [chirp.chirp_id])

  def test_make_a_conversation(self):
    chirp = Chirp('lol', 1234, False, None)
    convo = Conversation(chirp.chirp_id)
    chirp_two = Chirp('lolol', 124, False, None)
    convo.add_reply_to_conversation(chirp_two.chirp_id)
    self.assertEqual(convo.chirp_list[1], chirp_two.chirp_id)





if __name__ == '__main__':
    unittest.main()
