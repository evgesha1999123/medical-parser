import datetime
import time

def get_current_date() -> str:
    return datetime.date.today().isoformat()

def get_current_time() -> str:
    cur_time_unformatted = time.time()
    local_time = time.localtime(cur_time_unformatted)
    formatted_cur_time = time.strftime("%H:%M:%S", local_time)
    return formatted_cur_time

__all__ = ["get_current_date", "get_current_time"]