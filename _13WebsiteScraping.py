'''
Created on 28/03/2014

@author: Beto
'''
import urllib2
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import cookielib
from cookielib import CookieJar
import time

cj =  CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')]

def main():
    #page = 'https://twitter.com/search?q=%40epn&src=typd'
    page = 'http://www.eluniversal.com.mx/rss/notashome.xml'
    sourceCode = opener.open(page).read()
    print sourceCode

    '''
    patFinderTitle = re.findall(r'<title>(.*?)</title>',sourceCode)
    print patFinderTitle
    patFinderLink = re.findall(r'<link>(.*?)</link>',sourceCode)
    '''    

    '''
    re.compile(pattern [, flags])
      compile a regular expression pattern into a regular expression pattern object

    re.match( pattern, string [, flags])
      if zero of more characters at the start of the string match the pattern string, 
      return a corresponding match object, of None if no match is found. Rougly like a 
      search for a pattern that begins with the ^ operator

    re.search( pattern, string [, flags])
      scan through string for a location matching pattern, and return a corresponding
      match object, or None if not match is found

    re.findall( pattern, string, [, flags])
      Return a list of strings giving nonoverlapping matches of pattern in string.
      if there are any grous in patterns, return a list of groups, and a list of
      tuples if the pattern has no more than one group.

    re.finditer( pattern, string, [, flags])
      Return iterator over all nonoverlapping matches of pattern in string.

    re.split( pattern, string, [, maxsplit, flags])
      Split string by occurrences of pattern. if capturing parentheses (()) are used
       in the pattern, the text of all groups in the pattern are also returned in the
       resulting list.

    re.sub( pattern, repl, string [, count, flags])
      Return the string obtained by replacing the (first count) leftmost nonoverlapping
      occurrences of pattern ( a string or a pattern object) in string by repl ( which may
      by a string with backslach scapes that may back-reference a matched group, or a function
      that is passed a single mathc object and return the replacement string).
       
    re.subn( pattern, repl, string, [, count, flags])
      Same as sub, but returns a tuple (new-string, number-of-substitutions-made).

    re.escape( string)
      Return string with all nonalphanumeric characters backslashed, such that they can be 
      compiled as a string literal.
    
    Operator    
    
    .            Matches any character (including newline if DOTALL flag is specified or (?s) at pattern front)
    ^            Matches start of the string ( of every line in MULTILINE mode)
    $            Matches end of the string ( of every line in MULTILINE mode)
    C            Any nonspecial ( or backslash-scaped) charecter matches itself
    R*           Zero or more of preceding regular expression R (as many as possible)
    R+           one or more of preceding regular expression R ( as many as possible)
    R?           Zero or one occurrence of preceding regular expression R ( optional)
    R{m}         Matches exactly m copies of preceding R: a{5} matches 'aaaaa'
    R{m,n}       Matches from m to n repetitions of preceding regular expression R
    R*?, R+?,    Same as *, +, and ? but  matches as few characters/times as possible; these  are known as
    R??, R{m,n}? nongreedy match operators ( unlike others, they match and consume as few characters as possible) 
    [...]        Defines character set: e.g., [a-zA-Z] to match all letters (alternatives, with - for ranges)
    [^...]       Defines complemented characters set: matches if char is not in set
    \            Escapes special chars ( e.g., *+?|()) and introduces special secuences in Table 19-2
    \\           Matches a literal \ ( write as \\\\ in pattern, or use r'\\')
    \N           Matches the content of the group of the same number N: '(.+)' \1 matches "42 42"
        
    R|R         Alternative: matches left or right R
    RR          Concatenation: match both Rs
    (R)         matches any regular expression inside (), and delimits a group ( retain matched substring)
    (?:R)       same as (R) but simply delimits part R and does not denote saved group
    (?=R)       lock-ahead assertion: matches if R  matches next R, but doesn't not consume any of the
                string (e.g., X (?=Y) matches only X if followed by Y )
    (?!R)       Matches if R doesn't match next; negative of (?=R)
    (?P<name>R) Matches any regular expression inside (), and delimits a named group
    (?P=name)   Matches whatever text was matched by the earlier group named name
    (?#...)     A comment; ignored
    (?letter)   Set mode flag; letter is one of aiLmsux (see the Library manual)
    (?<=R)      Look-behind assertion: matches if the current position in the string is preceded by a match
                of R that ends at the current position
    (?<!R)      Matches if the current position in the string is not preceded by a match for R; negative of (?<=R)     
    (?(id/name)yespattern|nopattern)
                will try to match with yespattern if the group with given id or name exist, else with optional
                nopattern
                
    [a-zA-Z0-9_]+ one or more letters, numbers or  underscores
    [\t ]*        zero or more tabs or spaces
    
    Table 19-2  re special secuences
    Secuence    Interpretation
    \number     matches text of group number (numbered from 1)
    \A          Matches only at the start of the string
    \b          Empty string at word boundaries
    \B          Empty string at not word boundaries
    \d          Any decimal digit character ([0-9] for ASCII)
    \D          Any non decimal digit character (^[0-9] for ASCII)
    \s          Any whitespace character ([ \t\n\r\f\v] for ASCII)
    \S          Any non whitespace character (^[ \t\n\r\f\v] for ASCII)
    \w          Any alfanumeric character ([a-zA-Z0-9_] for ASCII)
    \W          Any not alphanumeric character (^[a-zA-Z0-9_] for ASCII)
    \Z          Matches only at the end of the string
    
    '''
   
    patFinderLink = re.compile('<link rel.*href="(.*)"/>')

    findPatTitle = re.findall(patFinderTitle, webpage)
    findPatTitle = re.findall(patFinderLink, webpage)
    '''
    
    listIterator = []
    listIterator[:] = range(1,50)

    soup2 = BeautifulSoup(sourceCode)
    titleSoup = soup2.findAll('title')
    descSoup = soup2.findAll('description')
    linkSoup = soup2.findAll('link')
    
    for i in listIterator:
        print titleSoup[i]
        print descSoup[i]
        print linkSoup[i]
        print '\n'    
    
    
    
     
if __name__ == '__main__': main()

