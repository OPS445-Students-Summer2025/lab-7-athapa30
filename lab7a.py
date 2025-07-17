#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum, carrying minutes/seconds."""
    result = Time(0, 0, 0)
    result.hour = t1.hour + t2.hour
    result.minute = t1.minute + t2.minute
    result.second = t1.second + t2.second

    # carry seconds
    if result.second >= 60:
        result.minute += result.second // 60
        result.second = result.second % 60

    # carry minutes
    if result.minute >= 60:
        result.hour += result.minute // 60
        result.minute = result.minute % 60

    return result

def valid_time(t):
    """Check validity of time t."""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False
    return True

