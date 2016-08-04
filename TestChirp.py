import unittest
from user import *
from main_menu import *
from chirp import *


class TestChirp(unittest.TestCase):

  # ------------------- PUBLIC CHIRP ---------------------
  def test_new_public_chirp_creation(self):
    chirper = User('Carter Harris', 'carter_harris')
    chirp = Chirp(
                  "message",
                  chirper.uuid,
                  private=False,
                  # receiver_id=False
                  receiver_id=None
                  )
    self.assertEqual(chirp.message, "message")
    self.assertEqual(chirp.chirper_id, chirper.uuid)
    self.assertEqual(chirp.private, False)
    self.assertEqual(chirp.receiver_id, None)


  # ------------------- PRIVATE CHIRP ---------------------
  def test_new_private_chirp_creation(self):
    chirper = User('Carter Harris', 'carter_harris')
    chirp = Chirp(
                  "message",
                  chirper.uuid,
                  private=True,
                  receiver_id=True
                  )
    self.assertEqual(chirp.message, "message")
    self.assertEqual(chirp.chirper_id, chirper.uuid)
    self.assertEqual(chirp.private, True)
    self.assertEqual(chirp.receiver_id, True)


if __name__ == '__main__':
    unittest.main()













