class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    #first we check if the user is present in the current group user list
    if user in group.get_users():
        return True
    
    #at this point user is not in current group i.e parent's group user list so we explore children group if any
    if len(group.get_groups()) > 0:
        for childGroup in group.get_groups():
            isInGroup = is_user_in_group(user,childGroup)
            #if user was found in child group we simply return early. no need to completely loop thorugh remaining groups
            if isInGroup == True:
                return True
    else:
        #user not found in user list and no child group to explore so we return false. user not found
        return False

    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

parent_user = "parent_user"
parent.add_user(parent_user)

child_user = "child_user"
child.add_user(child_user)

print(is_user_in_group(sub_child_user, sub_child))  # True
print(is_user_in_group(sub_child_user, child))  # True
print(is_user_in_group(sub_child_user, parent))  # True
print(is_user_in_group(parent_user, child))  # False
print(is_user_in_group(child_user, sub_child))  # False