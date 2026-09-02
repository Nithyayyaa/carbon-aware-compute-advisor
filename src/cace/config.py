import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ENTSOE_API_TOKEN = os.environ.get("ENTSOE_API_TOKEN")
if not ENTSOE_API_TOKEN:
    raise RuntimeError(
        "ENTSOE_API_TOKEN is not set. Copy .env.example to .env and fill in "
        "your token."
    )

# entsoe-py resolves this to the Germany-Luxembourg bidding zone
# (EIC code 10Y1001A1001A82H). This is the zone that has been in use
# since the DE-AT-LU zone split in Oct 2018, so it covers our 7-day pull.
GERMANY_LUXEMBOURG = "DE_LU"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_RAW_DIR = PROJECT_ROOT / "data" / "raw"
