# Aaron Oviedo 1990958


roster={}
i=1

for i in range(0,5):

    jersey = int(input('Enter player {}\'s jersey number:\n' .format(i+1)))
    rating = int(input('Enter player {}\'s rating:\n' .format(i+1)))
    print()

    if jersey < 0 and jersey > 99 and rating < 0 and rating > 9:
        print('invalid entry')
        break
    else:
        roster[jersey] = rating

print("ROSTER")

for jersey,rating in sorted(roster.items()):
    print("Jersey number: %d, Rating: %d" % (jersey,rating))



command =''
while command !='q':

    menu = ('\nMENU\n'
          'a - Add player\n'
          'd - Remove player\n'
          'u - Update player rating\n'
          'r - Output players above a rating\n'
          'o - Output roster\n'
          'q - Quit\n')

    print(menu)
    command = input('Choose an option:\n')


    if command == 'a':
        jersey = int(input('Enter a new player\'s jersey number:\n' .format(i+1)))
        rating = int(input('Enter the players\'s rating:\n'.format(i+1)))
        roster[jersey] = rating

    elif command == 'd':
        jersey = int(input('Enter a jersey number:\n'))
        if jersey in roster.keys():
            del roster[jersey]


    elif command == 'u':

        jersey = int(input('Enter a jersey number:\n'))

        if jersey in roster.keys():

            rating = int(input('Enter a new rating for player:\n'))

            roster[jersey] = rating

    elif command== 'r':

        newrating =int(input('Enter a rating:\n'))

        print('ABOVE {}'.format(newrating))

        for jersey,rating in sorted(roster.items()):
            if rating > newrating:
                print("Jersey number: %d, Rating: %d" % (jersey,rating))


    elif command == 'o':

        print("ROSTER")
        for jersey,rating in sorted(roster.items()):
            print("Jersey number: %d, Rating: %d" % (jersey,rating))
