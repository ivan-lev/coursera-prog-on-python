import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", help="key that you want to store")
parser.add_argument("-v", "--value", help="value that you want to store for this key")

args = parser.parse_args()

my_key = args.key
my_value = args.value

print(my_key)
print(my_value)

#print(args.echo)
#print(args.square**2)

#storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#with open(storage_path, 'w') as f:
#    pass
