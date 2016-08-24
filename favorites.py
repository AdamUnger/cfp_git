

def main():
	favorite_musicians = {
		'Adam': 'The Beatles',
	}

	for person, musician in favorite_musicians.items():
		print "{person}'s favorite musician is {musician}".format(person=person, musician=musician)

main()