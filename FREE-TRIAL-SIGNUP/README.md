## NOTES ABOUT THIS EXAMPLE

### signup.py

* All the test's locators have been gathered into a single 
Python dictionary at the top of the file. This allows multiple tests in the
same Signup class to use them. Then, if one of the locators has to be changed, it only has to be changed in one place.

* A module named **helpers** has been imported at the top. Methods inside **helpers** named **generate_date_stamp** and **generate_email** have been called in order to fill the **Email** field of the signup form with a unique email address.

* Since the **Username** field also needs a unique value, the most unique portion of the date stamp has been used--the hhmmss-mmmmmm portion. A string slice ([9:]) will yield the 9th through last characters of the unique date stamp.

* Single quotes have been used everywhere. The *PEP 0008 -- Style Guide for Python Code* states that either single or double quotes are acceptable for strings but that one's code should be consistent in its use of quotes.

* Vertical white space and the liberal use of comments have made the test more readable.

### helpers.py

* generate_email has 3 parameters but our test is only calling it with 1 parameter. The missing 2 parameters will use the default values in the method definition.
