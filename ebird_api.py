from ebird.api import get_taxonomy

INVALID_CHARS = [" ", "-", ","]


def is_name_valid(name: str) -> bool:
    for char in INVALID_CHARS:
        if char in name:
            return False
    return True


def get_rid_of_s(name: str) -> str:
    if name[-1] == 's':
        return name[:-1]
    else:
        return name

    
def without_duplicate(x: list) -> list:
    return list(set(x))


def get_bird_names() -> list:
    taxonomy = get_taxonomy()
    bird_list = []
    for element in taxonomy:
        if "familyComName" in element:
            name = element["familyComName"]
            if is_name_valid(name):
                name = get_rid_of_s(name)
                bird_list.append(name)
    return without_duplicate(bird_list)
