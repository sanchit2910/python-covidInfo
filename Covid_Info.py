from covid import Covid
covid = Covid()
print("Total active cases in world:", covid.get_total_active_cases())
print("Total recovered cases in world:", covid.get_total_recovered())
print("Total deaths in world:", covid.get_total_deaths())
# getting data according to country name
# data will be stored as a dictionary
# print(covid.list_countries()) 
cases = covid.get_status_by_country_name("india")
# printing country's data using for loop
for x in cases:
    print(x, ":", cases[x])
