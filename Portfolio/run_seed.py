import django
django.setup()
from hero_app import seed

if __name__ == '__main__':
    seed.runHero()