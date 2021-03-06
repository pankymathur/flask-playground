from werkzeug.security import safe_str_cmp
from user import User


# # users = [
# #     {
# #         'id':1,
# #         'username': 'bob',
# #         'password': 'asdf'
# #
# #     }
# # ]
#
# # pythonic way
# users = [
#         User(1,'bob', 'asdf')
# ]
#
# # username_mapping = {
# #     'bob': {
# #         'id':1,
# #         'username': 'bob',
# #         'password': 'asdf'
# #
# #     }
# # }
#
# # pythonic way
# username_mapping = {u.username: u for u in users}
#
#
# # userid_mapping = {
# #     1: {
# #         'id':1,
# #         'username': 'bob',
# #         'password': 'asdf'
# #
# #     }
# # }
#
# # pythonic way
# userid_mapping = {u.id: u for u in users}


# now let's make authenticate function

def authenticate(username, password):
    # list based data
    # user = username_mapping.get(username, None)
    # sqlite baed data
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

# create identity function
def identity(payload):
    user_id = payload['identity']
    # list based data
    # return userid_mapping.get(user_id, None)
    # sqlite baed data
    return User.find_by_id(user_id)
