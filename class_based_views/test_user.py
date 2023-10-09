# wrong
from django.contrib.auth.models import User

# correct
from django.contrib.auth import get_user_model

UserModel = get_user_model()
UserModel.object.create_user(
    username='bogi1',
    password='123',
)

