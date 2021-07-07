import os
import logging
import requests
import argparse
from urllib.parse import urlparse, parse_qs

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def get_id(url):
    parsed = urlparse(url)
    # qs: query string
    # https://stackoverflow.com/questions/5074803/retrieving-parameters-from-a-url
    qs = parse_qs(parsed.query)

    if parsed.scheme == "":
        logging.error("Include https:// before address")
        return -1

    elif parsed.netloc == "www.youtube.com" and "v" in qs.keys():
        id = qs["v"][0]
        return id

    elif parsed.netloc == "youtu.be" and parsed.path[1:] != "":
        id = parsed.path[1:]
        return id

    else:
        return -1


def download_image(id, filename):
    img_url = f"https://i.ytimg.com/vi/{id}/maxresdefault.jpg"
    logging.info("Image URL:" + img_url)

    img_res = requests.get(img_url)
    status = img_res.status_code
    if status == 200:
        with open(filename, 'wb') as f:
            f.write(img_res.content)
    else:
        return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="youtube_thumbnail")

    print("""IMPORTANT: Enclose the URL in single quotes.
SUPPORTED URL's:
    1.https://www.youtube.com/watch?v=dQw4w9WgXcQ
    2.https://youtu.be/dQw4w9WgXcQ
        """)

    parser.add_argument("url", type=str, help="input url")
    parser.add_argument("-o", "--out",
                        metavar="FILE",
                        help="write output to FILE.jpg "
                        "[default:<input filename>.jpg]")

    args = parser.parse_args()
    logging.info(args.url)
    id = get_id(args.url)

    if id != -1:
        logging.info("ID:" + id)
        if args.out == None:
            out_file = f"{id}.jpg"
        else:
            out_file = args.out + ".jpg"

        res = download_image(id, out_file)
        if res != -1:
            logging.info("Downloading...")
            logging.info("Thumbnail written")
        else:
            logging.error("Invalid URL")
            logging.info("Exiting...")

    else:
        logging.error("URL not supported")
        logging.info("Exiting...")
