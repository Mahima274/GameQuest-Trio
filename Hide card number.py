def take_card(card):
    #If credit card its length must be sixteen
    if len(card) == 16:
        last_code = card[-4:]
        print("************",last_code)
    else:
        print("Invalid card number")
take_card("4444444444444444")
