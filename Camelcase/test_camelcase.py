import unittest

import TitleSentencePractice

from unittest import TestCase

class TestCamelCase(TestCase):
	def test_camelcase_sentence(self):
	
		self.assertEqual('helloWorld', camelcase.camel_case('Hello World')) # does it work in simplicity
		
		self.assertEqual('hello', camelcase.camel_case('Hello')) #does it work with one word
		
		with self.assertRaises(ValueError):
			camelcase.camel_case('???') #does it error with symbols
			
		with self.assertRaises(ValueError):
			camelcase.camel_case('   ') #does it error with spaces
			
		self.assertEqual('helloLittleOne', camelcase.camel_case(' hello little one ')) #does it work with white space
		
		self.assertEqual('helloLittleOne', camelcase.camel_case('hello  little one')) #does it work with more than one space
		
		with self.assertRaises(ValueError):
			camelcase.camel_case('This is /n invalid') #does it error with new line notation
			
		with self.assertRaises(ValueError):
			camelcase.camel_case('This should not work.') #does it error with punctuation
			
		with self.assertRaises(ValueError):
			camelcase.camel_case('This sh3ould not work') #does it error with numbers