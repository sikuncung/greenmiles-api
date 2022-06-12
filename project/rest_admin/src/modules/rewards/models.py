from django.db import models
from rest_admin.src.modules.users.models import Profile


TYPE_FIXED = "fixed"
TYPE_PERCENTAGE = "percentage"

TYPE_OPTION = (
    (TYPE_PERCENTAGE, TYPE_PERCENTAGE),
    (TYPE_FIXED, TYPE_FIXED),
)

ACTIVE = "active"
EXPIRED = "expired"
USED = "used"

STATUS_OPTION = (
    (ACTIVE, ACTIVE),
    (EXPIRED, EXPIRED),
)

VOUCHER_OPTION = (
    (USED, USED),
    (ACTIVE, ACTIVE),
)

CLAIMED = "claimed"
UNCLAIMED = "unclaimed"

REWARD_OPTION = (
    (CLAIMED, CLAIMED),
    (UNCLAIMED, UNCLAIMED),
)

CHALLENGE_JOURNEY = "journey"
CHALLENGE_DISTANCE = "distance"
CHALLENGE_MILES = "miles"
CHALLENGE_DAILY = "daily"
CHALLENGE_FIRST = "first"

CHALLENGE_OPTION = (
    (CHALLENGE_FIRST, CHALLENGE_FIRST),
    (CHALLENGE_JOURNEY, CHALLENGE_JOURNEY),
    (CHALLENGE_DISTANCE, CHALLENGE_DISTANCE),
    (CHALLENGE_MILES, CHALLENGE_MILES),
    (CHALLENGE_DAILY, CHALLENGE_DAILY),
)

class Vouchers(models.Model):

    reward_type = models.CharField("Type", max_length=150, null=True)
    terms = models.TextField("Terms", null=True)
    thumbnail_active = models.TextField("Thumbnail Active", null=True)
    thumbnail_inactive = models.TextField("Thumbnail Inactive", null=True)
    title = models.TextField("Title", null=True)
    amount = models.IntegerField("Amount", null=True)
    discount_type = models.CharField("Discount Type", max_length=32, choices=TYPE_OPTION, blank=True, null=True)
    is_active = models.BooleanField("Is Active", default=True)
    
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.id)

    class Meta(object):
        """ Meta : for Vouchers metadata."""
        ordering = ['-created_at']
        db_table = "vouchers"
        verbose_name = "Voucher"
        verbose_name_plural = "Vouchers"

class UserVouchers(models.Model):

    voucher = models.ForeignKey(
        Vouchers,
        on_delete=models.CASCADE,
        verbose_name="Voucher",
        related_name="voucher_id",
        null=True,
        blank=True,
    )

    user_id = models.IntegerField("User",null=True)
    voucher_status = models.CharField("Voucher Status", max_length=32, choices=VOUCHER_OPTION, blank=True, null=True)
    expired_at = models.DateTimeField("Expired At", null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.voucher.title, self.user.name)

    class Meta(object):
        """ Meta : for Vouchers metadata."""
        ordering = ['-created_at']
        db_table = "user_vouchers"
        verbose_name = "User Voucher"
        verbose_name_plural = "User Vouchers"


class Rewards(models.Model):

    voucher = models.ForeignKey(
        Vouchers,
        on_delete=models.CASCADE,
        verbose_name="Voucher",
        related_name="reward_voucher_id",
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name="Profile",
        related_name="reward_profile_id",
        null=True,
        blank=True,
    )
    
    status = models.CharField("Status", max_length=32, choices=REWARD_OPTION, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.user.name)

    class Meta(object):
        """ Meta : for Vouchers metadata."""
        ordering = ['-created_at']
        db_table = "rewards"
        verbose_name = "Reward"
        verbose_name_plural = "Rewards"


class Challenge(models.Model):

    title = models.CharField("Title", max_length=150, null=True)
    unit = models.CharField("Unit", max_length=50, blank=True, null=True)
    thumbnail_active = models.TextField("Thumbnail Active", blank=True, null=True)
    thumbnail_inactive = models.TextField("Thumbnail Inactive", blank=True, null=True)
    description = models.TextField("Description", blank=True, null=True)
    target = models.IntegerField("Target", blank=True, null=True)
    challenge_type = models.CharField("Status", max_length=32, choices=CHALLENGE_OPTION, blank=True, null=True)
    due_date = models.DateTimeField("Due Date", auto_now_add=True)
    status = models.CharField("Status", max_length=32, choices=STATUS_OPTION, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.title, self.challenge_type)

    class Meta(object):
        """ Meta : for Challenge metadata."""
        ordering = ['-created_at']
        db_table = "challenges"
        verbose_name = "Challenge"
        verbose_name_plural = "Challenges"


class Badge(models.Model):

    user_id = models.IntegerField("User",null=True)

    challenge = models.ForeignKey(
        Challenge,
        on_delete=models.CASCADE,
        verbose_name="Challenge",
        related_name="challenge_id",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.user.name, self.challenge.title)

    class Meta(object):
        """ Meta : for Badge metadata."""
        ordering = ['-created_at']
        db_table = "badges"
        verbose_name = "Badge"
        verbose_name_plural = "Badges"
