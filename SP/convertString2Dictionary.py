import urllib
import re


def convertString2Dictionary(inputString = ""):
    try:
        inputString.decode('utf-8')
        inputString = urllib.unquote(inputString)

        inputValue = re.split(r'[=,]+', inputString)
        for i in range(len(inputValue)):
            if i % 2 == 0:
                if inputValue[i].isalpha():
                    print inputValue[i]
            else:
                print "iiii" + inputValue[i]
            i += 1



        # print inputValue
        # inputString = inputString.split(', ')
        # dictionary = dict()
        # for item in inputString:
        #     item = item.split('=')
        #     if len(item) == 2:
        #         #if item[1].startswith(' '):
        #         item[1] = item[1].replace(' ', '')
        #         dictionary[item[0]] = item[1]
        #     elif len(item) > 2:
        #         for i in range(0, len(item)):
        #             dictionary[item[i]] = item[i + 1]
        # return dictionary

    except UnicodeError:
        print 'error' + ':' + 'true'
        errorDict = {'error': 'true'}
        return errorDict
