import datetime
from django.conf import settings
import pytz


def as_local_timezone(t: datetime.datetime) -> datetime.datetime:
    """
    :param t: 需要设置为local timezone的datetime
    :return: datetime
    将t设置为settings中设置的时区（一般为本地时区）
    """
    tz = pytz.timezone(settings.TIME_ZONE)
    return t.astimezone(tz)
