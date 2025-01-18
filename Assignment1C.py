# Assignment1C.py

print("[Centimeters to feet & inches converter]")

# input
cmlength = float(input("enter the length in centimeters: "))

# conversions
cmperfoot = 30.48
cmperinch = 2.54

feet = int(cmlength // cmperfoot)
remainingcm = cmlength % cmperfoot
inches = remainingcm / cmperinch

# output 
print(f"\nThe length is {feet} feet and {inches:.2f} inches")
