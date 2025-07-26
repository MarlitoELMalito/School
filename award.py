# Get input times for each event
swim = int(input("Enter swimming time (in minutes): "))
cycle = int(input("Enter cycling time (in minutes): "))
run = int(input("Enter running time (in minutes): "))

# Calculate total time
total_time = swim + cycle + run
print("Total time taken for the triathlon:", total_time, "minutes")

# Determine award based on total time
if total_time <= 100:
    print("Award: Provincial colours")
elif total_time <= 105:
    print("Award: Provincial half colours")
elif total_time <= 110:
    print("Award: Provincial scroll")
else:
    print("Award: No award")
