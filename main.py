from managers.user import UserManager
from models.user import User
from querying.Filter import Filter, Operator

print('-----Playground------')

print('Create an user')
user = User(name='Cristiano', last_name='Ronaldo', address='Maderia', email='elbicho@gmail.com')
_id = UserManager.create_one(user)
print(_id)

print('Get an user by id')
user = UserManager.get(_id)
print(user)

print('Find one user by filter')
_filter = Filter(field='last_name', operator=Operator.equal, value='Ronaldo')
user = UserManager.find_one(_filter)
print(user)

print('Find many users by filter')
_filter = Filter(field='last_name', operator=Operator.not_equal, value='Ronaldo')
users = UserManager.find(_filter)
for _user in users:
    print(_user)

print('Create several users')
user1 = User(name='Killyan', last_name='Mbappe', address='Madrid', email='ratape@gmail.com')
user2 = User(name='Jude', last_name='Bellingham', address='Madrid', email='jude@gmail.com')
users_to_add = [user1, user2]
_ids = UserManager.create_many(users_to_add)
for _id in _ids:
    print(_id)

print('Update one user')
_filter = Filter(field='last_name', operator=Operator.equal, value='Ronaldo')
updated_values = {'_ranking': 3}
updated_result = UserManager.update_one(_filter, updated_values)
print(updated_result.modified_count)

print('Update many users')
_filter = Filter(field='last_name', operator=Operator.not_equal, value='Ronaldo')
updated_values = {'_ranking': 2}
updated_result = UserManager.update_many(_filter, updated_values)
print(updated_result.modified_count)

print('Delete one user')
_filter = Filter(field='last_name', operator=Operator.equal, value='Ronaldo')
updated_result = UserManager.delete_one(_filter)
print(updated_result.deleted_count)

print('Delete many user')
_filter = Filter(field='address', operator=Operator.equal, value='Madrid')
updated_result = UserManager.delete_many(_filter)
print(updated_result.deleted_count)
