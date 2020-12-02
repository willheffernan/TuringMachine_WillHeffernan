README for Will Heffernan's Turing Machine Project

I implemented Turing Machines for these problems:
Ones Complement
Incrementing
Recognizing Palindromes
Zeros and Ones
Decrementing
Divisible by 3
Addition

I will include input files for the grader to run, to make things easier.
These input files all start with "xinput" and then the name of the program.
They are of the form: xinput<PROGRAM>.txt

I have one main.py file that takes a program file and an input file. It creates
a turing machine with the program file. Then for every line in the input file, it will run the
turing machine with the line as an input tape. 

The turingmachine.py file executes the turing machine program code. It has methods to run the turing 
machine on an input tape, to execute a step in the turing machine, and to print out header, footer,
and step information.

The build scripts are of the form:
python3 main.py <PROGRAM FILE> $1 > <OUTPUT FILE>,
where $1 is where the input file will be given on the command line

The program file and output file are hard coded into the build scripts, but the input file will
a command line argument.