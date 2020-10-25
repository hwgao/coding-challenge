key_to_letters = {
    "1": "",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
    "0": " ",
}


def keypad_string(keys: str) -> str:
    '''
    Find the string that is created using a standard phone keypad
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
    >>> keypad_string("*")
    Traceback (most recent call last):
    ...
    AssertionError: Invalid key
    '''
    ret = ""
    i = 0
    while i < len(keys):
        assert ord("0") <= ord(keys[i]) and ord(
            keys[i]) <= ord("9"), "Invalid key"
        letters = len(key_to_letters[keys[i]])
        if len(keys) > i + 1 and keys[i] == keys[i+1] and letters > 1:
            if len(keys) > i + 2 and keys[i + 1] == keys[i+2] and letters > 2:
                if len(keys) > i + 3 and keys[i + 2] == keys[i+3] and letters > 3:
                    ret += key_to_letters[keys[i]][3]
                    i += 3
                else:
                    ret += key_to_letters[keys[i]][2]
                    i += 2
            else:
                ret += key_to_letters[keys[i]][1]
                i += 1
        else:
            if letters > 0:
                ret += key_to_letters[keys[i]][0]
        i += 1

    return ret
