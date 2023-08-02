from managers.user import UserManager
from models.user import User

user = User(name='Alvaro', last_name='Nieto', address='Alpargaterito', email='anieto687@gmail.com')
user.ranking = -1
user.admin = True

_id = UserManager.create_one(user)

print(_id)
# from querying.Filter import Filter, Operator
#
# _filter = Filter(field='_ranking', operator=Operator.greater, value=-1)
#
# user = UserManager.find(_filter)
#
# for u in user:
#     print(u)
