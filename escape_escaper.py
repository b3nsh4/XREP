#removing \\ from dict

ta={}

target = ''.join(f'{{"{k}": "{v}"}}' for k,v in a.items())