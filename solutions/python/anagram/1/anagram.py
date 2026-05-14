def find_anagrams(word, candidates):
    results = []
    for candidate in candidates:
        if len(candidate) == len(word) and candidate.lower() != word.lower():
            if sorted(word.lower()) == sorted(candidate.lower()):
                results.append(candidate)
    return results

