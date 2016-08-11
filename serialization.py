import pickle
from main_menu import *

def serialize_users(file, obj):
  with open(file, 'wb+') as f:
    pickle.dump(obj, f)


