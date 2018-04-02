import random

facts = ['For a right-angled triangle the square of the longest side is equal to the square' 
'Scalene, isocolese, and equilateral are the three types of triangle'
'Google play, Delta Airlines, and CAT all have triangles in their logos'
'The Sierpinski Triangle is a fractle form composed of equilateral triangles']

def random_fact():
	return random.choice(facts)