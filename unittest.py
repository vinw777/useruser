import unittest
from datetime import datetime
from user import User
from userservice import UserService
from UserUtil import UserUtil

class TestUser(unittest.TestCase):
    def test_get_details(self):
        user = User(1, "John", "Doe", datetime(1990, 5, 15))
        details = user.get_details()
        self.assertIn("John Doe", details)
        self.assertIn("john.doe@example.com", details)

    def test_get_age(self):
        user = User(1, "John", "Doe", datetime(1990, 5, 15))
        self.assertEqual(user.get_age(), datetime.today().year - 1990)


class TestUserService(unittest.TestCase):
    def test_add_user(self):
        user = User(1, "John", "Doe", datetime(1990, 5, 15))
        UserService.add_user(user)
        self.assertEqual(len(UserService.users), 1)

    def test_find_user(self):
        user = User(1, "John", "Doe", datetime(1990, 5, 15))
        UserService.add_user(user)
        found_user = UserService.find_user(1)
        self.assertEqual(found_user.user_id, 1)

    def test_delete_user(self):
        user = User(1, "John", "Doe", datetime(1990, 5, 15))
        UserService.add_user(user)
        UserService.delete_user(1)
        self.assertEqual(len(UserService.users), 0)

    def test_update_user(self):
        user = User(1, "John", "Doe", datetime(1990, 5, 15))
        UserService.add_user(user)
        updated_user = User(1, "Jane", "Doe", datetime(1992, 5, 15))
        UserService.update_user(1, updated_user)
        self.assertEqual(UserService.find_user(1).name, "Jane")


class TestUserUtil(unittest.TestCase):
    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertEqual(len(user_id), 9)
        self.assertTrue(user_id[:2].isdigit())

    def test_generate_password(self):
        password = UserUtil.generate_password()
        self.assertTrue(UserUtil.is_strong_password(password))

    def test_validate_email(self):
        valid_email = "john.doe@example.com"
        invalid_email = "john.doe.com"
        self.assertTrue(UserUtil.validate_email(valid_email))
        self.assertFalse(UserUtil.validate_email(invalid_email))


if __name__ == '__main__':
    unittest.main()
