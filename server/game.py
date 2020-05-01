from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit, send, rooms, join_room, close_room, leave_room
import scrabble

# Creating a flask app and using it to instantiate a socket object
game = Flask(__name__)
CORS(game, resources={r'/*':{'origin': '*'}})
game.config.from_object(__name__)
socketio = SocketIO(game, cors_allowed_origins="*")

allRooms = {}
allgames = {}
activeGamers = {}
gamerInfo = {}


# Handler for a message recieved over 'connect' channel
@socketio.on('connect')
def test_connect():
  gamerId = 'Gamer'+str(scrabble.getGamerId())
  while gamerId in list(activeGamers.values()):
    gamerId = 'Gamer'+str(scrabble.getGamerId())
  emit('connected', {'gamernick': gamerId })
  activeGamers[request.sid] = gamerId 

@socketio.on('disconnect')
def on_disconnect():
  gamer = activeGamers[request.sid]
  try:
    room = gamerInfo[gamer]
    on_lroom({'room': room, 'gamerid': gamer})  
  except:
    pass
  del activeGamers[request.sid]

@socketio.on('create')
def on_create(data):
  """Create a game lobby"""
  time = data['time']
  rules = data['rules']
  creator = data['creator']
  room = scrabble.getRoom(time, rules, creator)
  allRooms[room['id']] = room['data']
  on_join({'room': room['id'], 'gamer': creator})
  #emit('update_room',{'gameid': room, 'roomdata': allRooms[room]}, room= room, include_self = True)
  #print('created')
  #print(allRooms)

@socketio.on('join')
def on_join(data):
  room = data['room']
  gamer = data['gamer']
  added = False
  if gamer in gamerInfo:
    print(gamerInfo)
    if gamerInfo[gamer] != room:
      try:
        on_lroom({'room': gamerInfo[gamer], 'gamerid': gamer})
      except:
        del gamerInfo[gamer]
    else:
      emit('update_room',{'gameid': room, 'roomdata': allRooms[room]}, room= room, include_self = True)
      return
  if room in allRooms:
    if allRooms[room]['creator'] == gamer:
      added = True
    else:
      for r in allRooms[room]['slot']:
        if allRooms[room]['slot'][r]['nick'] == '':
          allRooms[room]['slot'][r]['status'] = 'Not Ready'
          allRooms[room]['slot'][r]['nick'] = gamer
          added = True
          break
    if added:
      gamerInfo[gamer] = room
      print(gamerInfo)
      join_room(room)
      emit('update_room',{'gameid': room, 'roomdata': allRooms[room]}, room= room, include_self = True)
    else:
      emit('error', {'error': 'Unable to join room. Room is full.'}, included_self = True)
  else:
    emit('error', {'error': 'Unable to join room. Room does not exist.'}, included_self = True)


@socketio.on('toggle_slot')
def on_stoggle(data):
  room = data['room']
  slot = data['slot']
  newtype = data['info']
  allRooms[room]['slot'][slot] = newtype
  emit('update_room',{'gameid': room, 'roomdata': allRooms[room]}, room= room, include_self = True)

@socketio.on('leave_room')
def on_lroom(data):
  room = data['room']
  gamer = data['gamerid']
  if allRooms[room]['creator'] == gamer:
    del allRooms[room]
    emit('left_room')
    emit('left_room', room= room,  include_self = False)
    close_room(room)
  else:
    for i in allRooms[room]['slot']:
      if (allRooms[room]['slot'][i]['nick'] == gamer):
        allRooms[room]['slot'][i] = { 'type': 'Human', 'status': 'Waiting', 'nick': '' }
    leave_room(room)
    del gamerInfo[gamer]
    emit('left_room')
    emit('update_room',{'gameid': room, 'roomdata': allRooms[room]}, room= room, include_self = False)

@socketio.on('p_ready')
def on_pready(data):
  room = data['room']
  gamer = data['gamerid']
  for i in allRooms[room]['slot']:
    if (allRooms[room]['slot'][i]['nick'] == gamer):
      allRooms[room]['slot'][i]['status'] = 'Ready'
      emit('update_room',{'gameid': room, 'roomdata': allRooms[room]}, room= room, include_self = True)
      return
  
@socketio.on('start_game')
def on_sgame(data):
  room = data['room']
  slot = data['slot']
  gamedata = allRooms[room]
  game = scrabble.startGame(gamedata, slot, room)
  allgames[room] = game
  emit('game_start',game, room= room, include_self = True)

@socketio.on('updated_rack')
def on_updaterack(data):
  room = data['room']
  gamedata = scrabble.game(room)
  bag = gamedata.getBagL()
  print(bag)
  emit('update_bag',{'bag': bag}, room= room, include_self = True)
  

@game.route('/api/played', methods = ['POST'])
def played():
  response = {}
  gamedata = request.get_json()
  board = gamedata['board']
  tiles = gamedata['tiles']
  word = scrabble.checkWords(tiles, board)
  res = word.cw()
  if res['status'] == 'failed':
    response = res
  else:
    response['status'] = res['status']
    wordplayed = []
    print(res['msg'])
    score = scrabble.getScore(res['msg'], tiles)
    print(score)
    wordplayed.append(res['msg']['mainword'])
    if(res['msg']['otho'] != 'none'):
      wordplayed.extend(list(res['msg']['otho'].values()))
    response['words'] = wordplayed
    response['score'] = score
  print(response)
  return jsonify(response)


@game.route('/api/refillrack', methods = ['POST'])
def refillrack():
  response = {}
  gamedata = request.get_json()
  room = gamedata['id']
  rack = gamedata['rack']
  game = scrabble.game(room)
  nrack = game.refillRack(rack)
  response['rack'] = nrack
  print(gamedata['gamer'] + ' ' + str(gamedata['rack']) + ' ' + str(nrack))
  response['status'] = 'success'
  return jsonify(response)
if __name__ == '__main__':
    socketio.run(game,debug= True)