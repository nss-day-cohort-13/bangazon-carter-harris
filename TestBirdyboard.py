import unittest
from main_menu import *
from user import *


class TestBirdyboard(unittest.TestCase):

  # ----------------- THINGS TO TEST ---------------------
  def test_create_user_has_stuff(self):
    new_user = User('Carter Harris', 'carter_harris')
    self.assertEqual(new_user.full_name, 'Carter Harris')
    self.assertEqual(new_user.screen_name, 'carter_harris')
    self.assertTrue(type(new_user.uid) == int)



if __name__ == '__main__':
    unittest.main()
