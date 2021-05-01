import unittest
import cube

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(cube.cubeVolume(10), 1000)
		self.assertEqual(cube.cubeVolume(3), 27)




if __name__ == '__main__':
	unittest.main()