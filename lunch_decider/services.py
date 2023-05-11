from datetime import date
from typing import List, Dict
from .models import Restaurant, Menu, Vote
from django.db import models


def get_current_day_vote_results() -> List[Dict[str, any]]:
    """
    Get the vote results for the current day.

    Returns:
        A list of dictionaries containing the restaurant name, vote count, and menu items for the current day.
    """

    today = date.today()
    votes = (
        Vote.objects.filter(menu__date=today)
        .values('menu__restaurant__name')
        .annotate(count=models.Count('menu__restaurant'))
        .order_by('-count')
        .values('menu__restaurant__name', 'count', 'menu__items')
    )

    return votes