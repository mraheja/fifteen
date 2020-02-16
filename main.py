from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
from random import choice
import matches

app = Flask(__name__)
app.config["SECRET_KEY"] = "HELLO"
socketio = SocketIO(app)

number_list = [
	100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
	416, 417, 418, 421, 422, 423, 424, 425, 426,
	429, 431, 444, 450, 451, 500, 502, 503, 504, 506, 507, 508, 509, 510, 511, 599
]

@app.route('/')
@app.route('/index.html')
@app.route('/home')
def index():
  return render_template('index.html')

@app.route('/generic')
def index2():
  return render_template('generic.html')

@app.route('/elements')
def elements():
  return render_template('elements.html')

@app.route('/user/', defaults={'username': None})
@app.route('/user/<username>')
def generate_user(username):
	if not username:
		username = request.args.get('username')

	if not username:
		return 'Sorry error something, malformed request.'

	return render_template('personal_user.html', user=username)

@app.route('/matches3')
def matches3():
  past_matches = matches.get_past_matches()
  current_match = matches.get_current_match()
  return render_template('matches3.html', past=past_matches, current=current_match)

'''
@app.route('/matches', defaults={'username': None})
@app.route('/matches?<username>')
def matches(username):
  if not username:
 		username = request.args.get('username')

  # results = # some other method that returns a dictionary
  # pass in user id, display match

  return render_template('matches.html', header = username)
'''

@app.route('/base')
def base():
  return render_template('base.html')

@app.route('/about')
def about():
  return render_template('about.html')
  
## MESSAGING SERVICE

channel_list = {"general": [] }
present_channel = {"initial":"general"}

@app.route("/matches", methods=["POST", "GET"])
def match():
    if request.method == "GET":
        # Pass channel list to, and use jinja to display already created channels
        return render_template("matches.html", channel_list=channel_list)
    elif request.method == "POST":
        channel = request.form.get("channel_name")
        #user = request.form.get("username")
        user = "mehul"

        # Adding a new channel
        if channel and (channel not in channel_list):
            channel_list[channel] = []
            return jsonify({"success": True})
        # Switching to a different channel
        elif channel in channel_list:
            # send channel specific data to client i.e. messages, who sent them, and when they were sent
            # send via JSON response and then render with JS
            print(f"Switch to {channel}")
            present_channel[user] = channel
            channel_data = channel_list[present_channel[user]]
            return jsonify(channel_data)
        else:
            return jsonify({"success": False})

@socketio.on("create channel")
def create_channel(new_channel):
    emit("new channel", new_channel, broadcast=True)

@socketio.on("send message")
def send_message(message_data):
    print(message_data)
    channel = message_data["current_channel"]
    channel_message_count = len(channel_list[channel])
    del message_data["current_channel"]
    channel_list[channel].append(message_data)
    message_data["deleted_message"] = False
    if(channel_message_count >= 100):
        del channel_list[channel][0]
        message_data["deleted_message"] = True
    emit("recieve message", message_data, broadcast=True, room=channel)

@socketio.on("delete channel")
def delete_channel(message_data):
    channel = message_data["current_channel"]
    user = message_data["user"]
    present_channel[user] = "general"
    del message_data["current_channel"]
    del channel_list[channel]
    channel_list["general"].append(message_data)
    message_data = {"data": channel_list["general"], "deleted_channel": channel}
    emit("announce channel deletion", message_data, broadcast=True)

@socketio.on("leave")
def on_leave(room_to_leave):
    print("leaving room")
    leave_room(room_to_leave)
    emit("leave channel ack", room=room_to_leave)

@socketio.on("join")
def on_join(room_to_join):
    print("joining room")
    join_room(room_to_join)
    emit("join channel ack", room=room_to_join)

app.run(host='0.0.0.0', port=8080)