import pyshorteners
long_url = input('Input URL : ')

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print('Short URL : ', short_url)
