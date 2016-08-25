

def main():
	favorite_musicians = {
		'Adam': 'The Beatles',
		'Clyon': 'Zinc Fence Redemption/ Chronixx',
		'Tina': 'Maxwell',
		'Ronesha': 'B2K',
	}

	for person, musician in favorite_musicians.items():
		print "{person}'s favorite musician is {musician}".format(person=person, musician=musician)

main()
