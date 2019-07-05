import urllib.request

response = urllib.request.Request(url)
response.add_header()
print(response)

cont = response.read()
print(cont)