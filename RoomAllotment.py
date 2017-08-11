import sys


class Bidder:

	def __init__(self, name):
		self._name = name
		self._hasCleared = False;
		self._room_num = None

	def get_name(self):
		return self.name

	def match(self, room_num):
		self.hasCleared = True
		self.room_num = room_num

class Room:

	def __init__(self, number, rent):
		self._number = number
		self._rent = rent

	def increment(self, amount):
		self._rent += amount

	def get_rent(self):
		return self._rent

class Apartment:

	def __init__(self, num_rooms, rent, increment = 5):
		self.rooms = range(num_rooms)
		self.rent = range(num_rooms)
		self.increment = increment

		for i in range(num_rooms):
			self.rooms[i] += 1
			self.rent[i] = rent



	def updatePrices(self, bids):
		
		for i in range(bids):
			if len(bids[i])==0:
				self.rent[i] -= 5
			elif len(bids[i])==1:
				a = self.rent.pop(i)
				self.cleared + (i, a[0])
				self.bidders.remove(a[0])

			else:
				self.rent[i] += len(bids[i])*5


if  __name__ == "__main__":
	num_rooms = sys.argv[0]
	rent = sys.argv[1]
	apartment = Apartment(num_rooms, rent)
	occupants = []
	i = 0
	while i < num_rooms
		try:
			occupant = raw_input("Enter the name of bidder " + str(i+1) + ".")
			occupants[i] = Bidder(occupant)
			i+=1
		except TypeErrror:
			print "Only strings are accepted. Please type in the correct name."



