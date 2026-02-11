from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import datetime
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    """Test cases for the User model"""

    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            password="password123",
            team_id="team123"
        )

    def test_user_creation(self):
        """Test that a user instance is created correctly"""
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertIsNotNone(self.user._id)

    def test_user_str(self):
        """Test the string representation of a user"""
        self.assertEqual(str(self.user), "Test User")


class TeamModelTest(TestCase):
    """Test cases for the Team model"""

    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team"
        )

    def test_team_creation(self):
        """Test that a team instance is created correctly"""
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(self.team.description, "A test team")
        self.assertIsNotNone(self.team._id)

    def test_team_str(self):
        """Test the string representation of a team"""
        self.assertEqual(str(self.team), "Test Team")


class ActivityModelTest(TestCase):
    """Test cases for the Activity model"""

    def setUp(self):
        self.activity = Activity.objects.create(
            user_id="user123",
            activity_type="running",
            duration=30,
            calories=300,
            distance=5.0,
            date=datetime.now(),
            notes="Morning run"
        )

    def test_activity_creation(self):
        """Test that an activity instance is created correctly"""
        self.assertEqual(self.activity.user_id, "user123")
        self.assertEqual(self.activity.activity_type, "running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)
        self.assertEqual(self.activity.distance, 5.0)


class LeaderboardModelTest(TestCase):
    """Test cases for the Leaderboard model"""

    def setUp(self):
        self.leaderboard_entry = Leaderboard.objects.create(
            user_id="user123",
            user_name="Test User",
            team_id="team123",
            team_name="Test Team",
            total_calories=1000,
            total_activities=10,
            total_distance=50.0,
            rank=1
        )

    def test_leaderboard_creation(self):
        """Test that a leaderboard entry is created correctly"""
        self.assertEqual(self.leaderboard_entry.user_name, "Test User")
        self.assertEqual(self.leaderboard_entry.team_name, "Test Team")
        self.assertEqual(self.leaderboard_entry.total_calories, 1000)
        self.assertEqual(self.leaderboard_entry.rank, 1)


class WorkoutModelTest(TestCase):
    """Test cases for the Workout model"""

    def setUp(self):
        self.workout = Workout.objects.create(
            name="Test Workout",
            description="A test workout",
            activity_type="strength",
            difficulty="intermediate",
            duration=45,
            calories=400,
            instructions="Do the exercises"
        )

    def test_workout_creation(self):
        """Test that a workout instance is created correctly"""
        self.assertEqual(self.workout.name, "Test Workout")
        self.assertEqual(self.workout.activity_type, "strength")
        self.assertEqual(self.workout.difficulty, "intermediate")
        self.assertEqual(self.workout.duration, 45)

    def test_workout_str(self):
        """Test the string representation of a workout"""
        self.assertEqual(str(self.workout), "Test Workout")


class UserAPITest(APITestCase):
    """Test cases for the User API endpoints"""

    def test_get_users_list(self):
        """Test retrieving the list of users"""
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeamAPITest(APITestCase):
    """Test cases for the Team API endpoints"""

    def test_get_teams_list(self):
        """Test retrieving the list of teams"""
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITest(APITestCase):
    """Test cases for the Activity API endpoints"""

    def test_get_activities_list(self):
        """Test retrieving the list of activities"""
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITest(APITestCase):
    """Test cases for the Leaderboard API endpoints"""

    def test_get_leaderboard_list(self):
        """Test retrieving the leaderboard"""
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """Test cases for the Workout API endpoints"""

    def test_get_workouts_list(self):
        """Test retrieving the list of workouts"""
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class APIRootTest(APITestCase):
    """Test cases for the API root endpoint"""

    def test_api_root(self):
        """Test that the API root endpoint returns all available endpoints"""
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
