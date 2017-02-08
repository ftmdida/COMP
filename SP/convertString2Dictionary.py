import urllib
import re


def convertString2Dictionary(inputString = ""):
    try:
        inputString.decode('utf-8')
        inputString = urllib.unquote(inputString)

        inputValue = re.split(r'[=,]+', inputString)
        errorDict = {'error': 'true'}
        dictionary = dict()
        for i in range(len(inputValue)):
            if i % 2 == 0:
                if inputValue[i].lstrip(' ').isalpha():
                    if findDuplicateKey(inputValue[i].lstrip(' '), dictionary):
                        dictionary[inputValue[i].lstrip(' ')] = inputValue[i+1].lstrip(' ')
                    else:
                        return errorDict
                else:
                    return errorDict
        return dictionary
    except UnicodeError:
        return errorDict


def findDuplicateKey(string, dictItems):
    if len(dictItems.items()) > 0:
        for key, value in dictItems.items():
            if str(key) != str(string):
                return True
            else:
                return False
    else:
        return True

