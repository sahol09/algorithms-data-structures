# TASK 1 - Stack Algorithm for Student ID
# Student ID: A00027052  (numeric part: 00027052)
#
# What this program does:
# 1. Takes the digits of my student ID.
# 2. Puts all digits inside a stack (last number is on top).
# 3. Keeps removing the top two numbers and:
#       - if both are odd, add them
#       - if both are even, multiply them
#       - if one is odd and one is even, subtract the smaller from the bigger
# 4. Puts the result back into the stack.
# 5. Continues until only one number is left.
#
# Extra feature:
# - After finishing the student ID, the program can also take ANY number
#   from the user and run the same stack algorithm on it.
#

#  STACK CLASS  
class Stack:
    """A simple stack made using a Python list."""

    def __init__(self):
        # This list will hold the items. The end of the list is the top.
        self.items = []

    def push(self, item):
        """Add (push) an item onto the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.items.pop()

    def is_empty(self):
        """Check if the stack has no items."""
        return len(self.items) == 0

    def size(self):
        """Return how many items are in the stack."""
        return len(self.items)

    def __str__(self):
        """Show the stack from bottom to top."""
        return str(self.items)


#  BUILD STACK FROM DIGITS 
def build_stack_from_id(num_str):
    """
    Turn a numeric string into a stack of digits.
    Example: "123" becomes a stack [1, 2, 3]
    (3 is on top because it was added last)
    """
    s = Stack()
    for digit in num_str:
        s.push(int(digit))
    return s


#  PROCESS THE STACK 
def process_stack(s, verbose=True):
    """
    Apply the rules until only one number is left.

    Rules:
      - both odd  -> add
      - both even -> multiply
      - mixed     -> subtract the smaller from the larger
    """
    step = 1

    while s.size() > 1:
        # Take the top two numbers from the stack
        b = s.pop()  # top number
        a = s.pop()  # number under it

        # Check whether each number is odd
        a_odd = (a % 2 == 1)
        b_odd = (b % 2 == 1)

        # Apply the correct rule
        if a_odd and b_odd:
            result = a + b
            operation = f"both odd - {a} + {b} = {result}"
        elif not a_odd and not b_odd:
            result = a * b
            operation = f"both even - {a} * {b} = {result}"
        else:
            result = max(a, b) - min(a, b)
            operation = f"mixed - |{a} - {b}| = {result}"

        # Put result back on the stack
        s.push(result)

        if verbose:
            print(f"Step {step}: {operation}")
            print(f"Stack now (bottom - top): {s}\n")

        step += 1

    # Only one number left now
    final_value = s.pop()

    if verbose:
        print("Final value on stack:", final_value)

    return final_value


#  USER INPUT MODE  
def process_user_input():
    """
    Extra feature:
    Lets the user enter any number and runs the same algorithm.
    """
    print("\nEXTRA FEATURE: Try your own number!")
    user_str = input("Enter a number (digits only), or press Enter to skip: ").strip()

    if user_str == "":
        print("Skipping custom number.\n")
        return

    if not user_str.isdigit():
        print("Invalid input. Please enter digits only.\n")
        return
    print("\nRunning the algorithm on your number...\n")
    custom_stack = build_stack_from_id(user_str)
    print("Initial stack:", custom_stack)
    process_stack(custom_stack, verbose=True)
    print("Done.\n")


#  MAIN FUNCTION 
def main():
    student_id_numeric = "00027052"

    print("\nTASK 1 - STACK ALGORITHM\n")

    # Run the algorithm on MY student ID
    print("Processing student ID number:", student_id_numeric)
    stack = build_stack_from_id(student_id_numeric)
    print("\nInitial stack (bottom - top):", stack)
    print("\nRunning the algorithm...\n")

    final_val = process_stack(stack, verbose=True)

    print(f"Final result for ID A00027052 is: {final_val}\n")

    # Run the algorithm on ANY user-entered number
    process_user_input()


# Run the program
if __name__ == "__main__":
    main()
