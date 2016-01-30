from project.models.user import User, UserFactory

uf = UserFactory()

admin = uf.getAdminUser()

users = [uf.getRegularUser() for i in range(5)]

user = users[0]
