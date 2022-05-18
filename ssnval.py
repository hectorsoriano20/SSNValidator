# SSN (Social Security Number)
# using regular expression
import re

# Function to validate SSN
# (Social Security Number).

def isValidSSN(str):

	# Regex to check valid
	# SSN (Social Security Number).
	regex = "^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$"

	# Compile the ReGex
	p = re.compile(regex)

	# If the string is empty
	# return false
	if (str == None):
		return False

	# Return if the string
	# matched the ReGex
	if(re.search(p, str)):
		return True
	else:
		return False

# Driver code


# Test Case 1:
str1 = input('Digite un numero de Seguridad Social en formato (XXX-XXX-XXXX): ')
print(isValidSSN(str1))


