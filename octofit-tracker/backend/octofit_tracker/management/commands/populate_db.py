from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data cleared'))
        
        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Avengers assemble! The mightiest heroes on Earth unite for fitness.'
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League unite! Protecting the world through strength and fitness.'
        )
        
        self.stdout.write(self.style.SUCCESS(f'Created teams: {team_marvel.name}, {team_dc.name}'))
        
        # Create Users - Marvel Heroes
        self.stdout.write('Creating Marvel heroes...')
        iron_man = User.objects.create(
            name='Tony Stark',
            email='ironman@marvel.com',
            password='arc_reactor_3000',
            team_id=str(team_marvel._id)
        )
        
        captain_america = User.objects.create(
            name='Steve Rogers',
            email='capamerica@marvel.com',
            password='vibranium_shield',
            team_id=str(team_marvel._id)
        )
        
        black_widow = User.objects.create(
            name='Natasha Romanoff',
            email='blackwidow@marvel.com',
            password='red_room_trained',
            team_id=str(team_marvel._id)
        )
        
        thor = User.objects.create(
            name='Thor Odinson',
            email='thor@marvel.com',
            password='mjolnir_worthy',
            team_id=str(team_marvel._id)
        )
        
        hulk = User.objects.create(
            name='Bruce Banner',
            email='hulk@marvel.com',
            password='gamma_radiation',
            team_id=str(team_marvel._id)
        )
        
        # Create Users - DC Heroes
        self.stdout.write('Creating DC heroes...')
        batman = User.objects.create(
            name='Bruce Wayne',
            email='batman@dc.com',
            password='dark_knight_rises',
            team_id=str(team_dc._id)
        )
        
        superman = User.objects.create(
            name='Clark Kent',
            email='superman@dc.com',
            password='kryptonian_power',
            team_id=str(team_dc._id)
        )
        
        wonder_woman = User.objects.create(
            name='Diana Prince',
            email='wonderwoman@dc.com',
            password='amazonian_warrior',
            team_id=str(team_dc._id)
        )
        
        flash = User.objects.create(
            name='Barry Allen',
            email='flash@dc.com',
            password='speed_force_fastest',
            team_id=str(team_dc._id)
        )
        
        aquaman = User.objects.create(
            name='Arthur Curry',
            email='aquaman@dc.com',
            password='atlantis_king',
            team_id=str(team_dc._id)
        )
        
        marvel_heroes = [iron_man, captain_america, black_widow, thor, hulk]
        dc_heroes = [batman, superman, wonder_woman, flash, aquaman]
        all_heroes = marvel_heroes + dc_heroes
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_heroes)} heroes'))
        
        # Create Activities
        self.stdout.write('Creating hero activities...')
        activity_types = ['Running', 'Weightlifting', 'Swimming', 'Cycling', 'Boxing', 'Yoga', 'HIIT']
        
        activities_data = [
            # Marvel Activities
            {'user': iron_man, 'type': 'Weightlifting', 'duration': 60, 'calories': 400, 'distance': 0, 'notes': 'Building the next Iron Man suit requires strength'},
            {'user': captain_america, 'type': 'Running', 'duration': 45, 'calories': 500, 'distance': 10, 'notes': 'Morning run around the shield facility'},
            {'user': black_widow, 'type': 'Boxing', 'duration': 50, 'calories': 450, 'distance': 0, 'notes': 'Sparring with Hawkeye'},
            {'user': thor, 'type': 'Weightlifting', 'duration': 90, 'calories': 800, 'distance': 0, 'notes': 'Lifting Mjolnir and other heavy objects'},
            {'user': hulk, 'type': 'HIIT', 'duration': 30, 'calories': 600, 'distance': 0, 'notes': 'Smash training session'},
            
            # DC Activities
            {'user': batman, 'type': 'Boxing', 'duration': 70, 'calories': 600, 'distance': 0, 'notes': 'Cave training with Robin'},
            {'user': superman, 'type': 'Running', 'duration': 20, 'calories': 300, 'distance': 50, 'notes': 'Quick flight around Metropolis'},
            {'user': wonder_woman, 'type': 'Weightlifting', 'duration': 55, 'calories': 500, 'distance': 0, 'notes': 'Themyscira training routine'},
            {'user': flash, 'type': 'Running', 'duration': 15, 'calories': 700, 'distance': 100, 'notes': 'Speed force sprint'},
            {'user': aquaman, 'type': 'Swimming', 'duration': 60, 'calories': 550, 'distance': 20, 'notes': 'Patrolling Atlantis waters'},
        ]
        
        for i, activity_data in enumerate(activities_data):
            Activity.objects.create(
                user_id=str(activity_data['user']._id),
                activity_type=activity_data['type'],
                duration=activity_data['duration'],
                calories=activity_data['calories'],
                distance=activity_data['distance'],
                date=datetime.now() - timedelta(days=i),
                notes=activity_data['notes']
            )
        
        # Add more random activities
        for hero in all_heroes:
            for _ in range(random.randint(3, 7)):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 90)
                calories = random.randint(200, 800)
                distance = random.uniform(0, 20) if activity_type in ['Running', 'Cycling', 'Swimming'] else 0
                
                Activity.objects.create(
                    user_id=str(hero._id),
                    activity_type=activity_type,
                    duration=duration,
                    calories=calories,
                    distance=round(distance, 2),
                    date=datetime.now() - timedelta(days=random.randint(0, 30))
                )
        
        self.stdout.write(self.style.SUCCESS(f'Created {Activity.objects.count()} activities'))
        
        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard...')
        for hero in all_heroes:
            user_activities = Activity.objects.filter(user_id=str(hero._id))
            total_calories = sum([act.calories for act in user_activities])
            total_distance = sum([act.distance for act in user_activities if act.distance])
            total_activities = user_activities.count()
            
            team = team_marvel if hero.team_id == str(team_marvel._id) else team_dc
            
            Leaderboard.objects.create(
                user_id=str(hero._id),
                user_name=hero.name,
                team_id=str(team._id),
                team_name=team.name,
                total_calories=total_calories,
                total_activities=total_activities,
                total_distance=round(total_distance, 2)
            )
        
        # Update ranks
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_calories')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()
        
        self.stdout.write(self.style.SUCCESS(f'Created leaderboard with {Leaderboard.objects.count()} entries'))
        
        # Create Workouts
        self.stdout.write('Creating workout suggestions...')
        workouts = [
            {
                'name': 'Arc Reactor Core',
                'description': 'Build an iron core like Tony Stark',
                'activity_type': 'Weightlifting',
                'difficulty': 'Advanced',
                'duration': 45,
                'calories': 400,
                'instructions': '1. Warm-up: 5 min\n2. Bench press: 4x10\n3. Deadlifts: 4x8\n4. Core exercises: 3x15\n5. Cool down: 5 min'
            },
            {
                'name': 'Super Soldier Stamina',
                'description': 'Train like Captain America',
                'activity_type': 'Running',
                'difficulty': 'Intermediate',
                'duration': 40,
                'calories': 450,
                'instructions': '1. Warm-up jog: 5 min\n2. Interval sprints: 10x1 min\n3. Steady pace run: 15 min\n4. Cool down walk: 5 min'
            },
            {
                'name': 'Widow\'s Web Workout',
                'description': 'Agility training from the Red Room',
                'activity_type': 'Boxing',
                'difficulty': 'Advanced',
                'duration': 50,
                'calories': 500,
                'instructions': '1. Shadow boxing: 10 min\n2. Heavy bag: 5x3 min rounds\n3. Speed bag: 10 min\n4. Stretching: 10 min'
            },
            {
                'name': 'Mjolnir Might',
                'description': 'Build god-like strength',
                'activity_type': 'Weightlifting',
                'difficulty': 'Advanced',
                'duration': 60,
                'calories': 600,
                'instructions': '1. Warm-up: 10 min\n2. Squats: 5x5\n3. Overhead press: 4x8\n4. Pull-ups: 4x10\n5. Hammer curls: 3x12'
            },
            {
                'name': 'Gamma Smash Session',
                'description': 'High-intensity Hulk training',
                'activity_type': 'HIIT',
                'difficulty': 'Advanced',
                'duration': 30,
                'calories': 550,
                'instructions': '1. Warm-up: 5 min\n2. Burpees: 4x20\n3. Jump squats: 4x15\n4. Mountain climbers: 4x30 sec\n5. Cool down: 5 min'
            },
            {
                'name': 'Dark Knight Discipline',
                'description': 'Train in the shadows like Batman',
                'activity_type': 'Boxing',
                'difficulty': 'Advanced',
                'duration': 60,
                'calories': 550,
                'instructions': '1. Warm-up: 10 min\n2. Martial arts combos: 15 min\n3. Heavy bag work: 20 min\n4. Core training: 10 min\n5. Flexibility: 5 min'
            },
            {
                'name': 'Man of Steel Marathon',
                'description': 'Kryptonian endurance training',
                'activity_type': 'Running',
                'difficulty': 'Intermediate',
                'duration': 50,
                'calories': 500,
                'instructions': '1. Warm-up: 10 min\n2. Long distance run: 35 min\n3. Sprint finish: 2 min\n4. Cool down: 3 min'
            },
            {
                'name': 'Amazon Warrior Workout',
                'description': 'Train like Wonder Woman',
                'activity_type': 'Weightlifting',
                'difficulty': 'Intermediate',
                'duration': 50,
                'calories': 450,
                'instructions': '1. Warm-up: 5 min\n2. Lunges: 3x12 each leg\n3. Rows: 4x10\n4. Shoulder press: 4x10\n5. Planks: 3x1 min'
            },
            {
                'name': 'Speed Force Sprint',
                'description': 'Lightning fast cardio',
                'activity_type': 'Running',
                'difficulty': 'Advanced',
                'duration': 30,
                'calories': 600,
                'instructions': '1. Dynamic warm-up: 5 min\n2. Sprint intervals: 15x30 sec\n3. Recovery jog between: 30 sec\n4. Cool down: 5 min'
            },
            {
                'name': 'Atlantean Aquatics',
                'description': 'Master the waters',
                'activity_type': 'Swimming',
                'difficulty': 'Intermediate',
                'duration': 45,
                'calories': 500,
                'instructions': '1. Warm-up swim: 10 min\n2. Freestyle laps: 20 min\n3. Backstroke: 10 min\n4. Cool down: 5 min'
            },
        ]
        
        for workout_data in workouts:
            Workout.objects.create(
                name=workout_data['name'],
                description=workout_data['description'],
                activity_type=workout_data['activity_type'],
                difficulty=workout_data['difficulty'],
                duration=workout_data['duration'],
                calories=workout_data['calories'],
                instructions=workout_data['instructions']
            )
        
        self.stdout.write(self.style.SUCCESS(f'Created {Workout.objects.count()} workout suggestions'))
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(self.style.SUCCESS(f'Teams: {Team.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Users: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Activities: {Activity.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Leaderboard Entries: {Leaderboard.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Workouts: {Workout.objects.count()}'))
