from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self, first_name, email, last_name, password):
		if not first_name:
			raise ValueError('user must have first name')

		if not email:
			raise ValueError('user must have email')

		if not last_name:
			raise ValueError('user must have last name')

		user = self.model(first_name=first_name, email=self.normalize_email(email), last_name=last_name)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, first_name, email, last_name, password):
		user = self.create_user(first_name, email, last_name, password)
		user.is_admin = True
		user.is_superuser = True
		user.save(using=self._db)
		return user
