from schwab_api import Schwab
import os
from json import dumps

username = os.getenv("SCHWAB_USER")
password = os.getenv("SCHWAB_PASS")
totp_secret = os.getenv("SCHWAB_TOTP")

# Initialize our schwab instance
api = Schwab(
    # Optional session cache - uncomment to enable:
    # session_cache="session.json"
    # headless=False
)

# Login using playwright
logged_in = api.login(
    username=username,
    password=password,
    totp_secret=totp_secret # Get this using itsjafer.com/#/schwab.
)

# Get all positions from:
# https://ausgateway.schwab.com/api/is.ClientSummaryExpWeb/V1/api/positions
positions = api.get_all_positions()
positions_json = dumps(positions, indent=4)
print(positions_json)
