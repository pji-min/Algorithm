def solution(babbling):
    valid_sounds = ["aya", "ye", "woo", "ma"]
    count = 0

    def can_pronounce(word, used):
        if not word:
            return True
        for sound in valid_sounds:
            if sound in used:
                continue
            if word.startswith(sound):
                if can_pronounce(word[len(sound):], used + [sound]):
                    return True
        return False

    for word in babbling:
        if can_pronounce(word, []):
            count += 1

    return count