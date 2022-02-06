from django.contrib.auth.models import BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, mobile_num, password=None):
        if not mobile_num:
            raise ValueError('Users must have an mobile_num')

        user = self.model(
            mobile_num=mobile_num,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_num, password):
        user = self.create_user(
            mobile_num=mobile_num,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user