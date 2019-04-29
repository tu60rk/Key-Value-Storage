import argparse
import os
import tempfile
import json

parser = argparse.ArgumentParser()
parser.add_argument('--key', help='display a value of key')
parser.add_argument('--value', help='add key and value in data')
args = parser.parse_args()

data = dict()
if args.key and args.value:
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'r')as f:
        #f.seek(0)
        a = f.read()
        f.close
    data = json.loads(a)

    if args.key in data:
        #data.setdefault(args.key,[])
        #data[args.key].append(args.value)
        values = list(data[args.key])
        values.append(args.value)
        data[args.key] = values
        print(data)
        #data[args.key]=list([args.value])
#data[args.key] = values
    else:
        data[args.key] = args.value

    with open(storage_path, 'r+')as f:
        f.write(json.dumps(data))
    print(data)
