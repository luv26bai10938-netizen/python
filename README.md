Scientific Calculator (Python)



A basic command line scientific calculator, written in Python. Asks the user for an operation, then the numbers required, and prints the answer.



Features

Basic arithmetics: addition, subtraction, multiplication, division

Trigonometry: sine, cosine, cosecant (angle in degrees)

Power (b^c)

Square root

Requirements

Python 3.8 or higher (it was created on 3.13)

No external libraries (it uses the standard math library)

How to run

Open a terminal in the projects folder

run:

bash

python world.py

Type an operation when asked, and the numbers required.

Supported operations

Input Operation Numbers asked

+ Addition first, second

- Subtraction first, second

Multiplication first, second

/ Division first, second

sin(x) Sine (degrees) angle

cos(x) Cosine (degrees) angle

cosec(x) Cosecant (degrees) angle

power First^second base, exponent

squareroot Square root number

Example session

scientific calculator

enter operator: +

enter first number 12

enter second number 8

Answer= 20.0

enter operator: power

enter first number 2

enter second number 10

Answer= 1024.0

Project structure

Programs/

├── world.py # Main calculator program

├── Readme.md # Project documentation

└── Statement.md # Problem statement

Known issues/suggested fixes

math.radian should be math.radians (used in sin and cos)

math.cosec does not exist, you should use 1/math.sin(math.radians(b))

Dividing by 0 and squarerooting a negative number results in a crash, please add checks or use try/except

sin, cos, cosec and squareroot ask for a second number not used, can be removed

The prompt text refers to sin, cos, square root, but the program asks for sin(x), cos(x), squareroot, please make them consistent.

Typos: Answe, scrond, squareroot variable text.
