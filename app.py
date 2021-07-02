import json

def pp_json(json_thing, sort=False, indents=2):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

# insert the copied code below this line


pp_json(data.decode("utf-8"))
