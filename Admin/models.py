from django.db import models

# Create your models here.
import json
import string
import random

from django.contrib.auth.models import AbstractUser
from django.db import models




# Create your models here.
USER_TYPE_CHOICES=[
    ("USER","user"),
    ("Admin","admin"),
    ("EventTeam","eventteam"),
    ("Pending","pending"),
    ("CameraMan","cameraman"),
    ("Rejected","rejected"),
    ("MakeupArtist","makeupartist")
    

]
STATUS_CHOICES={
    ("ACTIVE","Active"),
    ("DEACTIVE","Inactive"),
}
class LoginTable(AbstractUser):
    #username
    #password
    #first_name
    #last_name
    #email
    # otp= models.CharField(max_length=20,null=True,blank=True)
    status = models.CharField(max_length=20,null=True,choices=STATUS_CHOICES)
    is_active = models.CharField(max_length=20,null=True,blank=True,default=True)
    user_type=models.CharField(max_length=20,null=True,choices=USER_TYPE_CHOICES)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
       
          return f"{self.id}"

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='userprofile_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='userprofile_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    


class Token(models.Model):
    key = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(
        LoginTable,
        related_name="auth_tokens",
        on_delete=models.CASCADE,
        verbose_name="user",
        unique=True,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    session_dict = models.TextField(null=False, default="{}")

    def generate_key(self):
        """Generate a random key for the token."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=40))

    def read_session(self):
        """Read session data from the session_dict attribute."""
        try:
            self.data_dict = json.loads(self.session_dict)
        except json.JSONDecodeError:
            self.data_dict = {}

    def write_back(self):
        """Write session data back to the session_dict attribute."""
        self.session_dict = json.dumps(self.data_dict)
        self.save()

    def get(self, key, default=None):
        """Get a value from the session data."""
        self.read_session()
        return self.data_dict.get(key, default)

    def set(self, key, value, save=True):
        """Set a value in the session data."""
        self.read_session()
        self.data_dict[key] = value
        if save:
            self.write_back()

    def update_session(self, tdict, save=True, clear=False):
        """Update session data with the provided dictionary."""
        self.read_session()
        if clear:
            self.data_dict = tdict
        else:
            self.data_dict.update(tdict)
        if save:
            self.write_back()

    def save(self, *args, **kwargs):
        """Override the save method to generate a key if not provided."""
        if not self.key:
            self.key = self.generate_key()
        super().save(*args, **kwargs)

    def str(self):
        """Return a string representation of the token."""
        return str(self.user) if self.user else str(self.id)
    


    
