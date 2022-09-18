#challenge 009
# Write a program then will ask for a number of
# days and then will show many hours,
# minutes and seconds are in that number of days.

nbr_days = int(input("enter number of days ? : "))
nbr_hours = nbr_days * 24
nbr_minuts = nbr_days * 24 * 60
nbr_seconds =nbr_days * 24 * 60 * 60
print("in ",nbr_days,"day(s) we have ", nbr_hours, "hours.")
print("in ",nbr_days,"day(s) we have ", nbr_minuts, "minuts.")
print("in ",nbr_days,"day(s) we have ", nbr_seconds, "seconds.")