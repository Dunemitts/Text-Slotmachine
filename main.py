import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 0

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): # Goes through how many lines the user bets on
        symbol = columns[0][line] # We're using 0 (first symbol in the row) because we have all of the columns, not all of the rows available to us (the user creates the rows as needed from input)
        for column in columns: # Loops through every column to check for symbol in row
            symbol_to_check = column[line]
            if symbol != symbol_to_check: # If a symbol in a row is not the same as the checking, then we break, no further checks needed
                break
        else: # If we get to the end of the for loop and it doesn't break, then the winner wins
            winnings += values[symbol] * bet # Their winnings are the multiplier for the symbol * their bet on that line (not total bet)
            winning_lines.append(line + 1) # Stores what lines they won on (+1 because of zero point lists, if that wasn't there the line displayed would be -1)
        
    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # Items gets BOTH key and value of the item
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols): # Randomizes the value of a single column / _ is an throwaway variable name, its value is not used in the loop nor is the value of any interest
        column = []
        current_symbols = all_symbols[:] # The : copies the list of all_symbols, it's not a reference (because changes to the reference affects here), it's a copy (a static snapshot)
        for _ in range(rows):
            value = random.choice(current_symbols) # Picks random assortment of symbols
            current_symbols.remove(value) # Removes the chosen symbols out of the current_symbols list
            column.append(value) # Puts them on the single column list
        columns.append(column) # Puts the single column list onto a single column within the wider 3 column list

    return columns

def print_slot_machine(columns): # By default, the print would display the columns horizontally, so we need to transpose it to have it displayed vertically
    for row in range(len(columns[0])): # Finds the amount of rows via the amount of columns we have (assuming we have columns)
        for i, column in enumerate(columns):
            if i != len(columns) - 1: # Makes sure that seperators are in between columns and there's not one at the end
                print(column[row], "|", end=" " ) # Displays the seperator between columns
            else:
                print(column[row]) # Displays columns WITHOUT seperator

def deposit():
    while True: # Constantly asks for valid amount
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): # Checks valid input
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_num_of_lines():
    while True: # Constantly asks for valid amount
        lines = input("Enter the number of lines to bet on (1-" +str(MAX_LINES) + ")? ")
        if lines.isdigit(): # Checks valid input
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True: # Constantly asks for valid amount
        bet = input("What would you like to bet on each line? $")
        if bet.isdigit(): # Checks valid input
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a number.")

    return bet

def spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines:", *winning_lines) # * is the unpack operator that displays the exact winning_line that wins
    return winnings - total_bet

def main(): # Putting this as function so it can be called again if need be
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit).") # Constantly asks for an input to replay so the user doesn't need to keep running the program
        if answer == "q":
            break
        balance += spin(balance) # Balance is updated after every spin

    print(f"You left with ${balance}")

print(ROWS, COLS, symbol_count)
main()