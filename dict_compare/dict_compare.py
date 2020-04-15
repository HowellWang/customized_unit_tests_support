from collections import Counter


def is_same_dict(dict1, dict2):
    """ Recursively compare the two dictionaries.
    :param dict1: First dictionary
    :param dict2: Second dictionary
    :return: True if the dictionaries match
    """

    def is_same_list(l1, l2):
        is_match = False
        try:
            if Counter(l1) == Counter(l2):
                return True
        except TypeError:
            pass
        if len(l1) == len(l2) and len(l1) > 0:
            for v1e, v2e in zip(l1, l2):
                is_match = v1e == v2e
                if not is_match:
                    if isinstance(v1e, dict) and isinstance(v2e, dict):
                        is_match = is_same_dict(v1e, v2e)
                    elif isinstance(v1e, list) and isinstance(v2e, list):
                        is_match = is_same_list(v1e, v2e)
                if not is_match:
                    return is_match
        return is_match

    if dict1 == dict2:
        return True
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for k, v1 in sorted(dict1.items()):
        v2 = dict2[k]
        if v1 != v2:
            if isinstance(v1, dict) and isinstance(v2, dict):
                if not is_same_dict(v1, v2):
                    return False
            elif isinstance(v1, list) and isinstance(v2, list):
                if not is_same_list(v1, v2):
                    return False
            else:
                return False
    return True
