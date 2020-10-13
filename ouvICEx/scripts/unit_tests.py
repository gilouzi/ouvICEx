import unittest
from analyses import get_statistics

class TestAnalyses(unittest.TestCase):
	def get_statistics_est(self):
		self.assertEqual(get_statistics(0, 0, 'real', test_case = 1), 0)
		
	#def get_statistics_dict_totals(self):
		#print(get_statistics(posts.query.all(), EMPTY, 'real', test_case = 2))
		#self.assertEqual(get_statistics(posts.query.all(), EMPTY, 'real', test_case = 2), 0)
		
	#def get_statistics_labels(self):
		#self.assertEqual(get_statistics(EMPTY, EMPTY, 'real', test_case = 3), 0)
		
if __name__ == '__main__':
	unittest.main()
