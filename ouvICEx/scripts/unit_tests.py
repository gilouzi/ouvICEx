import unittest
from analyses import get_statistics

EMPTY = ''

class TestAnalyses(unittest.TestCase):
	def test_algo_do_analyses(self):
		self.assertEqual(get_statistics(EMPTY, EMPTY, 'real', test_case = 1), 0)
		
		
if __name__ == '__main__':
	unittest.main()
