month = "january" , "february", "march", "Arpil", "may", "june", "july", "aguest", "september", "october","november" , "december"
birthday = input("type your date of birth in (DD-MM-YYYY ) :")
index = int(birthday[3:5])
print("your birth month is ", month[index-1])