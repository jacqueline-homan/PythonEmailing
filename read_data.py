# Reading and writing to csv files in Python

import csv

ACCEPTED_MSG = """
Hi {},
We are thrilled to let you know that you are accepted to 
our programming workshop.

Your coach is {}.

Look forward to seeing you there!

Thank you, 
Workshop Organizers
"""

REJECTED_MSG = """
Hi {},
We are very sorry to let you know that due to 
the high number of applications, we could not
fit you into the workshop at this time.
We hope to see you next time.

Thank you, 
Workshop Organizers
"""

csv_file = open('/home/jacque/Desktop/applicants.csv')
for row in csv_file:
	print(row)

csv_file.close()


csv_file2 = open('/home/jacque/Desktop/applicants.csv')
csv_reader = csv.reader(csv_file2, delimiter=',')
for row in csv_reader:
	print(row)

csv_file2.close()


csv_file3 = open('/home/jacque/Desktop/applicants.csv')
csv_reader = csv.reader(csv_file3, delimiter=',')
next(csv_reader)

for row in csv_reader:
	name, email, accepted, coach, language = row 
	print(name, email, accepted, coach, language)
csv_file3.close()


csv_file4 = open('/home/jacque/Desktop/applicants.csv')
csv_reader = csv.reader(csv_file4, delimiter=',')
next(csv_reader)

for row in csv_reader:
	name, email, accepted, coach, language = row

	if accepted == "Yes":
		msg = ACCEPTED_MSG.format(name, coach)
	else:
		msg = REJECTED_MSG.format(name)

	print("Send email to: {}".format(email))
	print("Email content:")
	print(msg)

csv_file4.close()

# using `with` and `as`, we don't need the file.close() function
with open('/home/jacque/Desktop/applicants.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	next(csv_reader)

	for row in csv_reader:
		name, email, accepted, coach, language = row

		if accepted == "Yes":
			msg = ACCEPTED_MSG.format(name, coach)
		else:
			msg = REJECTED_MSG.format(name)

		print("Send email to: {}".format(email))
		print("Email content:")
		print(msg)


