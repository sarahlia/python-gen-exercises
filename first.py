def remove(s):
    s = s.replace('!', '')
    s += '!'

    return s
#
#
# alternative way
# def remove(s):
#     s = s.split('!')
#     s = ('').join(s) + ('!')
#
#     return s
#
print(remove('Hel!lo! world!!'))
print(remove('sa!!rah !lia nai!ng!!!golan'))