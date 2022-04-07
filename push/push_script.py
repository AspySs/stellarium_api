import urllib
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import json
import sys

MY_API_KEY = "AAAAkzFvnL0:APA91bE2Gi4YzIhi2zAax0CBgceZCXO4RmKnRP9q3gPNsJpoNIZ9wpEnpMegc90qWfHiUgSK9HHg930zHkS2NXpSTkSiT4MVapiz2AG4w_HCfhQiwktr8nrrj9rklTHpFxUf77RLkQBO"

messageTitle = sys.argv[1]
messageBody = sys.argv[2]

data={
    "to" : "/Notifications/test_notification",
    "notification" : {
        "body" : messageBody,
        "title" : messageTitle,
        "icon" : "stellarium_logo_icon"
    }
}
data = urllib.parse.urlencode(data).encode("utf-8")
#dataAsJSON = json.dumps(data)

request = Request(
    "https://gcm-http.googleapis.com/gcm/send",
    data,
    { "Authorization" : "key="+MY_API_KEY,
      "Content-type" : "application/json"
    }
)

print (urlopen(request).read())