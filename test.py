import unittest
import datetime
import forepast

class TestForepast(unittest.TestCase):
	def test_get(self):
		test_date = datetime.date(1994, 5, 27)
		test_state = "CA"
		test_city = "San_Francisco"
		self.assertIs(type(test_date), datetime.date)
		self.assertTrue(forepast.get(test_date, test_state, test_city))

	def test_zip(self):
		test_zipcode = 94107
		self.assertEqual(('San_Francisco', 'CA'), forepast.ziptocity(test_zipcode))

	def test_cords(self):
		test_lat = 37.776289
		test_long = -122.395234
		self.assertEqual(('San_Francisco', 'CA'), forepast.cordstocity(test_lat,test_long))

if __name__ == '__main__':
	unittest.main()