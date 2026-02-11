from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    team_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'first_name', 'last_name', 'password', 'team_id', 'team_name', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def get_team_name(self, obj):
        if obj.team_id:
            try:
                from .models import Team
                from bson import ObjectId
                team = Team.objects.get(_id=ObjectId(obj.team_id))
                return team.name
            except (Team.DoesNotExist, Exception):
                return None
        return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('_id'):
            representation['_id'] = str(representation['_id'])
        return representation


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('_id'):
            representation['_id'] = str(representation['_id'])
        return representation


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'user_id', 'activity_type', 'duration', 'calories', 'distance', 'date', 'notes']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('_id'):
            representation['_id'] = str(representation['_id'])
        return representation


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['_id', 'user_id', 'user_name', 'team_id', 'team_name', 'total_calories', 'total_activities', 'total_distance', 'rank']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('_id'):
            representation['_id'] = str(representation['_id'])
        return representation


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description', 'activity_type', 'difficulty', 'duration', 'calories', 'instructions']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('_id'):
            representation['_id'] = str(representation['_id'])
        return representation
