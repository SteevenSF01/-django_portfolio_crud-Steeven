import django
django.setup()
# from hero_app import seed
# from about_app import seed
from skills_app import seed

if __name__ == '__main__':
    # seed.runHero()
    # seed.runAbout()
    seed.runSkills()