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

from rest_admin.src.modules.rewards.models import UserVouchers, Vouchers, Rewards, UNCLAIMED

logger = logging.getLogger(__name__)

USER_ID = 1000

@api_view(['GET'])
@authentication_classes((RestCSRFAuthentication, BasicAuthentication))
@rest_verify_permission('can_access_greenmiles')
def get_list_reward(request):
    """ to get list reward."""

    unclaimed_reward = Rewards.objects.filter(user_id=USER_ID, status=UNCLAIMED).order_by("id")

    start_time = time.time()
    data = []
    for item in unclaimed_reward:
        data.append({"reward_id":item.id,
                     "status":UNCLAIMED, 
                     "created_at":item.created_at, 
                     "thumbnail":"https://storage.googleapis.com/greenmiles/new_reward.png"})

    response = json_response.render_api_success_response(data, start_time, total_records=1)

    return Response(response, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes((RestCSRFAuthentication, BasicAuthentication))
@rest_verify_permission('can_access_greenmiles')
def get_detail_reward(request, reward_id):
    """ to get detail reward."""

    start_time = time.time()

    try:
        reward = Rewards.objects.get(id=reward_id, user_id=USER_ID, status=UNCLAIMED)
    except Rewards.DoesNotExist:
        resp = json_response.render_api_error_response(error_message="reward not found", status=status.HTTP_404_NOT_FOUND)
        return Response(resp, status=status.HTTP_404_NOT_FOUND)

    available_voucher = Vouchers.objects.filter()
    data = []
    for voucher in available_voucher:
        data.append({
            "voucher_id" : voucher.id,
            "type" : voucher.reward_type,
            "thumbnail" : voucher.thumbnail_active,
            "terms" : voucher.terms,
            "title" : voucher.title
        })

    response = json_response.render_api_success_response(data, start_time, total_records=1)

    return Response(response, status=status.HTTP_200_OK)
    

@api_view(['GET'])
@authentication_classes((RestCSRFAuthentication, BasicAuthentication))
@rest_verify_permission('can_access_greenmiles')
def get_list_voucher(request):
    """ to get list voucher."""

    user_vouchers = UserVouchers.objects.filter(user_id=USER_ID)

    data = []

    for item in user_vouchers:
        if item.voucher_status == "Active":
            icon = item.voucher.thumbnail_active
        elif item.voucher_status == "Used":
            icon = item.voucher.thumbnail_inactive

        data.append({
            "voucher_id": item.voucher.id,
            "type": item.voucher.reward_type,
            "thumbnail": icon,
            "created_at": item.created_at,
            "terms": item.voucher.terms,
            "title": item.voucher.title,
            "status": item.voucher_status
        })

    start_time = time.time()

    response = json_response.render_api_success_response(data, start_time, total_records=1)

    return Response(response, status=status.HTTP_200_OK)
    