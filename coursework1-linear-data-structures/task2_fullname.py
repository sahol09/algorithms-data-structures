# TASK 2 - Linked List for Full Name (with menu interface)
# Student ID: A00027052
#
# This program stores all letters of a person's full name
# in a linked list and lets the user:
#   - print the list
#   - print the full name
#   - add a letter
#   - add a whole word
#   - search for a letter
#   - get an element by position
#   - remove a whole word (first / middle / last)
#
# The menu makes it easy to show each operation one by one.


# NODE CLASS 
class Node:
    """A single node in the linked list."""

    def __init__(self, position, letter, part):
        self.position = position      # integer, starting from 1
        self.letter = letter          # single character, lowercase
        self.part = part              # 'f', 'm', or 'l'
        self.next = None              # pointer to next node


# FULL_NAME CLASS 
class Full_Name:
    """Linked list that stores all letters of the full name."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0   # how many letters are in the list

    # add one letter 
    def Add_element(self, letter, part):
        """
        Add one new letter node to the end of the linked list.
        part should be 'f', 'm', or 'l'.
        """
        letter = letter.lower()
        new_position = self.size + 1
        new_node = Node(new_position, letter, part)

        if self.head is None:
            # list is empty
            self.head = new_node
            self.tail = new_node
        else:
            # attach to the end
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    # add a full word 
    def Add_word(self, word, part):
        """
        Add an entire word to the list.
        Each character becomes a node with the same part flag.
        """
        word = word.lower()
        for ch in word:
            self.Add_element(ch, part)

    # get element by position 
    def Get_element(self, position):
        """
        Return the node at a given position (1-based).
        If position is invalid, print error and return None.
        """
        if position < 1 or position > self.size:
            print(f"Error: position {position} is out of bounds.")
            return None

        current = self.head
        while current is not None:
            if current.position == position:
                return current
            current = current.next

        print(f"Error: position {position} not found in list.")
        return None

    # search for a letter 
    def Search_element(self, letter):
        """
        Search for all positions of a given letter.
        Prints positions separated by commas, e.g. 3,6,7
        """
        letter = letter.lower()
        positions = []
        current = self.head

        while current is not None:
            if current.letter == letter:
                positions.append(current.position)
            current = current.next

        if positions:
            print("Positions:", ",".join(str(p) for p in positions))
        else:
            print("Letter not found")

    # print the whole list 
    def Print_list(self):
        """
        Print the contents of the linked list like:
        [(1, 'k', 'f'), (2, 'e', 'f'), ...]
        """
        elements = []
        current = self.head
        while current is not None:
            elements.append(
                f"({current.position}, '{current.letter}', '{current.part}')"
            )
            current = current.next
        print("[" + ", ".join(elements) + "]")

    # print the full name normally 
    def Print_full_name(self):
        """
        Print the full name as words, with first letter capitalised.
        Example: "Keelt Ergu Bral"
        """
        first_letters = []
        middle_letters = []
        last_letters = []

        current = self.head
        while current is not None:
            if current.part == 'f':
                first_letters.append(current.letter)
            elif current.part == 'm':
                middle_letters.append(current.letter)
            elif current.part == 'l':
                last_letters.append(current.letter)
            current = current.next

        first = "".join(first_letters)
        middle = "".join(middle_letters)
        last = "".join(last_letters)

        words = []
        if first:
            words.append(first.capitalize())
        if middle:
            words.append(middle.capitalize())
        if last:
            words.append(last.capitalize())

        full_name_str = " ".join(words)
        print(full_name_str)

    # remove first/middle/last name 
    def Remove_word(self, part):
        """
        Remove all letters belonging to:
            part = 'f' (first), 'm' (middle), or 'l' (last)
        After removal, positions are updated to stay consecutive.
        """
        if part not in ('f', 'm', 'l'):
            print("Invalid part for Remove_word. Use 'f', 'm', or 'l'.")
            return

        current = self.head
        prev = None

        while current is not None:
            if current.part == part:
                # delete this node
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next

                if current == self.tail:
                    self.tail = prev

                self.size -= 1
                current = current.next
            else:
                prev = current
                current = current.next

        # reassign positions to be 1,2,3,...
        pos = 1
        current = self.head
        while current is not None:
            current.position = pos
            pos += 1
            current = current.next


# HELPER FUNCTIONS
def get_single_word(prompt):
    """
    Ask the user for a name.
    If they type more than one word, only the first is used.
    If they press Enter, returns an empty string.
    """
    text = input(prompt).strip()
    if text == "":
        return ""
    return text.split()[0]


def show_menu():
    """Print the simple text menu."""
    print("\n--- MENU ---")
    print("1 - Print linked list")
    print("2 - Print full name")
    print("3 - Add a letter")
    print("4 - Add a word")
    print("5 - Search for a letter")
    print("6 - Get element by position")
    print("7 - Remove a word (first / middle / last)")
    print("0 - Exit")
    choice = input("Enter your choice: ").strip()
    return choice


# MAIN PROGRAM 
def main():
    print("TASK 2 - Linked List for Full Name (Menu Version)\n")

    # 1. Ask user for names
    first_name = get_single_word("Enter first name: ")
    middle_name = get_single_word("Enter middle name (or press Enter to skip): ")
    last_name = get_single_word("Enter last name: ")

    # 2. Build the linked list
    full = Full_Name()

    if first_name:
        full.Add_word(first_name, 'f')
    if middle_name:
        full.Add_word(middle_name, 'm')
    if last_name:
        full.Add_word(last_name, 'l')

    print("\nInitial linked list and full name:")
    full.Print_list()
    full.Print_full_name()

    # 3. Menu loop
    while True:
        choice = show_menu()

        if choice == "1":
            print("\nCurrent linked list:")
            full.Print_list()

        elif choice == "2":
            print("\nCurrent full name:")
            full.Print_full_name()

        elif choice == "3":
            letter = input("Enter a single letter to add: ").strip()
            if len(letter) != 1:
                print("Please enter exactly one character.")
                continue
            part = input("Which part? (f = first, m = middle, l = last): ").strip().lower()
            if part not in ("f", "m", "l"):
                print("Invalid part. Use f, m or l.")
                continue
            full.Add_element(letter, part)
            print("Letter added.")

        elif choice == "4":
            word = input("Enter the word to add: ").strip()
            if word == "":
                print("Word cannot be empty.")
                continue
            part = input("Which part? (f = first, m = middle, l = last): ").strip().lower()
            if part not in ("f", "m", "l"):
                print("Invalid part. Use f, m or l.")
                continue
            full.Add_word(word, part)
            print("Word added.")

        elif choice == "5":
            letter = input("Enter the letter to search for: ").strip()
            if len(letter) != 1:
                print("Please enter exactly one character.")
                continue
            full.Search_element(letter)

        elif choice == "6":
            pos_str = input("Enter position (starting from 1): ").strip()
            if not pos_str.isdigit():
                print("Position must be a positive integer.")
                continue
            pos = int(pos_str)
            node = full.Get_element(pos)
            if node is not None:
                print(f"Position {node.position}: letter '{node.letter}', part '{node.part}'")

        elif choice == "7":
            part = input("Which word to remove? (f = first, m = middle, l = last): ").strip().lower()
            full.Remove_word(part)
            print("After removing that word:")
            full.Print_list()
            full.Print_full_name()

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    