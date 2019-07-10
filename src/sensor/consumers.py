from channels import Group

def ws_connect(message):
	# Message will be printed in the console
    print("Someone connected.")
    path = message['path']                                               

    if path == b’/sensor/':
        print("Adding new user to sensor group")
        # Add user to group for broadcast
        Group(“sensor").add(message.reply_channel) 
        # Reply to individual directly                       
        message.reply_channel.send({                                           
           "text": "You're connected to sensor group :) ",
        })
    else:
		print("Strange connector!!")

def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
	print("Received!!" + message['text'])

def ws_disconnect(message):
	# Message will be printed in the console
    print("Someone left us...")
    # Delete client form channel group
	Group("sensor").discard(message.reply_channel)