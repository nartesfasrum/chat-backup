import json, requests, os

# TODO:
# request json filename
# request chat channels to grab images from
# request output folder

json_filename = input("Chat-store filename: ")
output_filename = input("Output folder: ")
chat = input("Chat to archive: ")

chat = '/' + chat
channel = chat.rsplit('/', 1)[1]
ship = chat.rsplit('/', 1)[0]
ship = ship.split('~', 1)
ship = ship[1]

with open(json_filename) as json_file:

    json_chat = json.load(json_file)
    i = 0
    num_envelopes = len(json_chat['chat-initial'][chat]['envelopes'])
    output_filename = output_filename + '/' + ship + '/' + channel
    if not os.path.exists(output_filename):
        os.makedirs(output_filename)

    while i < num_envelopes:

        if 'url' in json_chat['chat-initial'][chat]['envelopes'][i]['letter']:
            url = json_chat['chat-initial'][chat]['envelopes'][i]['letter']['url']
            filename = url.rsplit('/', 1)[1]
            filepath = output_filename + '/' + filename
            r = requests.get(url)
            with open(filepath, 'wb') as filewrite:
                filewrite.write(r.content)
        else:
            pass

        i = i + 1
