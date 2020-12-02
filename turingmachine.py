"""Turing Machine Module docstring - Will Heffernan"""
class TuringMachine:
    """Class docstring"""
    def __init__(self,programfilename):
        """Init will initialize the variables of the turing machine"""
        # These are the transitions from an inputted state and symbol
        # to an output state, symbol, and direction for the tape head to move
        self.transitions = {}
        self.start_state = ""
        self.final_states = []
        self.program_name = ""

        # This reads the TM program input file and populates the start state,
        # final states, and transitions variables
        self.read_program(programfilename)
        self.tape = None
        self.current_state = self.start_state
        self.position = 1

    def step(self):
        """Step executes one step of the turing machine, based off of the current state and
        the symbol under the tape head"""
        state = self.current_state
        input_symbol = self.tape[self.position]

        # The turing machine computes what state to move to, what symbol to write back,
        # and what direction to move based on the current state and symbol
        transition = self.transitions[(state,input_symbol)]

        # These lines update the state and the symbol on tape
        self.current_state = transition[0]
        self.tape[self.position] = transition[1]
        direction = transition[2]

        # Based off of the direction, this moves the tape head
        if direction == "RIGHT":
            self.position += 1
        else:
            self.position -= 1

    def run(self,tape):
        """Run executes the turing machine on the entire input string"""
        self.tape = tape
        self.current_state = self.start_state

        # Sets the tape head back to the start position, as this may not be the first input
        # string read
        self.position = 1
        step_counter = 0
        print("START",self.program_name)

        # Continues running until it reaches a final state
        while self.current_state not in self.final_states:
            if (self.current_state,self.tape[self.position]) in self.transitions:
                self.print_tape(step_counter)
                self.step()
                step_counter += 1

            # If there is no transitions from the current state and symbol, then the turing machine
            # is in a halting state and the loop stops
            else:
                break
        self.print_tape(step_counter)

    def read_program(self,programfilename):
        """Read Program reads the program from the txt file and saves the
        states and their transitions"""
        program = open(programfilename)
        for line in program:
            args = line.split()
            if len(args) > 0:
                state = args[0]

                # This checks to see if the state is a start state
                if "START" in state:
                    self.start_state = state
                    self.program_name = state.replace("START","")
                input_symbol = args[1]
                next_state = args[2]

                # This checks to see if the state that is transitioned to is a final state
                if "FINAL" in next_state:
                    self.final_states.append(next_state)
                output_symbol = args[3]
                direction = args[4]

                # This creates a dict entry with a tuple of the current state and symbol
                # as a key and a tuple of the next state, the write back symbol, and direction
                # as a value associated with the key
                self.transitions[(state,input_symbol)] = (next_state,output_symbol,direction)

    def print_header(self):
        """Print Header prints the state and transition information"""

        # This iterates through all of the entries in the transitions dict
        # These are the state symbol transitions for the turing machine
        for i in self.transitions:
            transition = self.transitions[i]
            print(i[0],i[1],transition[0],transition[1],transition[2])

    def print_footer(self):
        """Print Footer prints whether the string has been accepted and what
        the string looks like after it has been read"""
        accept_message = ""

        # This tests whether the current state is in final states. This determines whether
        # the string is accepted or not
        if self.current_state in self.final_states:
            accept_message = "FINAL " + self.program_name + " STATE REACHED, HALT AND ACCEPT "
        else:
            accept_message = "HALT AND DO NOT ACCEPT "
        tape_string = self.tape_to_string()
        print("FINISH",self.program_name)
        print()

        # This prints whether the string was accepted or not and the final tape
        print(accept_message,tape_string)
        print("**********************************************************************")
        print()

    def print_tape(self,step_counter):
        """Print Tape prints the current tape, which includes the tape,
        the position of the tape head, the step number, and the state"""
        position_string = ""
        tape_string = self.tape_to_string()
        index = 0

        # This adds blank space before the asterisk, so it is placed where the tape head
        # would be in the string
        while index < self.position:
            position_string += "  "
            index += 1
        position_string += "*"

        print("STEP:    ",step_counter,"    STATE:",self.current_state)
        print("POS:   ",position_string)
        print("TAPE:  ",tape_string)
        print()

    def tape_to_string(self):
        """Tape To String converts the tape from a list to a string"""
        tape_string = ""

        # This iterates through the values in the tape list and adds them to a string
        for i in self.tape:
            tape_string += i
            tape_string += " "
        return tape_string
