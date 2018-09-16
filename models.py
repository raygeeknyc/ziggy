import sys
from google.appengine.ext import ndb

DEFAULT_DELAY_SECONDS = 10
DEFAULT_TIMESTAMP = 1520985600000  # Midnight, 3/14/2018 

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

class _Delay(ndb.Model):
  seconds = ndb.IntegerProperty()

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
  def Save(cls, delay):
    cls.Delete()
    cls.Add(delay)

  @classmethod
  def Add(cls, delay):
    persisted_value = _Delay(seconds=delay)
    key = persisted_value.put()
    print("Added {}".format(key))

_Delay.Save(DEFAULT_DELAY_SECONDS)
_Timestamp.Save(DEFAULT_TIMESTAMP)
