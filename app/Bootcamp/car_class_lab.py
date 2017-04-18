class Car(object):
	"""A car class that can be used to instantiate various vehicles"""
	def __init__(self, car_type, model, name):
		if car_type:
			self.type = car_type
		if model:
			self.model = model
		else:
			self.model = 'GM'
		if name:
			self.name = name
		else:
			self.name = 'General'

		if self.type == 'koenigsegg' || self.type == 'Porsche':
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4

		if self.type == 'trailer':
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4
		self.speed = 0


	def is_saloon(self):
		if self.type != trailer:
			return True

	def drive(self, value):
		if self.title == 'trailer':
			speed = value*11
		else:
			speed = value*(1000/3)
		return Car()