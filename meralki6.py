
import json
d='{"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}'
python_string=json.loads(d)
print(python_string)
print(type(python_string))


# Unique Key in a JSON object:-
# {'a': 4, 'b': 2}
