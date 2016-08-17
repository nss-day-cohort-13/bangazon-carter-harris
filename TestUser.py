import unittest

from main_menu import *
from user import *


class TestUser(unittest.TestCase):

  # ------------- USER -------------
  def test_create_user_has_attributes(self):
    user = User('Carter Harris', 'carter_harris')
    self.assertIsInstance(user, User)
    self.assertIsNotNone(user.user_id)
    self.assertEqual(user.full_name, 'Carter Harris')
    self.assertEqual(user.screen_name, 'carter_harris')

if __name__ == '__main__':
    unittest.main()
