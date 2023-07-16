from filestack import Client

api_key = "FILESTACK_KEY"

client = Client(api_key)
new_link = client.upload(filepath='myfile.txt')
print(new_link.url)