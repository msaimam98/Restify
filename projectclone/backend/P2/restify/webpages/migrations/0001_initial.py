# Generated by Django 4.2 on 2023-04-19 00:24

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields
import multiselectfield.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestifyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('host_or_not', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('phone_number', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('number_of_guest', models.PositiveIntegerField()),
                ('number_of_bed', models.PositiveIntegerField()),
                ('number_of_rooms', models.PositiveIntegerField()),
                ('baths', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('essentials', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('wifi', 'Wifi'), ('tv', 'TV'), ('kitchen', 'Kitchen'), ('workspace', 'Workspace'), ('air_conditioning', 'Air Conditioning'), ('heating', 'Heating'), ('washer', 'Washer'), ('dryer', 'Dryer')], max_length=63, null=True, validators=[multiselectfield.validators.MaxValueMultiFieldValidator(8)])),
                ('features', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('pool', 'Pool'), ('hot_tub', 'Hot Tub'), ('patio', 'Patio'), ('grill', 'Grill'), ('gym', 'Gym'), ('piano', 'Piano'), ('fire_pit', 'Fire Pit'), ('outdoor_shower', 'Outdoor Shower')], max_length=58, null=True, validators=[multiselectfield.validators.MaxValueMultiFieldValidator(8)])),
                ('location', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('lake_access', 'Lake Access'), ('beach_access', 'Beach Access'), ('skiin_skiout', 'Ski-in/Ski-out')], max_length=37, null=True, validators=[multiselectfield.validators.MaxValueMultiFieldValidator(8)])),
                ('safety_features', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('smoke_detector', 'Smoke Detector'), ('first_aid_kit', 'First Aid Kit'), ('fire_extinguisher', 'Fire Extinguisher')], max_length=46, null=True, validators=[multiselectfield.validators.MaxValueMultiFieldValidator(8)])),
                ('property_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'properties',
            },
        ),
        migrations.CreateModel(
            name='PropertyComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_on', models.DateTimeField(auto_now=True)),
                ('text_content', models.TextField()),
                ('reply', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_comment_author', to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='host_reservation_property', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RangePriceHostOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('price_per_night', models.PositiveBigIntegerField()),
                ('booked_for', models.BooleanField(default=False)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_for_available_date', to='webpages.property')),
            ],
            options={
                'verbose_name_plural': 'Available Ranges + Prices',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('posted_on', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(default=1)),
                ('num_of_guests', models.PositiveBigIntegerField(default=1)),
                ('status', models.CharField(choices=[('AR', 'Approval Request'), ('TE', 'Terminated'), ('AP', 'Approved'), ('DE', 'Denied'), ('CA', 'Cancelled'), ('CR', 'Cancellation Request'), ('CO', 'Completed')], default='AR', max_length=2)),
                ('available_date', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='date_booked_for', to='webpages.rangepricehostoffer')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_property', to='webpages.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restify_user_for_reservation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_on', models.DateTimeField(auto_now=True)),
                ('text_content', models.TextField(default=None)),
                ('rating', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='host_user_history', to=settings.AUTH_USER_MODEL)),
                ('reservation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation_user_history', to='webpages.reservation')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_user_history', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User History Comments',
            },
        ),
        migrations.CreateModel(
            name='RenterRequestNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webpages.propertycomment')),
            ],
        ),
        migrations.CreateModel(
            name='ReminderNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webpages.propertycomment')),
            ],
        ),
        migrations.CreateModel(
            name='RateNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webpages.propertycomment')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default=None, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_rating', to='webpages.property')),
                ('reservation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation_rating', to='webpages.reservation')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property_user_rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attribute_for_propimage', to='webpages.property')),
            ],
            options={
                'verbose_name_plural': 'Property Images',
            },
        ),
        migrations.AddField(
            model_name='propertycomment',
            name='reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_comments', to='webpages.reservation'),
        ),
        migrations.AddField(
            model_name='propertycomment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_reservation_property', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='OwnerRequestNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webpages.propertycomment')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.TextField(blank=True, null=True)),
                ('read', models.BooleanField(default=False)),
                ('notification_message', models.TextField(blank=True, null=True)),
                ('reservation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webpages.reservation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restify_user_notification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuestRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default=None, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('host_rater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='host_guest_rating', to=settings.AUTH_USER_MODEL)),
                ('reservation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation_guest_rating', to='webpages.reservation')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_guest_rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuestComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_on', models.DateTimeField(auto_now=True)),
                ('text_content', models.TextField()),
                ('reply', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_comment_author', to=settings.AUTH_USER_MODEL)),
                ('guest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guest_comments', to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='host_reservation_guest', to=settings.AUTH_USER_MODEL)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_guest_comments', to='webpages.reservation')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_reservation_guest', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webpages.propertycomment')),
            ],
        ),
    ]
