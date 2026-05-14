def raindrops(number):
    raindrop_dict = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    raindrop = ''
    for num, drop in raindrop_dict.items():
        if number % num == 0:
            raindrop += drop
    if not raindrop:
        return str(number)
    return raindrop

