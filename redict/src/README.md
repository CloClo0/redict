# redict

`redict` is a Python library that extends the functionality of dictionaries, allowing you to access dictionary keys as attributes and providing additional methods for setting and retrieving values.

## Installation

Install the library using pip:

```bash
pip install redict
```

## Features

- Access dictionary keys as attributes.
- Add keys and values using keyword arguments during initialization.
- Set values using attributes, the `set()` method, or dictionary-style assignment.
- Retrieve values using attributes, the `get()` method, or dictionary-style item access.
- Use `redict.get.key(default)` for default retrieval when a key does not exist.

## Usage
### Importing `redict`
Two ways to import redict
```python
# using from-import statement
from redict import redict
rdict = redict(...)
```
Or
```python
# using import statement
import redict
rdict = redict.new(...)  # use the redict module method
# OR
rdict = redict.redict(...)  # use directly the class instantiation
```

### `redict` object argument
You can create a `redict` object from every valid object for dict() (see [dict() documentation](https://docs.python.org/3/library/stdtypes.html#dict)  for details ) and by providing keywords arguments
````python
from redict import redict

# Initialize with a dictionary (or every valid object valid in dict())
regular_dict = {'from_dict': 'using a dict', 'key': 'a key'}
rdict = redict(regular_dict, kargs1='using kargs value', kargs2='another kargs value')
````

### Setting values
Multiple ways exist:
```python
from redict import redict
rdict = redict()  # create redict object
rdict['key'] = 'value' # regular dict attribution
rdict.key = 'value'  # setting key as attribute
rdict.set('key', 'value')  # setting key using redict.set()
```
> **WARNING:**\
> You can **NOT** use reserved name as attribute key\
> You must use a valid attribute name to set a key as attribute\
> To create a value with a key which is a reserved name or an invalid attribute name, use `redict.set()`
> ```python
> from redict import redict
> rdict = redict()  # create redict object
> # invalid attribute name: `items` (because it's a redict method)
> rdict.set('items', 'value')
> # invalid attribute name: `spaced key`
> rdict.set('spaced key', 'value')
> ```

### Getting values
```python
from redict import redict
rdict = redict(key='value')  # create redict object with a single key 'key' associated to the value 'value'
print(rdict['key'])  # using regular dict getting, can raise a KeyError
print(rdict.key)  # using key as attribute, can raise an AttributeError
print(rdict.get('key', 'optional default'))  # using redict.get() to get value if exists, otherwise return the default value (None if no specified)
print(rdict.get.key('optional default'))  # using the key name as a function on the attribute redict.get, same result of rdict.get('key', 'optional result')
print(rdict('key', 'optional default'))  # call redict object passing the key and eventually a default value
```
> **WARNING:**\
> You can **NOT** use reserved name as attribute key\
> You must use a valid attribute name to get a key as attribute\
> To get a value with a key which is a reserved name or an invalid attribute name, use `redict.get()`
> ```python
> from redict import redict
> rdict = redict({'spaced key': 'value'}, items='value')  # create redict object
> # invalid attribute name: `items` (because it's a redict method)
> rdict.get('items')
> # invalid attribute name: `spaced key`
> rdict.get('spaced key')
> ```

## Additional Features
### Values Deletion
`redict` supports attribute deletion
```python
from redict import redict
rdict = redict(key = 'value', other_key = 'value', another_key='value')
del rdict.key # Can raise an Attribute error
# you can also use dict deletion statements
del rdict['other_value']
print(rdict.pop('another_key'))
...
```
### `redict` as a dict instance

`redict` supports every method and attributes of dict()
```python
# some examples
from redict import redict
rdict = redict()
print(rdict.items())
print(rdict.update({'other_dict': 'value'}))
...
```

can test if `redict` is a dict subclass or instance

```python
from redict import redict
print(issubclass(redict, dict))  # Output: True
print(isinstance(redict(), dict))  # Output: True

# if you want to make distinction between redict and dict
print(type(redict) is dict)  # Output: False
```
