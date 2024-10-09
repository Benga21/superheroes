from flask import jsonify, request
from models import Hero, Power, HeroPower  
from database import db

def configure_routes(app):
    @app.route('/heroes', methods=['GET'])
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([{'id': hero.id, 'name': hero.name, 'super_name': hero.super_name} for hero in heroes])

    @app.route('/heroes/<int:id>', methods=['GET'])
    def get_hero(id):
        hero = Hero.query.get(id)
        if hero:
            hero_data = {
                'id': hero.id,
                'name': hero.name,
                'super_name': hero.super_name,
                'powers': [{'id': hp.power_id, 'strength': hp.strength} for hp in hero.hero_powers]
            }
            return jsonify(hero_data)
        return jsonify({'error': 'Hero not found'}), 404

    @app.route('/powers', methods=['GET'])
    def get_powers():
        powers = Power.query.all()
        return jsonify([{'id': power.id, 'name': power.name, 'description': power.description} for power in powers])

    @app.route('/powers/<int:id>', methods=['GET'])
    def get_power(id):
        power = Power.query.get(id)
        if power:
            power_data = {'id': power.id, 'name': power.name, 'description': power.description}
            return jsonify(power_data)
        return jsonify({'error': 'Power not found'}), 404

    @app.route('/powers/<int:id>', methods=['PATCH'])
    def update_power(id):
        power = Power.query.get(id)
        if not power:
            return jsonify({'error': 'Power not found'}), 404

        data = request.json
        if 'description' in data:
            power.description = data['description']

        db.session.commit()
        return jsonify({'id': power.id, 'name': power.name, 'description': power.description})

    @app.route('/hero_powers', methods=['POST'])
    def create_hero_power():
        data = request.json
        hero_power = HeroPower(hero_id=data['hero_id'], power_id=data['power_id'], strength=data['strength'])
        db.session.add(hero_power)
        db.session.commit()
        return jsonify({'message': 'Hero power created successfully', 'hero_power': {'id': hero_power.id, 'hero_id': hero_power.hero_id, 'power_id': hero_power.power_id, 'strength': hero_power.strength}}), 201

    # New methods added here
    @app.route('/hero_powers', methods=['GET'])
    def get_hero_powers():
        hero_powers = HeroPower.query.all()
        return jsonify([{'id': hp.id, 'hero_id': hp.hero_id, 'power_id': hp.power_id, 'strength': hp.strength} for hp in hero_powers])

    @app.route('/hero_powers/<int:id>', methods=['GET'])
    def get_hero_power(id):
        hero_power = HeroPower.query.get(id)
        if hero_power:
            return jsonify({'id': hero_power.id, 'hero_id': hero_power.hero_id, 'power_id': hero_power.power_id, 'strength': hero_power.strength})
        return jsonify({'error': 'Hero power not found'}), 404

    # DELETE routes
    @app.route('/heroes/<int:id>', methods=['DELETE'])
    def delete_hero(id):
        hero = Hero.query.get(id)
        if hero:
            db.session.delete(hero)
            db.session.commit()
            return jsonify(message=f"Hero with id {id} deleted."), 
        return jsonify(error="Hero not found."), 404

    @app.route('/powers/<int:id>', methods=['DELETE'])
    def delete_power(id):
        power = Power.query.get(id)
        if power:
            db.session.delete(power)
            db.session.commit()
            return jsonify(message=f"Power with id {id} deleted."), 
        return jsonify(error="Power not found."), 404

    @app.route('/hero_powers/<int:id>', methods=['DELETE'])
    def delete_hero_power(id):
        hero_power = HeroPower.query.get(id)
        if hero_power:
            db.session.delete(hero_power)
            db.session.commit()
            return jsonify(message=f"Hero power with id {id} deleted."), 
        return jsonify(error="Hero power not found."), 404