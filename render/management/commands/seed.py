# <project>/<app>/management/commands/seed.py
from django.core.management.base import BaseCommand
from render import models
from django.contrib.auth.models import User 

# ./manage.py seed --mode=clear
# ./manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    # logger.info("Delete Address instances")
    User.objects.all().delete()
    models.Message.objects.all().delete()


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return
    
    # >>>>>>>

    names = ["Винсет Вега", "Elon Musk", "Александр", "Мия Уоллес"]
    nics = ["@roizmangbn", "@elonmusk", "@sportsru", "@mia"]
    avatars = ["non_pyth"]
    emails = ["vvega@mail.com", "emusk@mail.com", "sport@mail.com", "mia@mail.com"]
    passwords = ['11111111']
    registr_times = ["2023-01-29T12:30:56.000000Z", "2023-01-29T12:31:56.000000Z", "2023-01-29T12:32:56.000000Z", "2023-01-29T12:33:56.000000Z"]

    text_messages = [
        "Hello friends! I’m writing message 1 here!",
        "Hello friends! I’m writing message 2 here!", 
        "Hello friends! I’m writing message 3 here!",
        "Hello friends! I’m writing message 4 here!",
        "Hello friends! I’m writing message 5 here!",
        "Hello friends! I’m writing message 1 here!",
        "Hello friends! I’m writing message 2 here!", 
        "Hello friends! I’m writing message 3 here!",
        "Hello friends! I’m writing message 4 here!",
        "Hello friends! I’m writing message 5 here!",
        "Hello friends! I’m writing message 1 here!",
        "Hello friends! I’m writing message 2 here!", 
        "Hello friends! I’m writing message 3 here!",
        "Hello friends! I’m writing message 4 here!",
        "Hello friends! I’m writing message 5 here!",
        "Hello friends! I’m writing message 1 here!",
        "Hello friends! I’m writing message 2 here!", 
        "Hello friends! I’m writing message 3 here!",
        "Hello friends! I’m writing message 4 here!",
        "Hello friends! I’m writing message 5 here!"
    ]

    images = ["non_pyth"]

    message_times = [
        "2024-01-29T12:34:01.000000Z",
        "2024-01-29T12:34:02.000000Z",
        "2024-01-29T12:34:03.000000Z",
        "2024-01-29T12:34:04.000000Z",
        "2024-01-29T12:34:05.000000Z",
        "2024-01-29T12:34:06.000000Z",
        "2024-01-29T12:34:07.000000Z",
        "2024-01-29T12:34:08.000000Z",
        "2024-01-29T12:34:09.000000Z",
        "2024-01-29T12:34:10.000000Z",
        "2024-01-29T12:34:11.000000Z",
        "2024-01-29T12:34:12.000000Z",
        "2024-01-29T12:34:13.000000Z",
        "2024-01-29T12:34:14.000000Z",
        "2024-01-29T12:34:15.000000Z",
        "2024-01-29T12:34:16.000000Z",
        "2024-01-29T12:34:17.000000Z",
        "2024-01-29T12:34:18.000000Z",
        "2024-01-29T12:34:19.000000Z",
        "2024-01-29T12:34:20.000000Z"
    ]

# ---
    
    for i in range(4):
        user = User(
            password = passwords[0],
            is_superuser = 0,
            username = nics[i],
            last_login = registr_times[i],
            email = emails[i],
            first_name = names[i].split()[0],
            last_name = names[i].split()[1] if ' ' in names[i] else '',
            is_staff = 0,
            is_active = 1,
            date_joined = registr_times[i],
        )
        user.save()
        print(user.id)

        for k in range(5):
            message = models.Message(
                text_message = text_messages[k],
                image = images[0],
                message_time = message_times[k],
                user = user
                )
            message.save()
