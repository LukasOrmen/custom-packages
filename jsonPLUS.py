import pathlib
import json

def changeatt(dict_, path):
    try:
        counter = 0
        for key, value in dict_.items():
            with pathlib.Path(path).open("r") as f:
                data = json.loads(f.read())
            data[key] = value
            with pathlib.Path(path).open("w") as f:
                f.write(json.dumps(data))
            counter += 1
            print(str(counter) + "th term completed.")
        return "Completed succesfully."
    except AttributeError:
        return "AttributeError\nchangejsonatt(dictionary, path)"

def returnatt(list_, path):
    try:
        _list = []
        with pathlib.Path(path).open() as f:
            whole = json.loads(f.read())
        for item in list_:
            _list.append(whole[str(item)])
        return _list
    except TypeError:
        return "TypeError\nreturnatt(list, path)"
    except KeyError:
        return "TypeError\nreturnatt(list, path)"

def addatt(dict_, path):
    with pathlib.Path(path).open() as f:
        original = json.loads(f.read())
    for key, value in dict_.items():
        original[key] = value
        with pathlib.Path(path).open("w") as f:
            f.write(json.dumps(original))
    return "Completed succesfully."
