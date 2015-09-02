def something_complicated():
    return [1,2,37,42]

import json

with open('something_complicated_approved.json', 'wb') as f:
    json.dump(something_complicated(), f)

