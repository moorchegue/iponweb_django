Introduction
------------
Realtor agency has developed a tiny application to simplify storing information
about selling houses and automatically assign one of agent to service every
deal.

You is the second developer of this application and should improve it by adding
new functions and fixing mistakes maded by your predecessor.

Please, Don't pay too much attention to beauty of HTML and whole UI.

If some of the tasks will consume too much time, please, write a few sentences
about the ways with which you planned to solve it. And why you choose these
ways.

Task 0 - Installation
---------------------
Main application called "realtdb". You should connect them to project before
start work on the other tasks.

Useful info:

* Project already configured to use SQLite as main database engine.
* When you finish connecting of "realtdb" you should create database and install
  initial data set by using command `manage.py loaddata realtor houses`.

Now please run the project in development mode by using `runserver`.

Task 1 - Validation of the user's input
---------------------------------------
Find a start URL to open application in browser (and do it). You will see the
simple interface containing list of all entered houses with the form to input
new ones.

Now this form does not performs validation of input data. For example, try to
add new house using this form but enter a string instead of number into a
"price" field.

You should implement validation of the input data in a way that is natural for
Django. Users should be able to see what is wrong with their data.

Task 2 - Analyzing queries
--------------------------
Press button "Show SQL" in the footer of page. You will see the list of all SQL
queries performed during loading the page.

All of this queries are neccessary? Could you reduce total amount of them? Do it
if you can.

Task 3 - Extension
------------------
Your agency now starts to sell an apartments. And you should make additional
page to operate with them. Take a look at top navigation bar - here you can find
already prepared link "Apartments".

The apartments are very similar to houses but contains three additional fields:

- count of rooms in apartment
- number of floor
- total count of floors in the building where apartment located

You should make a separate page for adding apartments similarly to
houses. Please, keep in mind that in nearest future you may face with another
kinds of the real estate: rooms, offices etc.

Also, please, ensure that user should not be able to enter number of floor which
is greater than total number of floors in building.
