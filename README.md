# Homework
- Name: Felix Fonderie

## Question 1) Define the following unit, integration, regression tests and when you would use each?
- Unit test:A test that is meant to see if a module is functioning properly.
- Integration test: Useful for when you need to see if two functional modules work together as you intended.
- Regression test: useful for when you want to make sure that your code works, and then continues to work after a change.

## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is
pytest looks for files and functions that start with test_ or end with _test. and runs those files when you test using pytest.
A fixture is a decorator that you put onto a function. That function sets up the conditions for a test or many tests. You can call a test with that fixture function as a parameter to test using its set up variables. Convenient for when you need to repeatedly set up a scenario for testing.

