import os
import tempfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="key that you want to store")
parser.add_argument("--value", help="value that you want to store for this key")

args = parser.parse_args()

print(args)

my_key = args.key
my_value = args.value

print(my_key)
print(my_value)

#print(args.echo)
#print(args.square**2)

#storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#with open(storage_path, 'w') as f:
#    pass
