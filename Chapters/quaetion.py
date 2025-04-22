every_day=5
total_days =30
total_rupee =0

for day in range(1,total_days+1):
    daily_amount = every_day * day  # Increasing amount each day
    total_rupee += daily_amount
    
    print(f"Day {day}: Added {every_day} rupees, Total = {total_rupee} rupees")

print(f"At the end of the month, the total rupees collected is {total_rupee} rupees.")
