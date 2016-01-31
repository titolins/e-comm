from project.models.user import User, UserFactory
from project.models.category import Category, CategoryFactory

## users
uf = UserFactory()
admin = uf.getAdminUser()
users = [uf.getRegularUser() for i in range(5)]
user = users[0]


## categories
cf = CategoryFactory()
categories = cf.getCategories()
