import unittest
import fullname

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(fullname.createFullName('Alex', "Vogt"), 'Alex Vogt')
		self.assertEqual(fullname.createFullName('Jeff', "Bezos"), 'Jeff Bezos')


if __name__ == '__main__':
	unittest.main()