from django_seed import Seed
from about_app.models import Profile



def runAbout():
    seeder = Seed.seeder()
    seeder.add_entity(Profile, 1, {
        'birthday' : '1 May 1995',
        'website' : 'www.example.com',
        'phone':'+123 456 7890',
        'city':'New York, USA',
        'age': '30',
        'degree': 'Master',
        'email': 'email@example.com',
        'freelance' : True
    })

    pks = seeder.execute()
    print(pks)