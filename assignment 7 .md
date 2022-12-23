1. What is the name of the feature responsible for generating Regex objects?

Ans : re. compile()

2. Why do raw strings often appear in Regex objects?

Ans: Raw string arr used so that backslashes do not have to be escaped.

3. What is the return value of the search() method?

The search() method returns -1 if no match is found.

4. From a Match item, how do you get the actual strings that match the pattern?

by using  group() method that will return actual matched text from searched string

5. In the regex which created from the r(\d\d\d)-(\d\d\d-\d\d\d\d) what does group zero cover? 
Group 2? Group 1?

Group zero :  Whole string  i.e  ( (\d\d\d)-(\d\d\d-\d\d\d\d))
Group 1 : first substring 
Group 2: second substring


6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell a regex that you want it to fit real parentheses and periods?


Ans : '\'

7. The findall() method returns a string list or a list of string tuples. What causes it to return one of the two options?


Ans :re.findall() method returns list containing strings.
re.findall().groups()  method returns groups of tuples containing strings.


8. In standard expressions, what does the | character mean?

Ans: '|' character stands for either or

9. In regular expressions, what does the character stand for?

Ans:‘ ? ’ stands for matching either 0 or 1.

10.In regular expressions, what is the difference between the + and * characters?

Ans : ' + ' characters stands for one or more occurrences of match pattern
' * ' character stands for zero or more occurrences of match pattern.


11. What is the difference between {4} and {4,5} in regular expression?

Ans:{4} stands for 4 occurrences  of match in string.
{4, 5} stands for occurrences of match between 4 to 5.


12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular expressions?


Ans:\d  : return a match where the string contains  digits between 0 -9.
\w :  return a match where the string contains words between  a-z or A -Z. 
\s :  return a match where string contains white space character. 


13. What do means by \D, \W, and \S shorthand character classes signify in regular expressions?

Ans :\D  : return a match where the string does not contain digits between 0 -9.
   \W :  return a match where the string does not contain words between  a-z or A -Z. 
   \S :  return a match where string does not contain white space character. 


14. What is the difference between .*? and .*?

Ans:  .*   :   greedy match     '.'  previous character matches zero or more times
 .*? :   non greedy match       ' .'  previous character matches or not


15. What is the syntax for matching both numbers and lowercase letters with a character class?

Ans: [0-9 a-z]

16. What is the procedure for making a normal expression in regax case insensitive?

Ans:By passing 2 nd argument or flag re.I or re.IGNORCASE, to remove ignore case sentivity of characters of string while matching with user defined  match object or match pattern   

17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?


Ans:Special character dot '.'
(Dot.) In the default mode, this matches any character except a newline. If the DOTALL flag has been specified as 2 nd argument in re.compile, this matches any character including a newline.


18 If numReg = re.compile(r'\d+'), what will numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') return?

Ans:Return value is :    ‘X drummers, X pipers, five rings, X hen’

19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?

Ans:This flag allows more flexibility and better formatting when writing more complex regex patterns between the parentheses of the match(), search(), or other regex methods.
The re.VERBOSE argument allows you to add whitespace and comments to the string passed to re.compile()


20. How would you write a regex that match a number with comma for every three digits? It must
'42'
'1,234'
'6,368,745'
but not the following:
'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)



```python
Ans: pattern = r'\d.+' 
string = '6,368,745'
result = re.match(pattern , string)
print(result)

```

 21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'
but not the following:
'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)



```python
import re
regex_pattern = '\w.+'
regex_string = 'Haruto watanabe'
result = re.match(regex_pattern , regex_string )
print(result)


```

Question 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
but not the following:
'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'



```python
import re
regex_pattern = '\w.+'
regex_string = 'Carol throws baseballs.'
result = re.match(regex_pattern , regex_string )
print(result)



```
