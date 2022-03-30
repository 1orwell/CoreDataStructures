import string
    # 1) build the map from keys to letters
    # 2) loop through the keys and add the corresponging letter
    # 3) taking into account keys pressed multiple times
'''
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |     #    |
    You can ignore 1, and 0 corresponds to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
'''

def get_key_to_letters():
    possible_letters = string.ascii_lowercase
    possible_keys = string.digits
    key_to_letters = {}
    start_index = 0
    for key in possible_keys:
        if key == '0':
            key_to_letters[key] = ' '
        elif key == '1':
            key_to_letters[key] = ''
        else:
            num_letters = 3
            if key in {'7', '9'}:
                num_letters = 4
            letters = possible_letters[start_index:start_index+num_letters]
            start_index += num_letters
            key_to_letters[key] = letters
    return key_to_letters



def keypad_string(keys):
    valid_keys = string.digits
    key_to_letters = get_key_to_letters()
    result = ""
    count = 0
    prev_key = ""
    for i, key in enumerate(keys):
        assert key in valid_keys, "Invalid key"
        if key == '1':
            pass
        else:
            # checking first key press
            if not prev_key:
                prev_key = key
                count = 1
            else: 
                # same key pressed
                if key == prev_key:
                    # pressed X times already
                    if len(key_to_letters[key]) == count:
                        result += key_to_letters[key][-1]
                        count = 1
                    else:
                        count += 1
                        # check if at end of word, need to add letter
                        if i == len(keys)-1:
                            result += key_to_letters[key][count-1]
                    # hasn't pressed X times
                # different key pressed
                else:
                    result += key_to_letters[prev_key][count-1]
                    count = 1
                    prev_key = key
    return result

print(keypad_string('2022'))
print(keypad_string('4433555555666'))