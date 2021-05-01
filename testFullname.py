import unittest
import fullname

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(fullname.createFullName('Alex', "Vogt"), 'Alex Vogt')
		self.assertEqual(fullname.createFullName('Jeff', "Bezos"), 'Jeff Bezos')

	def test_add_numbers(self):
		self.assertEqual(fullname.createFullName('1', "2"), '1 2')
		self.assertEqual(fullname.createFullName('25', "89"), '25 89')

	def test_add_miscellaneous_characters(self):
		self.assertEqual(fullname.createFullName('$teelers f@n', "Black-Yellow"), '$teelers f@n Black-Yellow')
		self.assertEqual(fullname.createFullName('*&^%', "<>?:"), '*&^% <>?:')


if __name__ == '__main__':
	unittest.main()