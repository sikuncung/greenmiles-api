""" Rest API Router. """
from django.urls import path

from rest_api.src.modules.sample import sample_views
from rest_api.src.modules.journey import views as journey_views
from rest_api.src.modules.user import views as user_views
from rest_api.src.modules.rewards import views as reward_views

app_name = "rest_api"
urlpatterns = [
    path('ping', sample_views.ping, name="ping"),

    path('profile', user_views.get_user_profile, name="profile"),
    path('profile/badges', user_views.get_badge_collection, name="get_badge_collection"),
    path('profile/challenges', user_views.get_user_challenge, name="get_user_active_challenge"),
    path('journeys', journey_views.get_list_journey, name="get_list_journey"),
    path('journeys/<int:journey_id>', journey_views.get_detail_journey, name="detail_journey"),
    path('vouchers', reward_views.get_list_voucher, name="get_list_voucher"),
    path('rewards', reward_views.get_list_reward, name="get_list_reward"),
    path('rewards/<int:reward_id>', reward_views.get_detail_reward, name="get_reward_option"),
    path('rewards/<int:reward_id>/select', reward_views.select_reward, name="select_reward_option"),
    
]