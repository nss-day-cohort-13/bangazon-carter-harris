import unittest

from main_menu import *
from user import *


class TestUser(unittest.TestCase):

  # ------------------- USER ---------------------
  def test_create_user_has_attributes(self):
    new_user = User('Carter Harris', 'carter_harris')
    self.assertEqual(new_user.full_name, 'Carter Harris')
    self.assertEqual(new_user.screen_name, 'carter_harris')
    self.assertTrue(type(new_user.user_id) == int)


if __name__ == '__main__':
    unittest.main()
