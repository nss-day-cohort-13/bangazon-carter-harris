import unittest
from user import *
from main_menu import *
from chirp import *


class TestChirp(unittest.TestCase):

  # ------------------- CHIRP ---------------------
  def test_new_public_chirp_creation(self):
    chirp_origin = User('Carter Harris', 'carter_harris')
    chirp = Chirp(
                  "message",
                  chirp_origin,
                  private=True,
                  receiver_id=True
                  )
    self.assertEqual(chirp.message, "message")
    self.assertEqual(chirp.chirp_origin, chirp_origin)
    self.assertEqual(chirp.private, True)
    self.assertEqual(chirp.receiver_id, True)



  def test_new_private_chirp_creation(self):
    pass




if __name__ == '__main__':
    unittest.main()













