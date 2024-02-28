#python: Your goal is to pick out a desired number in the fewest possible turns using  a binary search algorithm. 
# Write a function to help you pick the card with the correct number. 

def pick_card(card_list, card_number):
    start = 0
    end = len(card_list) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if card_list[mid] == card_number:
            return mid
        elif card_list[mid] < card_number:
            start = mid + 1
        else:
            end = mid - 1   
    return -1

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
index = pick_card(cards, target)

if index!= -1:
    print("Target card found at index: ", index)
else:
    print("Target card not found")
