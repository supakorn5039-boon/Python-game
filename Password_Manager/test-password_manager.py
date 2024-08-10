import unittest
from io import StringIO
from unittest.mock import patch, mock_open

from cryptography.fernet import Fernet

from Password_manager import view, add, load_key, Master_pwd, fer


class TestPasswordManager(unittest.TestCase):

    @patch('Password_manager.get_input', return_value='test_master_password')
    def setUp(self, mock_get_input):
        # Simulate loading the encryption key
        self.key = load_key()
        self.fer = Fernet(self.key + 'test_master_password'.encode())

    @patch('Password_manager.open', new_callable=mock_open, read_data="user1|gAAAAABkz9v6...")
    @patch('builtins.print')
    def test_view_valid_format(self, mock_print, mock_file):
        # Simulate the file with correctly formatted data
        encrypted_pwd = self.fer.encrypt('password1'.encode()).decode()
        mock_file.return_value.read.return_value = f'user1|{encrypted_pwd}\n'

        view()
        mock_print.assert_called_with(f'User: user1\nPassword: password1')

    @patch('Password_manager.open', new_callable=mock_open, read_data="user1-password1")
    @patch('builtins.print')
    def test_view_invalid_format(self, mock_print, mock_file):
        # Simulate the file with incorrectly formatted data
        view()
        mock_print.assert_called_with('Skipping line: user1-password1, as it does not match the expected format.')

    @patch('Password_manager.get_input', side_effect=['user2', 'password2'])
    @patch('Password_manager.open', new_callable=mock_open)
    def test_add(self, mock_open, mock_get_input):
        # Simulate adding a new password
        add()
        encrypted_pwd = self.fer.encrypt('password2'.encode()).decode()
        mock_open().write.assert_called_once_with(f'user2 | {encrypted_pwd}\n')

    @patch('Password_manager.get_input', side_effect=['user2', 'password2'])
    @patch('Password_manager.open', new_callable=mock_open)
    def test_add_and_view(self, mock_open, mock_get_input):
        # Simulate adding and then viewing the password
        add()

        mock_open.assert_called_with('password.txt', 'a')
        encrypted_pwd = self.fer.encrypt('password2'.encode()).decode()
        mock_open().write.assert_called_once_with(f'user2 | {encrypted_pwd}\n')

        # Now test the view function
        mock_open.reset_mock()
        mock_open.return_value.read.return_value = f'user2|{encrypted_pwd}\n'

        with patch('builtins.print') as mock_print:
            view()
            mock_print.assert_called_with(f'User: user2\nPassword: password2')


if __name__ == '__main__':
    unittest.main()
