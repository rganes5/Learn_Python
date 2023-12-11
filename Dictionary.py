monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversion["Nov"])
print(monthConversion["Jan"])
print(monthConversion["Oct"])
print(monthConversion.get("Docem", "Invalid key")) #This get keyword is cool

print(monthConversion)