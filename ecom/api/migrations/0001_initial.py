from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="ilhosh",
                          email="hitshahbazi@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="123456789",
                          gender="Male"
                          )
        user.set_password("1qaz2wsx!QAZ@WSX")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]