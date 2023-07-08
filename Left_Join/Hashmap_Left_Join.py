def left_join(synonyms, antonyms):
    result = {}

    for key in synonyms:
        if key in antonyms:
            result[key] = (synonyms[key], antonyms[key])
        else:
            result[key] = (synonyms[key], None)

    return result
