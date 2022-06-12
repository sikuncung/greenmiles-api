import logging
import time

from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_api.src.authentication.rest_csrf_authentication import RestCSRFAuthentication
from rest_api.src.decorator.rest_decorator import rest_verify_permission
from rest_framework.response import Response

from vendor.errors import error_message
from vendor.helper import helper
from vendor.template import json_response
from rest_admin.src.modules.users.models import Profile


logger = logging.getLogger(__name__)

level_tier = [{"level":"New Comer", "miles_required":0, "icon": "https://storage.googleapis.com/greenmiles/new-comer.png"},
              {"level":"Apprentice", "miles_required":1000, "icon": "https://storage.googleapis.com/greenmiles/apprentice.png"},
              {"level":"Green Knight", "miles_required":3000, "icon": "https://storage.googleapis.com/greenmiles/knight.png"},
              {"level":"Eco Warrior", "miles_required":5000, "icon": "https://storage.googleapis.com/greenmiles/eco-warrior.png"},
              {"level":"Earth Ninja", "miles_required":10000, "icon": "https://storage.googleapis.com/greenmiles/earth-ninja.png"},
              {"level":"Sage of Nature", "miles_required":20000, "icon": "https://storage.googleapis.com/greenmiles/sage-of-nature.png"}]

USER_ID = 1000

@api_view(['GET'])
@authentication_classes((RestCSRFAuthentication, BasicAuthentication))
@rest_verify_permission('can_access_greenmiles')
def get_user_profile(request):
    """ to get user profile."""

    start_time = time.time()
    
    user_profile = Profile.objects.get(user_id=USER_ID)
    
    index_selected = 0 
    i = 0
    for tier in level_tier:
        if user_profile.miles < tier["miles_required"]:
            index_selected = i - 1
            break

        i += 1
    
    delta_miles = 200 - user_profile.miles % 200        
    data = {"id":user_profile.id, 
            "user_id":user_profile.user_id, 
            "name": user_profile.name,
            "miles": user_profile.miles,
            "current_level": user_profile.level,
            "distance": user_profile.distance,
            "miles_need_for_next_reward":delta_miles,
            "journeys": user_profile.journeys,
            "current_level": user_profile.level,
            "icon": level_tier[index_selected]["icon"],
            "current_level_miles": level_tier[index_selected]["miles_required"],
            "previous_level": level_tier[index_selected-1]["level"],
            "previous_level_miles": level_tier[index_selected-1]["miles_required"],
            "next_level_miles": level_tier[index_selected+1]["miles_required"],
            "next_level": level_tier[index_selected+1]["level"]
            }

    response = json_response.render_api_success_response(data, start_time, total_records=1)

    return Response(response, status=status.HTTP_200_OK)
    

@api_view(['GET'])
@authentication_classes((RestCSRFAuthentication, BasicAuthentication))
@rest_verify_permission('can_access_greenmiles')
def get_badge_collection(request):
    """ to get user badge collection."""

    start_time = time.time()
    data =  [{
                "badge_id": 12,
                "title": "Buzzgreen",
                "thumbnail": "https://storage.googleapis.com/cdn-grab-hackathon/images/greenmiles/BuzzGreen.png",
                "awarded_at": "2022-06-06 10:10:20",
                "description":"Lorem ipsum dolor sit amet"
                
            },{
                "badge_id": 13,
                "title": "Green Ranger",
                "thumbnail": "https://storage.googleapis.com/cdn-grab-hackathon/images/greenmiles/CarbonFighter.png",
                "awarded_at": "2022-06-06 10:10:20",
                "description":"Lorem ipsum dolor sit amet"
            },{
                "badge_id": 14,
                "title": "Earth Day",
                "thumbnail": "https://storage.googleapis.com/cdn-grab-hackathon/images/greenmiles/EarthDay.png",
                "awarded_at": "2022-06-06 10:10:20",
                "description":"Lorem ipsum dolor sit amet"
            },
            {
                "badge_id": 15,
                "title": "Commuters",
                "thumbnail": "https://storage.googleapis.com/cdn-grab-hackathon/images/greenmiles/Commuters.png",
                "awarded_at": "2022-06-06 10:10:20",
                "description":"Lorem ipsum dolor sit amet"
            },
            {
                "badge_id": 16,
                "title": "First Mile",
                "thumbnail": "https://storage.googleapis.com/cdn-grab-hackathon/images/greenmiles/First%20Mile.png",
                "awarded_at": "2022-06-06 10:10:20",
                "description":"Lorem ipsum dolor sit amet"
            }]


    response = json_response.render_api_success_response(data, start_time, total_records=1)

    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes((RestCSRFAuthentication, BasicAuthentication))
@rest_verify_permission('can_access_greenmiles')
def get_user_challenge(request):
    """ to get user active challenge."""

    start_time = time.time()
    data =  [{
                "badge_id": 12,
                "title": "Buzzgreen",
                "thumbnail": "https://storage.googleapis.com/cdn-grab-hackathon/images/greenmiles/buzzgreen_inactive.png",
                "created_at": "2022-06-06 10:10:20",
                "description":"Lorem ipsum dolor sit amet",
                "current_progress":1,
                "target":4,
                "type":"journey",
                "unit":"Journey",
                "due_date":"2022-06-06"
                
            },{
                "badge_id": 13,
                "title": "Miles Hunter",
                "thumbnail": "https://storage.googleapis.com/cdn-grab-hackathon/images/greenmiles/miles_hunter_inactive.png",
                "created_at": "2022-06-06 10:10:20",
                "description":"Lorem ipsum dolor sit amet",
                "current_progress":2,
                "target":4,
                "type":"miles",
                "unit":"Day",
                "due_date":"2022-06-06"
                
            },
            {
                "badge_id": 14,
                "title": "Carbon Fighter",
                "thumbnail": "https://storage.googleapis.com/cdn-grab-hackathon/images/greenmiles/carbon-fighter-inactive.png",
                "created_at": "2022-06-06 10:10:20",
                "description":"Lorem ipsum dolor sit amet",
                "current_progress":50,
                "target":100,
                "type":"distance",
                "unit":"km",
                "due_date":"2022-06-06"
                
            }]


    response = json_response.render_api_success_response(data, start_time, total_records=1)

    return Response(response, status=status.HTTP_200_OK)
    