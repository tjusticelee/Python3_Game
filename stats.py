#base stats
atk = 1
spd = 1
hp = 1

#skill points to spend
sp = 15

class create(object):

    def customize(self):

        print("""You have 15 skill points to spend in
        attack, speed, and hit points.""")

        #attack stats
        user_atk = int(input('atk: '))

        atk = atk + user_atk

        sp = sp - user_atk

        #speed stats
        user_spd = int(input('spd: '))

        spd = spd + user_spd

        sp = sp - user_spd

        #hitpoint stats
        user_hp = int(input('hp: '))

        hp = hp + user_hp

        sp = sp - user_hp


        print(f"""Current stats are:
        atk: {atk}

        spd: {spd}

        hp: {hp}""")


def advantages(user_atk, user_spd):

    #have this add a greater chance to do higher damage
    #This should possibly be a method
    if user_atk > 5:
        print('added damage')

    elif user_atk > 10:
        print('Super damage!')

    #This should increase the chance the user is able to dodge an attack
    if user_spd > 5:
        print('fast')

    if user_spd > 10:
        print('boi you got handles')
