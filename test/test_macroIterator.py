import unittest
from hotkeys import HotKeys
from lib_RecentOperations import RecentOperations
import macroIterator

from unittest.mock import patch


class MacroIteratorTestHotKeys(HotKeys):
    def __init__(self, ignoreFn=True):
        super().__init__(ignoreFn)
        self.macroDict = {
            'test': {'keys': ['f1'], 'block': False},
            'testException': {'keys': ['f2'], 'block': False},
            'testBlocking': {'keys': ['f3'], 'block': True},
            'testSequence': {'sequences': [[{'key': 'FN', 'down': True}, {'key': 'F4', 'down': True}]], 'block': True},
        }
        self.setMacros(self.macroDict)
        print(self.getMacros())

    def execute(self, macroName):
        if macroName == 'test':
            pass
        elif macroName == 'testException':
            raise Exception('execution error')


class TestMacroIterator(unittest.TestCase):

    def setUp(self):
        self.macroIteratorTestHotKeys = MacroIteratorTestHotKeys()
        self.exceptionLog = {}
        self.recentOperations = RecentOperations()

    def handleException(self, f, t, e):
        self.exceptionLog = {'from': f, 'type': t, 'exceptionString': str(e)}

    def testMacroIterator(self):
        block = macroIterator.runMacros([self.macroIteratorTestHotKeys], {'F1': True}, self.recentOperations)
        self.assertEqual(False, block)

    def testExecutionError(self):
        with patch('macroIterator.exceptionHandler') as mockExceptionHandler:
            mockExceptionHandler.side_effect = lambda f, t, e: self.handleException(f, t, e)
            block = macroIterator.runMacros([self.macroIteratorTestHotKeys], {'F2': True}, self.recentOperations)
            self.assertEqual(False, block)
            self.assertEqual('execution', self.exceptionLog['from'])
            self.assertEqual(Exception, self.exceptionLog['type'])
            self.assertEqual('execution error', self.exceptionLog['exceptionString'])

    def testRunError(self):
        with patch('macroIterator.exceptionHandler') as mockExceptionHandler:
            mockExceptionHandler.side_effect = lambda f, t, e: self.handleException(f, t, e)
            block = macroIterator.runMacros([None], {'F2': True}, self.recentOperations)
            self.assertEqual(False, block)
            self.assertEqual('run', self.exceptionLog['from'])
            self.assertEqual(AttributeError, self.exceptionLog['type'])
            self.assertEqual("'NoneType' object has no attribute 'getMacros'", self.exceptionLog['exceptionString'])

    def testNormal(self):
        block = macroIterator.runMacros([self.macroIteratorTestHotKeys], {'F3': True}, self.recentOperations)
        self.assertEqual(True, block)

    def testSequence(self):
        self.recentOperations.addOperation('fn', True)
        self.recentOperations.addOperation('f4', True)
        block = macroIterator.runMacros([self.macroIteratorTestHotKeys], {'F4': True}, self.recentOperations)
        self.assertEqual(True, block)

    def testNotInList(self):
        block = macroIterator.runMacros([self.macroIteratorTestHotKeys], {'F5': True}, self.recentOperations)
        self.assertEqual(False, block)

    def testIgnoreFn(self):
        block = macroIterator.runMacros([self.macroIteratorTestHotKeys], {'FN': True, 'F5': True},
                                        self.recentOperations)
        self.assertEqual(False, block)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
