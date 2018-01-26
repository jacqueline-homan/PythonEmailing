class Applicant:

	def __init__(self, name, email, accepted, coach, language):
		self.name = name
		self.email = email 
		if accepted == "Yes": 
			self.accepted = True 
		else: 
			self.accepted = False 

		self.coach = coach
		self.language = language
		
	def say_hello(self):
		return "Hello"