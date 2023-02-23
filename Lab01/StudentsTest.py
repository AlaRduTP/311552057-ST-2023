import unittest
import Students


class Test(unittest.TestCase):
    students = Students.Students()

    user_name = ['John', 'Mary', 'Thomas', 'Jane']
    user_id = []

    # test case function to check the Students.set_name function
    def test_0_set_name(self):
        print('Start set_name test\n')
        for name in self.user_name:
            uid = self.students.set_name(name)
            print(uid, name)
            self.assertFalse(uid in self.user_id, uid)
            self.user_id.append(uid)
        print('\nFinish set_name test\n\n')

    # test case function to check the Students.get_name function
    def test_1_get_name(self):

        print('Start get_name test\n')
        print(f'user_id length =  {len(self.user_id)}')
        print(f'user_name length =  {len(self.user_name)}\n')

        for uid, name in zip(self.user_id, self.user_name):
            self.assertEqual(self.students.get_name(uid), name)
            print(f'id {uid} : {name}')
        mex = 0
        while mex in self.user_id:
            mex = mex + 1
        self.assertEqual(self.students.get_name(mex), 'There is no such user')
        print(f'id {mex} : There is no such user')
        print('\nFinish get_name test')
