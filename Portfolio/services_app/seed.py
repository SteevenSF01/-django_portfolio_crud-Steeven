from django_seed import Seed
from services_app.models import Service

def runServices():
    seeder = Seed.seeder()
    services = [
        {'title': 'Lorem Ipsum', 'icon':'bi bi-briefcase','description':'Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident'},
        {'title': 'Magni Dolores', 'icon':'bi bi-binoculars','description':'Excepteur sint occaecat cupidatat non proident, sun in culpa qui officia deserunt mollit anim id est laborum'},
        {'title': 'Dolor Sitema', 'icon':'bi bi-card-checklist','description':'Minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat tarad limino ata'},
        {'title': 'Sed ut perspiciatis', 'icon':'bi bi-bar-chart','description':' Duis aute irure dolor in reprehenderit in voluptate velit esse cillum  dolore eu fugiat nulla pariatur'},
        {'title': 'Nemo Enim', 'icon':'bi bi-brightness-high','description':'At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque'},
        {'title': 'Eiusmod Tempor', 'icon':'bi bi-calendar4-week','description':'Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi'},
    ]
    
    for service in services :
        seeder.add_entity(Service,1,service)
    pks = seeder.execute()
    print(pks , 'services created')