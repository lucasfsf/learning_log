"""Helper functions for the app"""
from django.http import Http404


def ensure_user_ownership(owner, user):
    """Compares owner of topic to current user and raises error if different"""
    if owner != user:
        raise Http404
