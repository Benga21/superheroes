from app import app
from database import db
from models import Hero, Power, HeroPower

with app.app_context():
    # This clears the existing data
    db.drop_all()
    db.create_all()

    # Add Heroes
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
        Hero(name="Carol Danvers", super_name="Captain Marvel"),
        Hero(name="Jean Grey", super_name="Dark Phoenix"),
        Hero(name="Ororo Munroe", super_name="Storm"),
        Hero(name="Kitty Pryde", super_name="Shadowcat"),
        Hero(name="Elektra Natchios", super_name="Elektra"),
    ]

    # Add Powers
    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
        Power(name="elasticity", description="can stretch the human body to extreme lengths"),
    ]

    db.session.add_all(heroes)
    db.session.add_all(powers)
    db.session.commit()

    # Add HeroPowers (relationship between heroes and powers)
    hero_powers = [
        HeroPower(hero_id=heroes[0].id, power_id=powers[1].id, strength="Strong"),  # Ms. Marvel - flight
        HeroPower(hero_id=heroes[1].id, power_id=powers[0].id, strength="Average"),  # Squirrel Girl - super strength
        HeroPower(hero_id=heroes[2].id, power_id=powers[2].id, strength="Strong"),  # Spider-Gwen - superhuman senses
        HeroPower(hero_id=heroes[3].id, power_id=powers[1].id, strength="Weak"),    # The Wasp - flight
        HeroPower(hero_id=heroes[4].id, power_id=powers[3].id, strength="Strong"),  # Scarlet Witch - elasticity
        HeroPower(hero_id=heroes[5].id, power_id=powers[1].id, strength="Strong"),  # Captain Marvel - flight
        HeroPower(hero_id=heroes[6].id, power_id=powers[0].id, strength="Strong"),  # Dark Phoenix - super strength
        HeroPower(hero_id=heroes[7].id, power_id=powers[1].id, strength="Strong"),  # Storm - flight
        HeroPower(hero_id=heroes[8].id, power_id=powers[2].id, strength="Weak"),    # Shadowcat - superhuman senses
        HeroPower(hero_id=heroes[9].id, power_id=powers[3].id, strength="Average"), # Elektra - elasticity
    ]

    db.session.add_all(hero_powers)
    db.session.commit()

    print("Seeding complete!")
