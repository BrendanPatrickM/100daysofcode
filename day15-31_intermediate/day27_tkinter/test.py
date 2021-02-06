def find_short(s):
    l =  min(s.split(), key=len)
    return l # l: shortest word length

print(find_short("bitcoin take over the world maybe who knows perhaps"))