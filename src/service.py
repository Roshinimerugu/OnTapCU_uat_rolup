from datetime import datetime
from datetime import datetime, timedelta
import json
#from dateutil import relativedelta
import requests
import dateutil
from dateutil import relativedelta
import util

def lambda_handler(data, context):
    util.util_print()
    return {"a":1,"b":6}