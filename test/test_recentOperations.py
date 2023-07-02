import unittest
from lib_RecentOperations import RecentOperations


class TestRecentOperations(unittest.TestCase):

    def setUp(self):
        self.recentOperations = RecentOperations(5)

    def testEmpty(self):
        self.assertEqual([], self.recentOperations.getAll())
        self.assertEqual(None, self.recentOperations.getLast())
        self.assertEqual(None, self.recentOperations.getLastNItems(1))

    def testWithin(self):
        self.recentOperations.addOperation('a', True)
        self.recentOperations.addOperation('a', False)
        self.recentOperations.addOperation('ctrl', True)
        self.recentOperations.addOperation('ctrl', False)
        self.assertEqual(
            [
                {'down': True, 'key': 'A'},
                {'down': False, 'key': 'A'},
                {'down': True, 'key': 'CTRL'},
                {'down': False, 'key': 'CTRL'}
            ],
            self.recentOperations.getAll()
        )
        self.assertEqual({'down': False, 'key': 'CTRL'}, self.recentOperations.getLast())
        self.assertEqual([{'down': True, 'key': 'CTRL'}, {'down': False, 'key': 'CTRL'}],
                         self.recentOperations.getLastNItems(2))
        self.assertEqual(
            [
                {'down': True, 'key': 'A'},
                {'down': False, 'key': 'A'},
                {'down': True, 'key': 'CTRL'},
                {'down': False, 'key': 'CTRL'}
            ],
            self.recentOperations.getLastNItems(5)
        )

    def testOver(self):
        self.recentOperations.addOperation('a', True)
        self.recentOperations.addOperation('a', False)
        self.recentOperations.addOperation('ctrl', True)
        self.recentOperations.addOperation('ctrl', False)
        self.recentOperations.addOperation('a', True)
        self.recentOperations.addOperation('a', False)
        self.recentOperations.addOperation('ctrl', True)
        self.recentOperations.addOperation('ctrl', False)

        self.assertEqual(
            [
                {'down': False, 'key': 'CTRL'},
                {'down': True, 'key': 'A'},
                {'down': False, 'key': 'A'},
                {'down': True, 'key': 'CTRL'},
                {'down': False, 'key': 'CTRL'}
            ],
            self.recentOperations.getAll()
        )


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
