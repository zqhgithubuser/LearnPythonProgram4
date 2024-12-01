import json
from datetime import date

today = date.today()


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return {
                "_meta": "_date",
                "data": obj.timetuple()[:3],
            }
        return super().default(obj)


data = {
    "an_int": 42,
    "a_float": 3.14159265,
    "a_date": today,
}

json_data = json.dumps(data, cls=DateEncoder)
print(json_data)


def object_hook(obj):
    try:
        if obj["_meta"] == "_date":
            return date(*obj["data"])
    except KeyError:
        return obj


data_out = json.loads(json_data, object_hook=object_hook)
print(data_out)
