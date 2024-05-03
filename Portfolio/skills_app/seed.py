from django_seed import Seed
from skills_app.models import Skill

def runSkills():
    seeder = Seed.seeder()
    skills = [
        {'name': 'HTML', 'proficiency' : 100},
        {'name': 'CSS', 'proficiency' : 90},
        {'name': 'JAVASCRIPT', 'proficiency' : 75},
        {'name': 'PHP', 'proficiency' : 5},
        {'name': 'WORDPRESS/CMS', 'proficiency' : 30},
        {'name': 'PHOTOSHOP', 'proficiency' : 60},
    ]
    for skill_data in skills:
        seeder.add_entity(Skill, 1, skill_data)
    pks = seeder.execute()
    print(pks)
