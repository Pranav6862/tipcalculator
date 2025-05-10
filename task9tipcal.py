print("Welcome to the tip calculator")

bill=input("What was the total bill? ") # bill= int (input("What was the total bill? $")) input will betaken as string

tipin=int(input("How much tip would you like to give ? 10, 12, 20 "))
final_tip = ( tipin / 100 ) + 1

tip_bill = ( int(bill) *  (final_tip))

split=input("How many people to split the bill ? ")     # input will betaken as string

Total_bill= tip_bill/ int(split)
#print(f"Each person should pay: {round(Total_bill,2)}")
print(f"Each person should pay: {Total_bill: .2f}")
