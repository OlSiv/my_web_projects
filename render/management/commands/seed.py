# <project>/<app>/management/commands/seed.py
from django.core.management.base import BaseCommand
from render import models

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
    models.User.objects.all().delete()
    models.Message.objects.all().delete()


def create_user(zn):
    """Creates an address object combining different elements from the list"""

    names = ["Anri", "Бобби", "Cindy", "Dan"]
    nics = ["@anri", "@bobby", "@cindy", "@dan"]
    avatars = ["non_pyth"]
    emails = ["anri@mail.com", "bobby@mail.com", "cindy@mail.com", "dan@mail.com"]
    passwords = ['11111111']
    registr_times = ["2023-01-29T12:30:56.000000Z", "2023-01-29T12:31:56.000000Z", "2023-01-29T12:32:56.000000Z", "2023-01-29T12:33:56.000000Z"]


    user = models.User(
        name = names[zn],
        nic = nics[zn],
        avatar = avatars[0],
        email = emails[zn],
        password = passwords[0],
        registr_time = registr_times[zn]
    )
    user.save()
    return user 


def create_message(zn, us):
    """Creates an address object combining different elements from the list"""

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
    

    message = models.Message(
        text_message = text_messages[zn],
        image = images[0],
        message_time = message_times[zn],
        uuser = user
    )
    message.save()
    # logger.info("{} users created.".format(users))
    # return message


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return


    # Creating addresses
    for i in range(4):
        user = create_user(i)
        create_message(k, user) 
        # create_user(i)


    # Creating addresses
    for k in range(20):





    # ???????????????????????????????
    # связи, ORM



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 
# # <project>/<app>/management/commands/seed.py
# from django.core.management.base import BaseCommand
# # import random

# # python manage.py seed --mode=refresh

# """ Clear all data and creates addresses """
# MODE_REFRESH = 'refresh'

# """ Clear all data and do not create any object """
# MODE_CLEAR = 'clear'

# class Command(BaseCommand):
#     help = "seed database for testing and development."

#     def add_arguments(self, parser):
#         parser.add_argument('--mode', type=str, help="Mode")

#     def handle(self, *args, **options):
#         self.stdout.write('seeding data...')
#         run_seed(self, options['mode'])
#         self.stdout.write('done.')


# def clear_data():
#     """Deletes all the table data"""
#     logger.info("Delete Address instances")
#     Address.objects.all().delete()


# def create_address():
#     """Creates an address object combining different elements from the list"""
#     logger.info("Creating address")
#     street_flats = ["#221 B", "#101 A", "#550I", "#420G", "#A13"]
#     street_localities = ["Bakers Street", "Rajori Gardens", "Park Street", "MG Road", "Indiranagar"]
#     pincodes = ["101234", "101232", "101231", "101236", "101239"]

#     address = Address(
#         street_flat=random.choice(street_flats),
#         street_locality=random.choice(street_localities),
#         pincode=random.choice(pincodes),
#     )
#     address.save()
#     logger.info("{} address created.".format(address))
#     return address

# def run_seed(self, mode):
#     """ Seed database based on mode

#     :param mode: refresh / clear 
#     :return:
#     """
#     # Clear data from tables
#     clear_data()
#     if mode == MODE_CLEAR:
#         return

#     # Creating 15 addresses
#     for i in range(15):
#         create_address()
        
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# # <project>/<app>/management/commands/seed.py
# from django.core.management.base import BaseCommand
# from render import models

# # ./manage.py seed --mode=clear
# # ./manage.py seed --mode=refresh

# class Command(BaseCommand):
#     help = "seed database for testing and development."

#     def add_arguments(self, parser):
#         parser.add_argument('--mode', type=str, help="Mode")

#     def handle(self, *args, **options):
#         # self.stdout.write('seeding data...')
#         run_seed(self, options['mode'])
#         # self.stdout.write('done.')


# def run_seed(self, mode):
#     """ Seed database based on mode

#     :param mode: refresh / clear 
#     :return:
#     """
#     print('Hello')
    
#     for _ in range(4):

#         user = models.User(
#             name = 'Evgen',
#             registr_time = "2024-01-29T12:34:01.000000Z"
#         )
#         user.save()
#         print(user.id)

#         for _ in range(5):
#                 message = models.Message(
#                     text_message = "1",
#                     message_time = "2024-01-29T12:34:20.000000Z",
#                     image = '1',
#                     uuser = user
                
#                 )
#                 message.save()
