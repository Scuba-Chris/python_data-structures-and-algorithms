def left_join(d1, d2):
    results = []
    for key in d1:
        if key in d2:
            results.append([key, d1[key], d2[key]])
        else:
            results.append([key, d1[key], None])
    return results