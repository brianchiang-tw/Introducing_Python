from collections import defaultdict

def no_idea():
    return 'Huh?'

animal_sound = defaultdict( no_idea )

animal_sound['dog'] = 'bark'
animal_sound['cat'] = 'meow'