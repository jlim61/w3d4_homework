# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints (Not always necessary) 
    # Determine a Logical way to solve the problem
        #Write each step out English
        #Write each step out in Python-esse (sudo-code)
    # Invoke and Test Your Function

# You are given a string s representing an attendance record for a student where each character
#  signifies whether the student was absent, late, or present on that day. The record only 
# contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutivedays.
# Return true if the student is eligible for an attendance award, or false otherwise.

# Example 1:
# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:
# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

# WHAT I HAVE:
# a string (s) containing 'A' 'L' or 'P'

# CONSTRAINT:
# There is an award, but it can only be obtained if the student was absent for fewer than 2 days total > sounds like 1 absent only AND that student was not late for 3 or more consecutive days

# OUTPUT:
# I want to return TRUE if the student is eligible and False otherwise

# pseudo-code
# function that takes in string:
# def attendance(s):
# check the attendance for criteria: A only one time AND cannot have LLL
# if criteria met return True
# if not, return False

astring = "PPALLP"
astring2 = "PPALLL"
astring3 = "PAAPAL"

def attendance(s):
    a_count = 0
    for letter in s:
        if 'A' in letter:
            a_count += 1
    if a_count < 2 and 'LLL' not in s:
        return True
    else:
        return False
    
print(attendance(astring))
print(attendance(astring2))
print(attendance(astring3))

# same as code above but more condensed
def student_attendance(record):
    if record.count('A') < 2 and 'LLL' not in record:
        return True
    return False

print(student_attendance(astring))
print(student_attendance(astring2))
print(student_attendance(astring3))