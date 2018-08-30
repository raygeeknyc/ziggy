import sys
from google.appengine.ext import ndb

class _Timestamp(ndb.Model):
  datetime = ndb.IntegerProperty()

  @classmethod
  def Delete(cls):
    print("Deleting {}".format(cls.__name__))
    all_instances = cls.query()
    instance_count = 0
    for key in all_instances.iter(keys_only=True):
      print("Deleting {}".format(key))
      key.delete()
      instance_count += 1
    print("Deleted {} of {}".format(instance_count, cls.__name__))
 
  @classmethod
  def Get(cls):
    print("Finding all {}".format(cls.__name__))
    instance_query = cls.query()
    instances = instance_query.iter()
    entities = []
    for instance in instances:
      entities.append(instance)
      print("found: {}".format(instance))
    print("Found {} instances".format(len(entities)))
    if entities:
      return entities[0]
    else:
      return None

  @classmethod
  def Save(cls, timestamp):
    cls.Delete()
    cls.Add(timestamp)

  @classmethod
  def Add(cls, timestamp):
    persisted_value = _Timestamp(datetime=timestamp)
    key = persisted_value.put()
    print("Added {}".format(key))
