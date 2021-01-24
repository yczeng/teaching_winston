weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekends = ["Saturday", "Sunday"]

def checkDayOfTheWeek(day):
	if day in weekdays:
			return "weekday"
	elif day in weekends:
		return "weekend"
	else:
		return "not a day of the week"


# test case 1
print(checkDayOfTheWeek("Monday"))

# test case 2
print(checkDayOfTheWeek("Sunday"))

# test case 3
print(checkDayOfTheWeek("carrot"))


''' Winston wants to figure out what to do

if it's a weekday, he will go to school
if it's a weekend, he will play tennis

program will say that the input is incorrect

input: String day
output: String school or tennis

'''

def tennisOrSchool(day):
	if checkDayOfTheWeek(day) == "weekday":
		return "school"
	elif checkDayOfTheWeek(day) == "weekend":
		return "tennis"
	else:
		return "not a day of the week"

print("\n==================================\n")

# test case 1
print(tennisOrSchool("Monday"))

# test case 2
print(tennisOrSchool("Sunday"))

# test case 3
print(tennisOrSchool("carrot"))





for i in 