import django
django.setup()
from hero_app import seed as seed_hero
from about_app import seed as seed_about
from skills_app import seed as seed_skill
from portfolio_app import seed as seed_portfolio
from services_app import seed as seed_services
from testimonials_app import seed as seed_testimonials

if __name__ == '__main__':
    # seed_hero.runHero()
    # seed_about.runAbout()
    # seed_skill.runSkills()
    # seed_portfolio.runPortfolio()
    # seed_services.runServices()
    seed_testimonials.runTestimonials()