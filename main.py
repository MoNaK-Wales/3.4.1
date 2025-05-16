import django_setup
from users.models import User, Role, Group


admins = Role.objects.get(name='admin')
users = Role.objects.get(name='user')

group1 = Group.objects.get(name='group1')
group2 = Group.objects.get(name='group2')

user1 = User.objects.get(name='Jake')
user2 = User.objects.get(name='John')
user3 = User.objects.get(name='Jane')
user4 = User.objects.get(name='Jill')

while True:
    choice = input('1. Change user role\n2. Add user to group\n3. Exit\n')

    if choice == '1':
        name = input('Enter user name: ')
        user = User.objects.filter(name=name).first()
        
        if user:
            if user.role == admins:
                user.role = users
            else:
                user.role = admins
            user.save()
        
    elif choice == '2':
        name = input('Enter user name: ')
        user = User.objects.filter(name=name).first()
        
        if user:
            group_name = input('Enter group name: ')
            group = Group.objects.filter(name=group_name).first()
            
            if group:
                user.groups.add(group)
                user.save()
    
    elif choice == '3':
        break

print("Admins:", admins.users.all())
print("Users:", users.users.all())
print("Group1:", group1.users.all())
print("Group2:", group2.users.all())