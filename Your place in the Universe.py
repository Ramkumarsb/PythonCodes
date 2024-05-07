# Your place in the universe program
# This program will determine the approximate number of atoms that a person
# consists of and the percent of the universe that they comprise...

# initialization
num_atoms_universe = 10e80
weight_avg_person = 70 # i.e 70 kg (145 lbs)
num_atoms_avg_person = 70e27

# program greeting
print("This program will determine your place in the universe.")
print()

# prompt for user's weight
weight_lbs = int(input('Enter the weight in pounds: '))

# convert weight into kg
weight_kg = 2.2 * weight_lbs

# Determine number atoms in person
num_atoms = (weight_kg/70)*num_atoms_avg_person
percent_of_universe = (num_atoms/num_atoms_universe)*100

# display
print('Your approximate contain', format(num_atoms,'.2e'),'atoms')
print('Therefour you comprise', format(percent_of_universe,'.2e'),'% of the universe')
