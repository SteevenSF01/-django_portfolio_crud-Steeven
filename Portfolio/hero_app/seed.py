from django_seed import Seed
from hero_app.models import HeroModel



def runHero():
    seeder = Seed.seeder()
    seeder.add_entity(HeroModel, 1, {
        'name' : 'Steeven Salgado',
        'title' : 'freelance, affamé, the best'
    })

    pks = seeder.execute()
    print(pks)