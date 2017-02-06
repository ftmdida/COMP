import unittest
from convertString2Dictionary import convertString2Dictionary


class MyTestCase(unittest.TestCase):
    # valid parameters
    # 100_0xx
    # With one key-value pair
    def test100_001ValidParameterWithOnePair(self):
        self.assertEqual(convertString2Dictionary('abc%3D123'), {'abc':'123'})

    # With two key-value pairs
    def test100_002ValidParameterWithTwoPairs(self):
        self.assertEqual(convertString2Dictionary('function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse'),
                         {'function':'calculatePosition', 'sighting':'Betelgeuse'})

    # With multiple key-value pairs
    def test100_003ValidParameterWithMultiplePairs(self):
        self.assertEqual(convertString2Dictionary('function%3D%20calculatePosition%2C%20abc%3D123%2C%20abc%3D123'),
                         {'function':'calculatePosition', 'abc':'123', 'abc':'123'})

    # def test_validParameter_PercentEncodedString(self):
    #    self.assertEqual()

    # invalid-parameters
    # should return Python dictionary {'error': 'true'} with invalid key
    # 200_0xx
    # non-string key
    def test200_001InvalidParameter_WithNonStringKey(self):
        self.assertEqual(convertString2Dictionary('42%3D%20value'), {'error': 'true'})

    # key starts with number
    def test200_002InvalidParameter_InvalidKey(self):
        self.assertEqual(convertString2Dictionary('1key%3Dvalue'), {'error': 'true'})

    # key with embedded blank characters
    def test200_003InvalidParameter_KeyWithEmbeddedBlankCharacters(self):
        self.assertEqual(convertString2Dictionary('k%20e%20y%20%3D%20value'), {'error': 'true'})

    # key starts with blank character
    def test200_004InvalidParameter_KeyStartsWithBlankCharacter(self):
        self.assertEqual(convertString2Dictionary('%20key%3D%20value'), {'error': 'true'})

    # duplicate key
    def test200_005InvalidParameter_DuplicateKey(self):
        self.assertEqual(convertString2Dictionary('key%3Dvalue%2C%20key%3Dvalue'), {'error':'true'})

    # missing key
    def test200_006InvalidParameter_MissingKey(self):
        self.assertEqual(convertString2Dictionary('value'), {'error': 'true'})

    # should return Python dictionary {'error': 'true'} with invalid value
    # 300_0xx
    # missing value
    def test300_001InvalidParameter_MissingValue(self):
        self.assertEqual(convertString2Dictionary('key%3D'), {'error':'true'})

    # value with embedded blank characters
    def test300_002InvalidParameter_ValueWithEmbeddedBlankCharacters(self):
        self.assertEqual(convertString2Dictionary('key%20%3D%20v%20a%20l%20ue'), {'error': 'true'})

    # should return Python dictionary {'error': 'true'} with invalid key-value pairs
    # 400_0xx
    # empty input string
    def test400_001InvalidParameter_WithoutKeyValuePairs(self):
        self.assertEqual(convertString2Dictionary(''), {'error': 'true'})

    # blank input string
    def test400_002InvalidParameter_WithoutKeyValuePairs_WithBlankString(self):
        self.assertEqual(convertString2Dictionary('%3D%20'), {'error': 'true'})

    # input string with None
    def test400_003InvalidParameter_WithInvalidKey(self):
        self.assertEqual(convertString2Dictionary(None), {'error': 'true'})

    # non-string
    def test400_004InvalidParameter_WithNonStringKeyValuePairs(self):
        self.assertEqual(convertString2Dictionary(42), {'error': 'true'} )

    # input without legal separator
    def test400_005InvalidParameter_KeyValuePairsWithoutLegalSeparator(self):
        self.assertEqual(convertString2Dictionary('key1%3Dvalue%3B%20key2%3Dvalue'), {'error': 'true'})



