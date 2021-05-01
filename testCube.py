import unittest
import cube

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(cube.cubeVolume(10), 1000)
		self.assertEqual(cube.cubeVolume(3), 27)

	def test_add_negative(self):
		self.assertEqual(cube.cubeVolume(-10), -1000)
		self.assertEqual(cube.cubeVolume(-3), -27)

	def test_add_decimals(self):
		self.assertEqual(cube.cubeVolume(10.5), 1157.625)
		self.assertEqual(cube.cubeVolume(3.4), 39.304)

if __name__ == '__main__':
	unittest.main()