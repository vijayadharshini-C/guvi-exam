

kms = int(input(" Enter the no:of kms the customer has travelled: "))

if(kms < 50):
    amount = kms * 2.60
    surcharge = 5
elif(kms <= 100):
    amount = 130 + ((kms- 50) * 3.25)
    surcharge = 10
elif(kms <= 200):
    amount = 130 + 162.50 + ((kms - 100) * 5.26)
    surcharge = 15
else:
    amount = 130 + 162.50 + 526 + ((kms - 200) * 8.45)
    surcharge = 25

total = amount + surcharge
print("\n = %.2f"  %total,"RS")
