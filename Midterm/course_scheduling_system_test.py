from course_scheduling_system import CSS
from unittest.mock import patch
import unittest

class CSSTest(unittest.TestCase):
    def setUp(self):
        self.css = CSS()

    def test_q1_1(self):
        with patch.object(CSS, 'check_course_exist') as mock_check_course_exist:
            mock_check_course_exist.return_value = True
            courses = [('Algorithms', 'Monday', 3, 4)]
            self.assertTrue(self.css.add_course(courses[0]))
            self.assertEqual(self.css.get_course_list(), courses)

    def test_q1_2(self):
        with patch.object(CSS, 'check_course_exist') as mock_check_course_exist:
            mock_check_course_exist.return_value = True
            courses = [
                ('Algorithms', 'Monday', 3, 4),
                ('Compiler', 'Monday', 4, 5)
            ]
            self.assertTrue(self.css.add_course(courses[0]))
            self.assertFalse(self.css.add_course(courses[1]))
            self.assertEqual(self.css.get_course_list(), courses[:1])

    def test_q1_3(self):
        with patch.object(CSS, 'check_course_exist') as mock_check_course_exist:
            mock_check_course_exist.return_value = False
            course = ('Algorithms', 'Monday', 3, 4)
            self.assertFalse(self.css.add_course(course))

    def test_q1_4(self):
        with patch.object(CSS, 'check_course_exist') as mock_check_course_exist:
            mock_check_course_exist.return_value = True
            with self.assertRaises(TypeError):
                invalid_course = 123
                self.css.add_course(invalid_course)

    def test_q1_5(self):
        with patch.object(CSS, 'check_course_exist') as mock_check_course_exist:
            mock_check_course_exist.return_value = True
            courses = [
                ('Algorithms', 'Monday', 3, 4),
                ('Compiler', 'Tuesday', 4, 5),
                ('Software Testing', 'Tuesday', 6, 7)
            ]
            for c in courses:
                self.assertTrue(self.css.add_course(c))
            self.assertTrue(self.css.remove_course(courses[1]))
            self.assertEqual(mock_check_course_exist.call_count, 4)
            print('\n', self.css)

    def test_q1_6(self):
        with patch.object(CSS, 'check_course_exist') as mock_check_course_exist:
            mock_check_course_exist.return_value = False
            self.assertFalse(self.css.remove_course(('Algorithms', 'Monday', 3, 4)))
            mock_check_course_exist.return_value = True
            self.assertFalse(self.css.remove_course(('Algorithms', 'Monday', 3, 4)))
        with self.assertRaises(TypeError):
            self.css.add_course((123, 'Monday', 3, 4))
        with self.assertRaises(TypeError):
            self.css.add_course(('aaa', 123, 3, 4))
        with self.assertRaises(TypeError):
            self.css.add_course(('aaa', 'Monday', 4, 3))

if __name__ == "__main__":
    unittest.main()
