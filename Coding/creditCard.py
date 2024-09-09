import re

def is_valid_credit_card(card_number):
    # Check if it starts with 4, 5 or 6
    if not card_number[0] in ['4', '5', '6']:
        return False
    
    # Remove hyphens and check if it's 16 digits
    card_number = card_number.replace('-', '')
    if len(card_number) != 16:
        return False
    
    # Check if it only contains digits
    if not card_number.isdigit():
        return False
    
    # Check for valid grouping
    if '-' in card_number:
        if not re.match(r'^\d{4}-\d{4}-\d{4}-\d{4}$', card_number):
            return False
    
    # Check for 4 or more consecutive repeated digits
    if re.search(r'(\d)\1{3,}', card_number):
        return False
    
    return True

# Read input
N = int(input())
card_numbers = [input().strip() for _ in range(N)]

# Process each card number
for card in card_numbers:
    if is_valid_credit_card(card):
        print("Valid")
    else:
        print("Invalid")

