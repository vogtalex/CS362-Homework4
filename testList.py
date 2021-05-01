import unittest
import list

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		list1 = [2, 4, 6, 8, 10]
		list2 = [1, 13 ,22, 13]
		self.assertEqual(list.listAverage(list1), 6)
		self.assertEqual(list.listAverage(list2), 12.25)

	

if __name__ == '__main__':
	unittest.main()