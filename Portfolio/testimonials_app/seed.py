from django_seed import Seed
from testimonials_app.models import Testimonial


def runTestimonials():
    seeder = Seed.seeder()
    testimonial = [
        {
            'content': 'Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.',
            'client_name': 'Saul Goodman',
            'client_position': 'Ceo &amp; Founder',
            'image': 'img/testimonials/testimonials-1.jpg'
        },
        {
            'content': 'Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid cillum eram malis quorum velit fore eram velit sunt aliqua noster fugiat irure amet legam anim culpa.',
            'client_name': 'Sara Wilsson',
            'client_position': 'Designer',
            'image': 'img/testimonials/testimonials-2.jpg'
        },
        {
            'content': 'Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam duis minim tempor labore quem eram duis noster aute amet eram fore quis sint minim.',
            'client_name': 'Eric Sauvage',
            'client_position': 'Ceo &amp; Founder of Raciste & Co.',
            'image': 'img/testimonials/eric.jpg'
        },
        {
            'content': 'Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat minim velit minim dolor enim duis veniam ipsum anim magna sunt elit fore quem dolore labore illum veniam.',
            'client_name': 'Ariel Nasimba',
            'client_position': 'Ceo &amp; Founder of The Lion King',
            'image': 'img/testimonials/ariel.jpg'
        },
        {
            'content': 'Quis quorum aliqua sint quem legam fore sunt eram irure aliqua veniam tempor noster veniam enim culpa labore duis sunt culpa nulla illum cillum fugiat legam esse veniam culpa fore nisi cillum quid.',
            'client_name': 'John Larson',
            'client_position': 'Ceo &amp; Founder',
            'image': 'img/testimonials/testimonials-5.jpg'
        },
    ]
    for t in testimonial:
        seeder.add_entity(Testimonial, 1, t)
    pks = seeder.execute()
    print(pks, 'testimonial created')
