# tuple.py
# Create a tuple that stores the months of the year, from that tuple create 
# another tuple with just the summer months (May, June, July), print out the 
# summer months one at a time.
# Author: Finbar Dennehy

# create a tuple that stores months of the year
months = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
# create tuple with subset of summer months
summer_months = months[4:7]

# loop through the summer months and print each one
for month in summer_months:
    print(month)