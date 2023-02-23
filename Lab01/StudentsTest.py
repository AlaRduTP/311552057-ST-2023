import unittest
import Students


class Test(unittest.TestCase):
    students = Students.Students()

    user_name = ['John', 'Mary', 'Thomas', 'Jane']
    user_id = []

    # test case function to check the Students.set_name function
    def test_0_set_name(self):
        for name in self.user_name:
            uid = self.students.set_name(name)
            self.assertEqual(self.students.name[uid], name)

    # test case function to check the Students.get_name function
    def test_1_get_name(self):
        for uid, name in enumerate(self.user_name):
            self.assertEqual(self.students.get_name(uid), name)
        MEX = len(self.user_name)
        self.assertEqual(self.students.get_name(MEX), 'There is no such user')
