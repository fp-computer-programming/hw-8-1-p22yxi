# Yongdong Xi

def blackjack():
    total = 0
    card1 = int(input("What's the face value of the first card ? "))
    if card1 > 10:
        total += 10
    else:
        total += card1
    card2 = int(input("What's the face value of the first card ? "))
    if card2 > 10:
        total += 10
    else:
        total += card2   
    print(total)
    
    
blackjack()