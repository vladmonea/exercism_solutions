def hey(phrase):
    phrase = phrase.strip()
    if len(phrase) == 0:
        return 'Fine. Be that way!'
    if not phrase.isupper() and phrase[-1] == '?':
        return 'Sure.'
    if phrase.isupper():
        if phrase[-1] == '?':
            return 'Calm down, I know what I\'m doing!'
        return 'Whoa, chill out!'
    return 'Whatever.'