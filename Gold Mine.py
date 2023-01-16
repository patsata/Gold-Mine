location = int(input())

for i in range(location):
    total_days = 0
    expeted_gold = float(input())
    days = int(input())
    total_gold = 0
    while True:
        total_days += 1
        if total_days <= days:
            gold = float(input())
            total_gold += gold
            continue
        else:
            break
    average_gold = total_gold / (total_days - 1)
    if average_gold >= expeted_gold:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    else:
        print(f"You need {expeted_gold - average_gold:.2f} gold.")

