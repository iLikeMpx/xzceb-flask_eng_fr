import unittest

from machinetranslation import translator

class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(translator.frenchToEnglish('Bonjour'), None)
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')
        

class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(translator.englishToFrench('Hello'), None)
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')
        
unittest.main()