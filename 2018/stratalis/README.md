# Python Backend Developer

Deadline: The test must be completed before Nov 20, 15:00 (UTC) (24-hour clock).

IDE: We recommend having an IDE ready. 

Resources: You can use help files and other resources programmers normally use.

Test duration: This test normally takes 2h 2min, but you have up to 3h 3min.

| Question | Type          | Environment |
|----------|---------------|-------------|
| 1        | Live Coding   | Python      |
| 2        | Number Picker | -           |
| 3        | Live Coding   | Python      |
| 4        | Live Coding   | Python      |
| 5        | Live Coding   | Python      |
| 6        | Live Coding   | SQL         |
| 7        | Live Coding   | SQL         |
| 8        | Live Coding   | SQL         |

## Python environment

Your code will be evaluated as a Python 3.6.5 source code. In addition to Python Standard Library, the following modules are available:

- pandas 0.22.0
- numpy 1.13.3
- scipy 1.0.1
- scikit-learn 0.19.1

Other third-party libraries cannot be used. For longer problems, we recommend that you copy to and paste from PyDev or a similar development environment.

## SQL environment

Your answer will be executed on an SQLite 3.19.3 database.

## Sample question

Fix the bug

    class MathUtils:
    
        @staticmethod
        def average(a, b):
            return a + b / 2
    
    print(MathUtils.average(2, 1))
