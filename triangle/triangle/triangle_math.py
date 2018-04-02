def area(base,height):
	'''Compute the area of a triangle with the given base and height'''
	area = base * height/2
	return area
	
def is_right_angle(s1, s2, s3):
	'''Pythagorian theroem'''
	
	sides = [s1,s2,s3]
	sides.sort()#sorts by length
	
	a,b,c = tuple(sides)
	
	if a**2 + b**2 == c**2: #pythagorean theroem
		return True
		
	return math.isclose(a**2 + b**2, c**2) #for decimal comparison