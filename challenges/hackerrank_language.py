# https://www.hackerrank.com/challenges/hackerrank-language
import unittest

LANGSTR = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC"
LANGS = LANGSTR.split(':')
def main():
    n = int(input().strip())
    strings = []
    for _ in range(n):
        t = input().strip()
        strings.append(t)
    
    for s in strings:
        if isValidLang(s[6:]):
            print('VALID')
        else:
            print('INVALID')
  
        
def isValidLang(s):
    return s in LANGS
    
if __name__ == '__main__':
    main()

class Test(unittest.TestCase):
    
    def setUp(self):
        ""
        
    def testStart(self):
        self.assertEquals(False, isValidLang('JSONqe'))
        self.assertEquals(False, isValidLang('K'))