#This calculator is going to find the annual pretax earnings of someone's job 
#First we ask the user how much they make a hour and store that
hourly = input("How much money do you make a hour?")
#Then we print that variable to show the user
print(f'${hourly} per hour')
#We ask the user how many hours they work a week
hours_per_week = input("How many hours a week do you work?")
#Print that variable
print(f'{hours_per_week} a week')

#Do the calculation to find the annual pretax earnings
yearly_earnings = float(hourly) * float(hours_per_week) * 52

#Show the user the calculated annual earnings before any tax is taken out
print(f'Your annual income before tax is ${float(yearly_earnings)}!')