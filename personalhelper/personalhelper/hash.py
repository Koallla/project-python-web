import hashlib
import pickle

s = hashlib.md5(pickle.dumps({'a':1})).hexdigest()
print(s)
