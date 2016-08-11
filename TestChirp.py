import unittest
from main_menu import *
from user import *
from chirp import *


class TestChirp(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.source = User("Hamilton Harris", "Lol")
    self.target = User("Carter Harris", "Lul")



  # ---------- PUBLIC CHIRP CREATION ----------
  def test_new_public_chirp_creation(self):
    chirp = Chirp(
      message='lol',
      user_id=self.source.user_id,
    )
    self.assertIsInstance(chirp, Chirp)
    self.assertIsNotNone(chirp.chirp_id)
    self.assertEqual(chirp.message, "lol")
    self.assertEqual(chirp.author, self.source.user_id)
    self.assertEqual(chirp.private, False)


  # ---------- REPLY PUBLIC CHIRP CREATION ----------
  def test_reply_to_public_chirp_creation(self):
   chirp = Chirp(
     message='lol',
     user_id=self.source.user_id,
   )
   self.assertIsInstance(chirp, Chirp)
   self.assertIsNotNone(chirp.chirp_id)
   self.assertEqual(chirp.message, "lol")
   self.assertEqual(chirp.author, self.source.user_id)
   self.assertEqual(chirp.private, False)




  # ---------- PRIVATE CHIRP CREATION ----------
  def test_new_private_chirp_creation(self):
    chirp = Chirp(
      message="lol",
      user_id=self.source.user_id,
      private=True,
      receiver_id=self.target.user_id
    )
    self.assertIsInstance(chirp, Chirp)
    self.assertIsNotNone(chirp.chirp_id)
    self.assertEqual(chirp.message, "lol")
    self.assertEqual(chirp.author, self.source.user_id)
    self.assertEqual(chirp.private, True)
    self.assertEqual(chirp.receiver, self.target.user_id)


  # ------- REPLY PRIVATE CHIRP CREATION -------
  def test_reply_to_private_chirp_creation(self):
    chirp = Chirp(
      message="lol",
      user_id=self.source.user_id,
      private=True,
      receiver_id=self.target.user_id
    )
    self.assertIsInstance(chirp, Chirp)
    self.assertIsNotNone(chirp.chirp_id)
    self.assertEqual(chirp.message, "lol")
    self.assertEqual(chirp.author, self.source.user_id)
    self.assertEqual(chirp.private, True)
    self.assertEqual(chirp.receiver, self.target.user_id)


if __name__ == '__main__':
    unittest.main()
