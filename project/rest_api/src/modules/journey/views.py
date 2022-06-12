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

from rest_admin.src.modules.journeys.models import Journeys, JourneyDetail, MRT, BUS, TRAIN, GRABBIKE, GRABCAR

ORDER_START_POINT = 1
ORDER_PUBLIC_TRANSPORT = 2
ORDER_END_POINT = 3
ORDER_PRIVATE_JOURNEY = 4
ORDER_ELIGIBLE = [ORDER_START_POINT, ORDER_PUBLIC_TRANSPORT, ORDER_END_POINT ]

logger = logging.getLogger(__name__)

USER_ID = 1000

ICON_JOURNEY = {MRT : "https://storage.googleapis.com/greenmiles/public-mrt.png",
                TRAIN : "https://storage.googleapis.com/greenmiles/public-train.png",
                BUS : "https://storage.googleapis.com/greenmiles/public-bus.png",
                GRABBIKE : "https://storage.googleapis.com/greenmiles/grab-bike.png",
                GRABCAR : "https://storage.googleapis.com/greenmiles/grab-car.png", }

ICON_PRIVATE_CAR = "https://storage.googleapis.com/greenmiles/privatecar.png"

ICON = {TRAIN: "https://storage.googleapis.com/greenmiles/journey-krl.png",
        MRT : "https://storage.googleapis.com/greenmiles/journey-mrt.png",
        BUS : "https://storage.googleapis.com/greenmiles/journey-bus.png"}


@api_view(['GET'])
@authentication_classes((RestCSRFAuthentication, BasicAuthentication))
@rest_verify_permission('can_access_greenmiles')
def get_list_journey(request):
    """ to get list journey."""

    start_time = time.time()

    journeys = Journeys.objects.filter(user_id=USER_ID)
    data = []

    for journey in journeys:
        data.append({
            "id": journey.id,
            "name": journey.title,
            "from": journey.start_point,
            "icon": ICON[journey.type],
            "type": journey.type,
            "miles": journey.miles,
            "distance": journey.distance,
            "date": journey.created_at.strftime("%B %d, %Y")
        })

    response = json_response.render_api_success_response(data, start_time, total_records=1)

    return Response(response, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes((RestCSRFAuthentication, BasicAuthentication))
@rest_verify_permission('can_access_greenmiles')
def get_detail_journey(request, journey_id):
    """ to get detail journey."""

    start_time = time.time()

    try:
        journey = Journeys.objects.get(id=journey_id)
        private_journey = JourneyDetail.objects.get(journey__id=journey_id, order=ORDER_PRIVATE_JOURNEY)

        eligible_journey = JourneyDetail.objects.filter(journey__id=journey_id, order__in=ORDER_ELIGIBLE).order_by('order')
        
        detail_journey = []
        for item in eligible_journey:
            detail_journey.append({
                "start": item.start_point,
                "type": item.vehicle_type,
                "icon": ICON_JOURNEY[item.vehicle_type],
                "end": item.end_point,
                "emission": item.emission,
                "distance": item.distance,
                "lat_start_point": item.lat_start_point,
                "long_start_point": item.long_start_point,
                "lat_end_point": item.lat_end_point,
                "long_end_point": item.long_end_point
                })

        data = {
            "id": journey.id,
            "name": journey.title,
            "from": journey.start_point,
            "icon": ICON_JOURNEY[journey.type],
            "type": journey.type,
            "distance": journey.distance,
            "date": journey.created_at.strftime("%B %d, %Y"),
            "start_point": "Green Hills Residence",
            "end_point": "SCBD District 8",
            "emission_occured": journey.emission_occured,
            "emission_actual": journey.emission_actual,
            "emission_reduced": journey.emission_reduced,
            "miles_earned": journey.miles,
            "journey_map": journey.journey_map,
            "journeys" : detail_journey,
            "private_journey": {
                "start": private_journey.start_point,
                "type": private_journey.vehicle_type,
                "icon": ICON_PRIVATE_CAR,
                "end": private_journey.end_point,
                "emission": private_journey.emission,
                "distance": private_journey.distance,
                "lat_start_point": private_journey.lat_start_point,
                "long_start_point": private_journey.long_start_point,
                "lat_end_point": private_journey.lat_end_point,
                "long_end_point": private_journey.long_end_point
            }

        }

    except Journeys.DoesNotExist:
        resp = json_response.render_api_error_response(error_message="journey not found", status=status.HTTP_404_NOT_FOUND)
        return Response(resp, status=status.HTTP_404_NOT_FOUND)

    response = json_response.render_api_success_response(data, start_time, total_records=1)

    return Response(response, status=status.HTTP_200_OK)
