from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin configuration for the User model"""
    list_display = ['name', 'email', 'team_id', 'created_at']
    list_filter = ['created_at', 'team_id']
    search_fields = ['name', 'email']
    readonly_fields = ['_id', 'created_at']
    ordering = ['-created_at']

    fieldsets = (
        ('User Information', {
            'fields': ('_id', 'name', 'email', 'password')
        }),
        ('Team Assignment', {
            'fields': ('team_id',)
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin configuration for the Team model"""
    list_display = ['name', 'description', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['_id', 'created_at']
    ordering = ['-created_at']

    fieldsets = (
        ('Team Information', {
            'fields': ('_id', 'name', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin configuration for the Activity model"""
    list_display = ['user_id', 'activity_type', 'duration', 'calories', 'distance', 'date']
    list_filter = ['activity_type', 'date']
    search_fields = ['user_id', 'activity_type', 'notes']
    readonly_fields = ['_id']
    ordering = ['-date']

    fieldsets = (
        ('Activity Information', {
            'fields': ('_id', 'user_id', 'activity_type', 'date')
        }),
        ('Metrics', {
            'fields': ('duration', 'calories', 'distance')
        }),
        ('Additional Information', {
            'fields': ('notes',)
        }),
    )


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin configuration for the Leaderboard model"""
    list_display = ['rank', 'user_name', 'team_name', 'total_calories', 'total_activities', 'total_distance']
    list_filter = ['team_name', 'rank']
    search_fields = ['user_name', 'team_name']
    readonly_fields = ['_id']
    ordering = ['rank']

    fieldsets = (
        ('Leaderboard Information', {
            'fields': ('_id', 'rank', 'user_id', 'user_name', 'team_id', 'team_name')
        }),
        ('Statistics', {
            'fields': ('total_calories', 'total_activities', 'total_distance')
        }),
    )


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin configuration for the Workout model"""
    list_display = ['name', 'activity_type', 'difficulty', 'duration', 'calories']
    list_filter = ['activity_type', 'difficulty']
    search_fields = ['name', 'description', 'instructions']
    readonly_fields = ['_id']
    ordering = ['name']

    fieldsets = (
        ('Workout Information', {
            'fields': ('_id', 'name', 'description')
        }),
        ('Workout Details', {
            'fields': ('activity_type', 'difficulty', 'duration', 'calories')
        }),
        ('Instructions', {
            'fields': ('instructions',)
        }),
    )
