"""Take the string representing the date and time and converts it to a date time object"""

from dateutil import parser
"""Brings a bunch of class and function to the code"""
start = '9/01/24 1:30 PM ' 
end  = '9/01/24 3:32 PM '    
start_date = parser.parser(start)
End_date = parser.parser(end)
"""Type is datetime.datetime"""
print(f'type of start date {type(start_date)}')
# it makes the date and time easy
print(End_date - start_date)