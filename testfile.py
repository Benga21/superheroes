import unittest
from app import create_app, db
from models import Hero, Power, HeroPower

class HeroesApiTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client and a fresh database for each test."""
        self.app = create_app('testing')  
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  
        self.app.config['TESTING'] = True
        
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()
            self.seed_database()

    def seed_database(self):
        """Create some initial data for testing."""
        power1 = Power(name='super strength', description='gives the wielder super-human strengths')
        power2 = Power(name='flight', description='gives the wielder the ability to fly through the skies at supersonic speed')
        
        hero1 = Hero(name='Kamala Khan', super_name='Ms. Marvel')
        hero2 = Hero(name='Gwen Stacy', super_name='Spider-Gwen')
        
        db.session.add(power1)
        db.session.add(power2)
        db.session.add(hero1)
        db.session.add(hero2)
        db.session.commit()

        #  this Creates hero powers
        hero_power1 = HeroPower(hero_id=hero1.id, power_id=power1.id, strength='Strong')
        hero_power2 = HeroPower(hero_id=hero2.id, power_id=power2.id, strength='Average')

        db.session.add(hero_power1)
        db.session.add(hero_power2)
        db.session.commit()

    def tearDown(self):
        """Clean up after each test."""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_heroes(self):
        """Test the GET /heroes endpoint."""
        response = self.client.get('/heroes')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Kamala Khan', response.data)
        self.assertIn(b'Gwen Stacy', response.data)

    def test_get_hero_by_id(self):
        """Test the GET /heroes/:id endpoint."""
        response = self.client.get('/heroes/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ms. Marvel', response.data)

    def test_get_power_by_id(self):
        """Test the GET /powers/:id endpoint."""
        response = self.client.get('/powers/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'super strength', response.data)

    def test_create_hero_power(self):
        """Test the POST /hero_powers endpoint."""
        response = self.client.post('/hero_powers', json={
            'strength': 'Average',
            'power_id': 1,
            'hero_id': 2
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Hero power created successfully', response.data)  

    def test_power_not_found(self):
        """Test handling of a non-existent power."""
        response = self.client.get('/powers/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Power not found', response.data)
if __name__ == '__main__':
    unittest.main()
