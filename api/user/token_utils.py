from datetime import timedelta
from django.utils import timezone
from rest_framework.authtoken.models import Token

def create_token(user):
    # Calculate expiry date (24 hours from now)
    expires_at = timezone.now() + timedelta(hours=24)

    # Create token with expiry date
    token, _ = Token.objects.get_or_create(
        user=user,
        created=timezone.now(),
    )

    return token
