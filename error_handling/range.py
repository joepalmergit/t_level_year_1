milage_valid = False

while not milage_valid:
	milage = int(input("Enter your yearly milage: "))

	if milage >= 1000:
		print("Valid milage.")

		milage_valid = True

	else:
		print("Invalid milage.")

