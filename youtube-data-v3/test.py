from urllib.parse import urlparse, parse_qs


def get_id(url):
    parsed = urlparse(url)
    print(parsed)
    # qs: query string
    # https://stackoverflow.com/questions/5074803/retrieving-parameters-from-a-url
    qs = parse_qs(parsed.query)
    if parsed.netloc == "www.youtube.com" and "v" in qs.keys():
        id = qs["v"][0]
        return id

    elif parsed.netloc == "youtu.be" and parsed.path != "":
        # remove the forward slash
        id = parsed.path[1:]
        return id

    else:
        return -1


# def get_id(url):
#     parsed = parse_qs(url)
#     print(parsed)
#     # print(parsed.query["v"])


print(get_id("https://www.youtube.com/watch?v=ZkYOvViSx3E"))
print(get_id("https://www.youtube.com"))
print(get_id("https://youtu.be/o7h_sYMk_oc"))
print(get_id("https://youtu.be"))
