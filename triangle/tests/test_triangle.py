import unittest
from triangle import triangle_math


class TestTriangle(unittest.TestCase):
	def test_triangle_area(self):
	
		#Test area function with some example data
		self.assertEqual(12, triangle_math.area(6,4))
		
		#Test with floats
		self.assertAlmostEqual(17.79875, triangle_math.area(7.25,4.91))
		
	def area(base,height):
		
		if base < 0 or height < 0:
			raise ValueError('base and height must be positive. \
			Was given base: {}, height {}'.format(base,height))
			
		area = base*height/2
		return area
		
	def test_right_angle_triangle(self):
		
		#example right triangles
		self.assertTrue(triangle_math.is_right_angle(4,5,3))
		self.assertTrue(triangle_math.is_right_angle(7,24,25))
		
		
		#floating point
		self.assertTrue(triangle_math.is_right_angle(2.33333333333, 8, 8.33333333))
		
		self.assertTrue(triangle_math.is_right_angle(1.2222222222, 6.6666666666, 6.7777777777))
		
		#non right angle triangles
		
		self.assertFalse(triangle_math.is_right_angle(14,25,3))
		
		self.assertFalse(triangle_math.is_right_angle(3.1, 23.89, 22.4))
		
		#tests against order dependancy 
		
		self.assertTrue(triangle_math.is_right_angle(4,5,3))
		self.assertTrue(triangle_math.is_right_angle(5,4,3))
		self.assertTrue(triangle_math.is_right_angle(3,5,4))
		
		#TODO zero length sides
		#TODO negative sides
		