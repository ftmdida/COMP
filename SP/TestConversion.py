import unittest
from convertString2Dictionary import convertString2Dictionary


class MyTestCase(unittest.TestCase):
    def test_validParameterWithOnePair(self):
        self.assertEqual(convertString2Dictionary('abc%3D123'), {'abc':'123'})

    def test_validParameterWithTwoPairs(self):
        self.assertEqual(convertString2Dictionary('function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse'),
                         {'function':'calculatePosition', 'sighting':'Betelgeuse'})

    def test_validParameterWithMultiplePairs(self):
        self.assertEqual(convertString2Dictionary('function%3D%20calculatePosition%2C%20abc%3D123%2C%20abc%3D123'),
                         {'function':'calculatePosition', 'abc':'123', 'abc':'123'})

    # def test_validParameter_PercentEncodedString(self):
    #    self.assertEqual()

    def test_invalidParameter_DuplicateKey(self):
        self.assertEqual(convertString2Dictionary('key%3Dvalue%2C%20key%3Dvalue'), {'error':'true'})

    def test_invalidParameter_MissingValue(self):
        self.assertEqual(convertString2Dictionary('key%3D'), {'error':'true'})

    def test_invalidParameter_MissingKey(self):
        self.assertEqual(convertString2Dictionary('value'), {'error':'true'})

    def test_invalidParameter_InvalidKey(self):
        self.assertEqual(convertString2Dictionary('1key%3Dvalue'), {'error': 'true'})

    def test_invalidParameter_KeyWithEmbeddedBlankCharacters(self):
        self.assertEqual(convertString2Dictionary('k%20e%20y%20%3D%20value'), {'error': 'true'})

    def test_invalidParameter_KeyStartsWithBlankCharacter(self):
        self.assertEqual(convertString2Dictionary('%20key%3D%20value'), {'error': 'true'})

    def test_invalidParameter_ValueWithEmbeddedBlankCharacters(self):
        self.assertEqual(convertString2Dictionary('key%20%3D%20v%20a%20l%20ue'), {'error': 'true'})

    def test_invalidParameter_WithoutKeyValuePairs(self):
        self.assertEqual(convertString2Dictionary(''), {'error': 'true'})

    def test_invalidParameter_WithoutKeyValuePairs_WithBlankString(self):
        self.assertEqual(convertString2Dictionary(' '), {'error': 'true'})

    def test_invalidParameter_KeyValuePairsWithoutLegalSeperator(self):
        self.assertEqual(convertString2Dictionary('key1%3Dvalue%3B%20key2%3Dvalue'), {'error': 'true'})



