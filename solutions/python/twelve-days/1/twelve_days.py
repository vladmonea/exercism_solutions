days_to_gifts = {
    1: {'day': 'first', 'gift': 'a Partridge in a Pear Tree'},
    2: {'day': 'second', 'gift': 'two Turtle Doves'},
    3: {'day': 'third', 'gift': 'three French Hens'},
    4: {'day': 'fourth', 'gift': 'four Calling Birds'},
    5: {'day': 'fifth', 'gift': 'five Gold Rings'},
    6: {'day': 'sixth', 'gift': 'six Geese-a-Laying'},
    7: {'day': 'seventh', 'gift': 'seven Swans-a-Swimming'},
    8: {'day': 'eighth', 'gift': 'eight Maids-a-Milking'},
    9: {'day': 'ninth', 'gift': 'nine Ladies Dancing'},
    10: {'day': 'tenth', 'gift': 'ten Lords-a-Leaping'},
    11: {'day': 'eleventh', 'gift': 'eleven Pipers Piping'},
    12: {'day': 'twelfth', 'gift': 'twelve Drummers Drumming'}
}



def recite(start_verse, end_verse):
    all_verses = []
    verse = "On the {} day of Christmas my true love gave to me: {}."
    for verse_number in range(start_verse, end_verse+1):
        day_and_gift = days_to_gifts[verse_number]
        gift_list = [days_to_gifts[vn]['gift'] for vn in range(1, verse_number + 1)]
        if len(gift_list) > 1:
            gifts = ', '.join(gift_list[:0:-1]) + ', and ' + gift_list[0]
        else:
            gifts = gift_list[0]

        all_verses.append(verse.format(day_and_gift['day'], gifts))
    return all_verses

