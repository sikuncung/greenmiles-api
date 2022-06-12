from django.contrib import admin

from rest_admin.src.modules.journeys.models import Journeys, JourneyDetail
from rest_admin.src.modules.users.models import Profile
from rest_admin.src.modules.rewards.models import Vouchers, UserVouchers, Rewards

# Register your models here.
admin.site.register(Profile)
admin.site.register(Journeys)
admin.site.register(JourneyDetail)
admin.site.register(Vouchers)
admin.site.register(UserVouchers)
admin.site.register(Rewards)