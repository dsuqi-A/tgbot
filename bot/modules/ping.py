import requests
from bot import logger

def ping_url(ping_url):
  try:
    response = requests.get(ping_url)
    status_code = response.status_code
    if status_code == 200:
      ping_time = response.elapsed.total_seconds() * 1000
      ping_time = f"{int(ping_time)}ms"
      return ping_time, status_code
    else:
      return "~", status_code
  except Exception as e:
    logger.error(f"Error (pinging url): {e}")
    return "~", None
