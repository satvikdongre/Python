#lab 6b add ing(if thr add ly)
def string(s):
    if len(s)>2:
        if s[-3:]=='ing':
            s=s+'ly'
        else:
            s=s+'ing'
    return s
print(string('a'))
print(string('ab'))
print(string('abc'))
print(string('string'))
