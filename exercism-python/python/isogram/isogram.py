def is_isogram(string):
    if string:
        temp = string.replace(' ', '').replace('-', '')
        string = set(list(temp.lower()))
        if len(temp) != len(string):
            return False
        else:
            return True
    else:
        return True
