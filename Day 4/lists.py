from os import stat


# create a list
states_of_australia = ["NSW", "TAS", "VIC", "NT", "WA", "SA", "QLD", "ACT"]

# change an entry in the list

states_of_australia[0] = "locked_NSW"

# append an item to the end of a list
states_of_australia.append("Mal's Place")

# extend a list with another list
states_of_australia.extend(
    ["Miller's", "Sydney Residence", "Korean Town House", "Farm House"])

print(states_of_australia)
