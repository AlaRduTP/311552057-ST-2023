from app import Application, MailSystem
from unittest.mock import patch

import unittest


class ApplicationTest(unittest.TestCase):

    app = ...
    children = ['William', 'Oliver', 'Henry', 'Liam']

    def setUp(self):
        # stub
        self.app = Application()
        self.app.selected = self.children[:-1]

    def test_app(self):
        # test Application
        with patch.object(Application, 'get_random_person') as mock_get_random_person:
            mock_get_random_person.side_effect = self.children[:]
            name = self.app.select_next_person()
            print(name, 'selected')
            self.assertEqual(name, self.children[-1])

        # test MailSystem
        with patch.object(MailSystem, 'write') as mock_write, patch.object(MailSystem, 'send') as mock_send:
            congrat_msgs = [f'Congrats, {name}!' for name in self.children]
            mock_write.side_effect = congrat_msgs
            self.app.notify_selected()
            print(*congrat_msgs, sep='\n')
            print(mock_write.call_args_list)
            print(mock_send.call_args_list)
            self.assertEqual(mock_write.call_count, len(self.children))
            self.assertEqual(mock_send.call_count, len(self.children))


if __name__ == "__main__":
    unittest.main()
