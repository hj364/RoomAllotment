class Bidder:

	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name



class Apartment:

	def __init__(self, num_rooms, rent, bidders = [], increment = 5):
		self.rooms = range(num_rooms)
		self.rent = range(num_rooms)
		self.numBids = range(num_rooms)
		self.increment = increment
		self.bidders = bidders
		for i in range(num_rooms):
			self.rooms[i] += 1
			self.rent[i] = rent
			self.numBids[i] = 0


	def updatePrices(self, bids):
		
		for i in range(bids):
			if(len(bids[i])==0):
				self.rent[i] -= 5
			elif(len(bids[i])==1):
				a = self.rent.pop(i)
				self.cleared + (i, a[0])
				self.bidders.remove(a[0])

			else:
				self.rent[i] += len(bids[i])*5

	