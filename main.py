"""Main Module docstring - Will Heffernan"""
import sys

from turingmachine import TuringMachine

# These are the command line arguments
programfilename = sys.argv[1]
infilename = sys.argv[2]

# main function
def main():
    """Main method opens the input file, creates a turing machine with the program file,
    and then runs the turing machine on the lines in the input file"""
    infile = open(infilename)

    # Creates a turing machine with the instructions from the given file
    turing_machine = TuringMachine(programfilename)
    turing_machine.print_header()

    # for each line in the input file it will run the turing machine
    for line in infile:
        # Remove whitespace from line
        line = line.strip()

        # Convert line to a list
        tape = list(line)

        # Run the turing machine on the tape
        turing_machine.run(tape)
        turing_machine.print_footer()

    infile.close()

# This runs the main method
if __name__ == '__main__':
    main()
