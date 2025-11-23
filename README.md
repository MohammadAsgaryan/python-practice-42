This Python program validates an email address based on a custom format rule.
The required pattern is:

expression@string.string


expression: must consist of letters or a combination of letters and digits.

string: must contain only letters.

The email must include one @ and one . placed in the proper structure.

The program uses Python’s re (regular expressions) module to check whether the input matches the specified pattern.
If the email format is valid, it prints OK.
If not, it prints WRONG.

This script can be used in beginner-level Python exercises involving input validation and regex.