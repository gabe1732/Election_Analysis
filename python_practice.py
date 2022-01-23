counties = ['Arapahoe', 'Denver', 'Jefferson']
# if counties[1] == 'Denver':
#     print(counties[1])  
# temperature = int(input('what is the temperature outside? '))

# if temperature > 80:
#     print('Turn on the AC.')
# else:
#     print('Open the windows')
 
#  # what is the score?
# score = int(input('what is your test score? '))   
 
#  # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your score is a B')
# elif score >= 70:
#     print('Your score is a c')
# elif score >=60:
#     print('Your score is a D')
# else:
#     print('Your grade is an F')

# if "Arapahoe" in counties or 'El Paso' not in counties:
#     print('Arapahoe or El Paso is in the list of counties.')
# else:
#     print('Arapahoe or El Paso is not in the list of counties.')

# for county in counties:
#     print(county)
    
# for i in range(len(counties)):
#     print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county, voters in counties_dict.items():
#     print(county, voters)

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")