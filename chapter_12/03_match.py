def htt_status(status):
    match status:
        case 400:
            return "Not found"
        case 500:
            return "Internal Server error"
        case 200:
            return "ok"
        case 201:
            return "ok"
        case _:
            return "unknown status"


print(htt_status(200))  # "ok"
print(htt_status(500))  # "Internal Server error"


# extries you can merge two or more Dic as:
dic1 = {"a": 1, "b": 2}
dic2 = {"c": 3, "d": 4}
merged = dic1 | dic2
print(merged)
