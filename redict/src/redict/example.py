from redict import redict

# set values
regular_dict = {'from_dict': 'using and dict', 'key': 'a key'} # using a dict or a compatible Iterable
rdict = redict(regular_dict, kargs1='using kargs value', kargs2='another kargs value') # add key and value as keyword argument
rdict.attribute = 'using attribute value' # using key as attribute
rdict.set('set', 'using set') # using set() method
rdict['dict'] = 'using dict() expression' # using set item expression

# get
print(rdict.key) # using key as attribute
print(rdict['key']) # using get item expression
print(rdict.get('key', 'default')) # using dict.get(key, default) as method, return the value or the default value
print(rdict.get.key('default')) # using key as method on redict.get attribute, return the value or the default value
print(rdict('key', 'default'))  # using redict as callable
