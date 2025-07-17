#!/usr/bin/env python3

from lab7b import Time, format_time, valid_time

def time_to_sec(time):
    minutes = time.hour * 60 + time.minute
    return minutes * 60 + time.second

def sec_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    total = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total)

def change_time(time, seconds):
    total = time_to_sec(time) + seconds
    new_time = sec_to_time(total)
    time.hour, time.minute, time.second = new_time.hour, new_time.minute, new_time.second
    return None

