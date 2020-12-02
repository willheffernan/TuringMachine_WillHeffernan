README for Will Heffernan's Turing Machine Project

I implemented Turing Machines for these problems:
Ones Complement
Incrementing
Recognizing Palindromes
Decrementing
Zeros and Ones
Divisible by 3
Addition

I will include input files for the grader to run, to make things easier.
These input files all start with "xinput" and then the name of the program.
They are of the form: xinput<PROGRAM>.txt

I have one main.py file that runs the turing machine python code. The only thing that changes 
is the turing machine state code files. These are read as command line arguments and are hard
coded into the build scripts.

The build scripts are of the form:
python main.py <PROGRAM FILE> $1 > <OUTPUT FILE>,
where $1 is where the input file will be given on the command line

The program file and output file are hard coded into the build scripts, but the input file will
a command line argument after the script is run.