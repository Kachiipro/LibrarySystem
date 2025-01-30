from rest_framework.throttling import SimpleRateThrottle
from django.utils.timezone import now
import math

class CustomRateThrottle(SimpleRateThrottle):
    scope = 'custom'  # Must match 'custom' in settings.py

    def get_cache_key(self, request, view):
        """Generate a cache key based on client IP address."""
        return self.get_ident(request)  # Uses client IP as the key

    def allow_request(self, request, view):
        """Check if the request is allowed and calculate reset time."""
        allowed = super().allow_request(request, view)

        if hasattr(self, 'history') and self.history:
            reset_time = self.history[0] + self.duration  # Calculate reset time
            request.rate_limit_reset = reset_time
        else:
            request.rate_limit_reset = None  # No history, reset is unknown

        return allowed

    def get_rate_limit_headers(self, request):
        """Generate rate limit headers with correct reset time."""
        remaining_requests = max(self.num_requests - len(getattr(self, 'history', [])), 0)
        reset_time = getattr(request, "rate_limit_reset", None)

        return {
            "X-RateLimit-Limit": str(self.num_requests),
            "X-RateLimit-Remaining": str(remaining_requests),
            "X-RateLimit-Reset": str(int(reset_time)) if reset_time else "N/A",
        }
