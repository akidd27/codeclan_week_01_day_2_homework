stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append('Edinburgh Waverley')

#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0,'Glasgow Queen St')

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
polmont_index = stops.index('Falkirk High') + 1
stops.insert(polmont_index,'Polmont')

#4. Print out the index position of "Linlithgow"
print(stops.index('Linlithgow'))

#5. Remove "Livingston" from the list using its name
stops.remove('Livingston')

#6. Delete "Cumbernauld" from the list by index
cumbernauld_index = stops.index('Cumbernauld')
stops.pop(cumbernauld_index)

#7. Print the number of stops there are in the list
print(len(stops))

#8. Sort the list alphabetically
alphabetical_stops = sorted(stops)

#9. Reverse the positions of the stops in the list
rev_alphabetical_stops = sorted(stops, reverse = True)

#10 Print out all the stops using a for loop
for stop in stops:
    print(stop)
