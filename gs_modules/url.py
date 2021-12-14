def get_url():
    file = open('url.txt', 'r')
    return file.read().splitlines()[0]