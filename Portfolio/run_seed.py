import django
django.setup()
from hero_app import seed as seed_hero
from about_app import seed as seed_about
from skills_app import seed as seed_skill
from portfolio_app import seed as seed_portfolio

if __name__ == '__main__':
    # seed_hero.runHero()
    # seed_about.runAbout()
    # seed_skill.runSkills()
    seed_portfolio.runPortfolio()