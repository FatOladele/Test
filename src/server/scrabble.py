import random
import string
import os
import json
import copy
from materials import materials, dictionary, TW, DW, TL, DL
gamePath = os.path.join(os.path.dirname(__file__),'game.json')
letcode=  {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I":  9, "J": 10, "K": 11, "L": 12, "M": 13, "N":14, "O": 15}
global  yWords
yWords = dictionary()
yWords = yWords.dictWords()
class checkWords:
  def __init__(self, nl, board):
    self.nl = nl
    self.emptyboard = True
    self.onstar = False
    self.board = self.reboard(board)
    
  def cw(self):
    if (len(self.nl) > 1):
      return self.checkPlacement()
    else:
      return self.oneletter()
  def reboard(self, board):
    for i in range(len(board)):
      for j in range(len(board[i])):
        if( board[i][j] != 0):
          board[i][j] = board[i][j]['lp']
          self.emptyboard = False
    return board
  def oneletter(self):
    bcode = list(self.nl.keys())[0]
    y = letcode[bcode[0]] - 1
    x = int(bcode[1:]) -1
    plist = []
    cod = 0
    if ((self.emptyboard)):
      return { "status": 'failed', "msg": 'You must play a word'}
    else:
      if( ((y > 1) and (self.board[y+1][x] or 0)) or ((y < 15) and (self.board[y-1][x] != 0))):
        self.direction = 'x'
        plist.append(x)
        cod = y
      elif ( ((x>1) and (self.board[y][x - 1] != 0)) or ((y<15) and (self.board[y][x+1] != 0))):
        self.direction = 'y'
        plist.append(y)
        cod = x
      else:
        return { "status": 'failed', "msg": 'Letter not connected to any word'}
    return self.getWords(plist, cod, [])
  def checkPlacement(self):
    px = []
    py = []
    startX = 0
    startY = 0
    bcode = list(self.nl.keys())
    for i in range(len(bcode)):
      py.append((letcode[bcode[i][0]]) - 1)
      px.append(int(bcode[i][1:]) -1)
    dx = 0
    dy = 0
    for i in range(len(px)):
      if px[i] != px[0]:
        dx = 1
        self.direction = 'x'
      if px[i] == 7:
        startX = 1
    for i in range(len(py)):
      if py[i] != py[0]:
        dy = 1
        self.direction = 'y'
      if py[i] == 7:
        startY = 1
    if((startX == 1) and (startY == 1)):
      self.onstar = True
    if((dx > 0) and (dy > 0)):
      return { "status": 'failed', "msg": 'You can only play vertically or horizontally'}
    elif(self.emptyboard and (not(self.onstar))):
      return { "status": 'failed', "msg": 'Starting word must be on star'}
    else:
      return self.checkConnection(px, py)

  def checkConnection(self,px,py):
    if (self.direction == 'x'):
      px.sort()
      emptyX = [x for x in range(px[0],px[-1]) if x not in px]
      if(len(emptyX) > 0):
        for i in range(len(emptyX)):
          if(self.board[py[0]][emptyX[i]] == 0):
            return { "status": 'failed', "msg": 'Spaces in word'}
      return self.getWords(px,py[0],emptyX)
    elif(self.direction == 'y'):
      py.sort()
      emptyY = [y for y in range(py[0],py[-1]) if y not in py]
      if(len(emptyY) > 0):
        for i in range(len(emptyY)):
          if(self.board[emptyY[0]][px[0]] == 0):
            return { "status": 'failed', "msg": 'Spaces in word'}
      return self.getWords(py,px[0],emptyY)
  def getWords(self,plist, cod, elist ):
    words = {}
    pre = plist[0] - 1
    post = plist[-1] + 1
    new = 0
    while((new >= 0)):
      new = -1
      if pre>= 0:
        if (((self.direction =='y') and (self.board[pre][cod] != 0)) or ((self.direction =='x') and (self.board[cod][pre] != 0))):
          new += 1
          elist.append(pre)
          pre -= 1
      if post <= 14:
        if (((self.direction =='y') and (self.board[post][cod] != 0)) or ((self.direction =='x') and (self.board[cod][post] != 0))):
          new += 1
          elist.append(post)
          post += 1
    
    elist.extend(plist)
    elist
    elist.sort() 
    mw = []
    if(self.direction == 'x'):
      for m in elist:
        if(m in plist):
          key = self.getKey(cod, m)
          # key = str(list(letcode.keys())[list(letcode.values()).index(cod + 1)]) + str(m + 1)
          mw.append(self.nl[key])
        else:
          mw.append(self.board[cod][m])
    elif(self.direction == 'y'):
      for m in elist:
        if(m in plist):
          key = self.getKey(m, cod)
          mw.append(self.nl[key])
        else:
          mw.append(self.board[m][cod])

    words['mainword'] = mw
    othow = self.getOwords(plist, cod)
    words['otho'] = othow
    if ((othow == 'none') and (len(mw) == len(plist))and not(self.emptyboard)):
      return { "status": 'failed', "msg": 'word not connected'}
    else:
      return {"status": 'success', "msg": words}

  def getKey(self, y, x):
    return str(list(letcode.keys())[list(letcode.values()).index(y + 1)]) + str(x +1)

  def getOwords(self, plist, cod):
    owords = {}
    for p in range(len(plist)):
      new = 0
      letp = plist[p]
      pre = cod - 1
      post = cod + 1
      elist = []
      while((new >= 0)):
        new = -1
        if pre>= 0:
          if (((self.direction =='y') and (self.board[letp][pre] != 0)) or ((self.direction =='x') and (self.board[pre][letp] != 0))):
            new += 1
            elist.append(pre)
            pre -= 1
        if post <= 14:
          if (((self.direction =='y') and (self.board[letp][post] != 0)) or ((self.direction =='x') and (self.board[post][letp] != 0))):
            new += 1
            elist.append(post)
            post += 1 
      
      if len(elist) != 0:
        elist.append(cod)
        elist.sort()
        ow = []
        if(self.direction == 'x'):
          for m in elist:
            if(m == cod):
              key = self.getKey(m, letp)
              # key = str(list(letcode.keys())[list(letcode.values()).index(cod + 1)]) + str(m + 1)
              ow.append(self.nl[key])
            else:
              ow.append(self.board[m][letp])
        elif(self.direction == 'y'):
          for m in elist:
            if(m == cod):
              key = self.getKey(letp, m)
              ow.append(self.nl[key])
            else:
              ow.append(self.board[letp][m])
        owords[key] = ow

    if (owords != {}): 
      return owords 
    else:  
      return 'none'

def refillRack(rack, bag):
  nbag = bag
  while ((len(rack) < 7) and (len(nbag) > 0)):
    random.shuffle(nbag)
    rack.append(nbag.pop())
  return {'bag': nbag, 'rack': rack}

def getScore(words, tilesonbord):
  keys = list(tilesonbord.keys())
  dlkey = [x for x in keys if x in DL]
  dwkey = [x for x in keys if x in DW]
  tlkey = [x for x in keys if x in TL]
  twkey = [x for x in keys if x in TW]
  mwscore = 0
  othoscore = 0
  gameObject = materials()
  scores = gameObject.getscores()
  mainword = words['mainword']
  for i in dlkey:
    if tilesonbord[i] > 200: tilesonbord[i] = 200
    mwscore += scores[str(tilesonbord[i])]
  for i in tlkey:
    if tilesonbord[i] > 200: tilesonbord[i] = 200
    mwscore += 2 * scores[str(tilesonbord[i])]
  for i in mainword:
    if i > 200: i = 200
    mwscore += scores[str(i)]
  for i in dwkey:
    mwscore = mwscore * 2
  for i in twkey:
    mwscore = mwscore * 3
  if words['otho'] != 'none':
    othokeys = list(words['otho'].keys())
    for k in othokeys:
      if tilesonbord[k] > 200: tilesonbord[k] = 200
      if k in dlkey:
        othoscore += scores[str(tilesonbord[k])]
      elif k in tlkey:
        othoscore += 2 * scores[str(tilesonbord[k])]
      ow = 0
      for i in words['otho'][k]:
        if i > 200: i = 200
        ow += scores[str(i)]
      if k in dwkey:
        ow = ow * 2
      elif k in twkey:
        ow = ow * 3
      othoscore += ow

  return mwscore + othoscore     

# def rerack(rack, tileonboard):
#   for i in list(tileonboard.values()):
#     rack.remove(i)
#   return rack
def checkDictionary (words):
  for word in words:
    wcode = ''
    for i in word:
      wcode += str(i)
    if wcode not in yWords:
      return False
  return True
def swaptiles(rack, swaptiles, bag):
  for i in swaptiles:
    rack.remove(i)
  res = refillRack(rack, bag)
  newrack = res['rack']
  newbag = res['bag']
  for i in swaptiles:
    newbag.append(i)
  return {'bag': newbag, 'rack': newrack}
  
def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def getRoom(time, rules, creator, observer):
  roomId = randomString(5)
  room = {'id': roomId, 'data' : {'slot': {'slot1':{'type':'Human', 'status': 'Not ready', 'nick': creator}, 'slot2':{'type':'Human', 'status': 'waiting', 'nick':''}, 'slot3':{'type':'Human', 'status': 'waiting', 'nick':''}, 'slot4':{'type':'Human', 'status': 'waiting', 'nick':''}}, 'time': (time*60), 'observe': observer, 'olist': [], 'rules': rules, 'creator': creator}}
  return room

def getGamerId():
  number = random.randint(11111, 99999)
  return number

def startGame(roomdata, slot, roomid):
  player = {}
  gameobject = materials()
  for a in slot:
    gamer = roomdata['slot'][a]['nick'] 
    player[gamer] = {'id': a[-1], 'score': 0, 'time': roomdata['time'] }
  bag = gameobject.getbag()
  board = gameobject.getboard()
  game = {'board': board, 'players': player, 'bag': bag, 'turn': 1, 'tilesonboard':{}, 'probers': {'yes': [], 'no': []}, 'misser': [], 'pwords': [], 'pscore': 0, 'cplayer': '', 'cpasses': 0, 'endgame': {}} 
  with open(gamePath, "r") as file:
    data = json.load(file)
  data[roomid] = game
  with open(gamePath, "w") as file:
    json.dump(data, file)
  return game

class game:
  def __init__(self, room):
    self.gid = room
    with open(gamePath, "r") as file:
      data = json.load(file)
    self.gdata = data[self.gid]
    self.gbag = self.gdata['bag']
    self.board = self.gdata['board']
    self.players = self.gdata['players']
  def getBag(self):
    return self.gbag
  def getBagL(self):
    return len(self.gbag)
  def getBoard(self):
    return self.board
  def getPlayers(self):
    return self.players
  def setBag(self, bag):
    self.gbag = bag
    self.gdata['bag'] = bag
    with open(gamePath, "r") as file:
      data = json.load(file)
    data[self.gid] = self.gdata
    with open(gamePath, "w") as file:
      json.dump(data, file)
    
  def refillRack(self, rack):
    nbag = self.gbag
    while ((len(rack) < 7) and (len(nbag) > 0)):
      random.shuffle(nbag)
      rack.append(nbag.pop())
    self.setBag(nbag)
    return rack
  def swaptiles(self, rack, swaptiles):
    nbag = self.gbag
    for i in swaptiles:
      rack.remove(i)
      rack.append(nbag.pop())
    for i in swaptiles:
      nbag.append(i)
    self.setBag(nbag)
    return rack
  def setBoard(self, board):
    self.board = board
    self.gdata['board'] = board
    with open(gamePath, "r") as file:
      data = json.load(file)
    data[self.gid] = self.gdata
    with open(gamePath, "w") as file:
      json.dump(data, file)
  def swappass(self, gamer, action, nswap = 0):
    activity = []
    if action == 'swap':
      act = gamer + ' swapped ' + str(nswap) + ' tiles'
      activity.insert(0, act)
    else: 
      act = gamer + ' passed'
      activity.insert(0, act)
      self.gdata['cpasses'] += 1
      if (self.gdata['cpasses']) > (2 * len(self.players)):
        return 'endgame'
    turn = self.gdata['turn']
    nxtturn = False 
    while not nxtturn:
      turn = turn + 1
      if turn > 4:
        turn = 1
      name = self.getplayername(turn)
      if name != 'none':
        misser = self.gdata['misser']
        if name in misser:
          act = name + ' missed a turn for a wrong probe'
          activity.insert(0, act)
          misser.remove(name)
          self.gdata['misser'] = misser
        else:
          nxtturn = True
    self.gdata['turn'] = turn  
    with open(gamePath, "r") as file:
      data = json.load(file)
    data[self.gid] = self.gdata
    with open(gamePath, "w") as file:
      json.dump(data, file)

    return {'turn': turn, 'activity': activity}

  def createbaord(self, tiles, player):
    oboard = self.getBoard()
    board = copy.deepcopy(oboard)
    for bcode in list(tiles.keys()):
      py = ((letcode[bcode[0]]) - 1)
      px = (int(bcode[1:]) -1)
      board[py][px] = { 'pl': player, 'lp': tiles[bcode] }
    return board
  
  def probegame(self, tilesonboard, pwords, pscore, cplayer):
    board = self.createbaord(tilesonboard, 5)
    self.gdata['tilesonboard'] = tilesonboard
    self.gdata['pwords'] = pwords
    self.gdata['cplayer'] = cplayer 
    self.gdata['pscore'] = pscore
    self.gdata['cpasses'] = 0
    with open(gamePath, "r") as file:
      data = json.load(file)
    data[self.gid] = self.gdata
    with open(gamePath, "w") as file:
      json.dump(data, file)
    return board
  
  def getplayername(self, pid):
    for player in list(self.players.keys()):
      if (self.players[player]['id'] == str(pid)):
        return player
    return 'none'
  def presponse(self, gamer, response):
    probers = self.gdata['probers']
    probers[response].append(gamer)
    if ((len(probers['yes']) + len(probers['no'])) == (len(list(self.players.keys())) - 1)):
      self.gdata['probers'] = {'yes': [], 'no': []}
      activity = []
      score = 0
      cplayer = self.gdata['cplayer']
      words = self.gdata['pwords']
      if (len(probers['yes']) > 0):
        if (checkDictionary(words)):
          score = self.gdata['pscore']
          self.gdata['players'][cplayer]['score'] += score
          for a in probers['yes']:
            act = a + ' probed wrongly'
            activity.insert(0, act)
            self.gdata['misser'].append(a)
          act = cplayer + ' scored ' + str(score) + ' pts'
          activity.insert(0, act)
          board = self.createbaord(self.gdata['tilesonboard'], self.players[cplayer]['id'])
          self.gdata['board'] = board
          turn = self.gdata['turn']
          nxtturn = False 
          while not nxtturn:
            turn = turn + 1
            if turn > 4:
              turn = 1
            name = self.getplayername(turn)
            if name != 'none':
              misser = self.gdata['misser']
              if name in misser:
                act = name + ' missed a turn for a wrong probe'
                activity.insert(0, act)
                misser.remove(name)
                self.gdata['misser'] = misser
              else:
                nxtturn = True
          self.gdata['turn'] = turn  
          with open(gamePath, "r") as file:
            data = json.load(file)
          data[self.gid] = self.gdata
          with open(gamePath, "w") as file:
            json.dump(data, file)
          return {'gamer': cplayer, 'turn': turn, 'board': board, 'activity': activity, 'score': score, 'stat': 't', 'pwords': words}
        else:
          act = cplayer + 'Scored 0 for playing none existing word(s)'
          activity.insert(0, act)
          turn = self.gdata['turn']
          nxtturn = False 
          while not nxtturn:
            turn = turn + 1
            if turn > 4:
              turn = 1
            name = self.getplayername(turn)
            if name != 'none':
              misser = self.gdata['misser']
              if name in misser:
                act = name + ' missed a turn for a wrong probe'
                activity.insert(0, act)
                misser.remove(name)
                self.gdata['misser'] = misser
              else:
                nxtturn = True
          self.gdata['turn'] = turn
          board = self.board  
          with open(gamePath, "r") as file:
            data = json.load(file)
          data[self.gid] = self.gdata
          with open(gamePath, "w") as file:
            json.dump(data, file)
          return {'gamer': cplayer, 'turn': turn, 'board': board, 'activity': activity, 'score': score, 'stat': 'f'}
      else:
        score = self.gdata['pscore']
        self.gdata['players'][cplayer]['score'] += score
        board = self.createbaord(self.gdata['tilesonboard'], self.players[cplayer]['id'])
        self.gdata['board'] = board
        turn = self.gdata['turn']
        act = cplayer + ' scored ' + str(score) + ' pts'
        activity.insert(0, act)
        nxtturn = False 
        while not nxtturn:
          turn = turn + 1
          if turn > 4:
            turn = 1
          name = self.getplayername(turn)
          if name != 'none':
            misser = self.gdata['misser']
            if name in misser:
              act = name + ' missed a turn for a wrong probe'
              activity.insert(0, act)
              misser.remove(name)
              self.gdata['misser'] = misser
            else:
              nxtturn = True
        self.gdata['turn'] = turn  
        with open(gamePath, "r") as file:
          data = json.load(file)
        data[self.gid] = self.gdata
        with open(gamePath, "w") as file:
          json.dump(data, file)
        return {'gamer': cplayer, 'turn': turn, 'board': board, 'activity': activity, 'score': score, 'stat': 't', 'pwords': words }
        
    else:
      self.gdata['probers'] = probers
      with open(gamePath, "r") as file:
        data = json.load(file)
      data[self.gid] = self.gdata
      with open(gamePath, "w") as file:
        json.dump(data, file)
      return 'wait' 
  def cscores(self):
    endeddata = []
    scorelist = []
    enddata = self.gdata['endgame']
    tracksub = 0
    for gamer in enddata:
      tracksub += enddata[gamer]['rsub']
    for gamer in enddata:
      if enddata[gamer]['rsub'] == 0:
        enddata[gamer]['addition'] += tracksub 
        enddata[gamer]['nscore'] += tracksub
      scorelist.append(enddata[gamer]['nscore'])
    scorelist.sort(reverse=True)
    for a, b in enumerate(scorelist):
      for gamer in enddata:
        if enddata[gamer]['nscore'] == b:
          sact = ''
          if enddata[gamer]['rsub'] != 0:
            sact = '(' + str(enddata[gamer]['oscore']) + ' minus ' + str(enddata[gamer]['rsub']) + ')'
          elif enddata[gamer]['addition'] != 0:
            sact = '(' + str(enddata[gamer]['oscore']) + ' plus ' + str(enddata[gamer]['addition']) + ')'
          if a == 0 :
            act = 'WINNER: ' + gamer + ' Total score of ' + str(b) +  sact 
            endeddata.append(act)
          elif a == 1:
            act = '2ND PLACE: ' + gamer + ' Total score of ' + str(b) +  sact 
            endeddata.append(act)
          elif a == 2:
            act = '3RD PLACE: ' + gamer + ' Total score of ' + str(b) +  sact 
            endeddata.append(act)
          elif a == 3:
            act = '4TH PLACE: ' + gamer + ' Total score of ' + str(b) +  sact 
            endeddata.append(act)
          break
    return endeddata

  def endgame(self,gamer, rack):
    enddata = self.gdata['endgame']
    gameObject = materials()
    scores = gameObject.getscores()
    if gamer not in list(enddata.keys()):
      oldscore = self.players[gamer]['score']
      racksub = 0
      newscore = 0
      for i in rack:
        if i > 200: i = 200
        racksub += scores[str(i)]
      newscore = oldscore - racksub
      enddata[gamer] = {'oscore': oldscore, 'rsub': racksub, 'nscore': newscore, 'addition': 0}
    if len(enddata) == len(self.players):
      return self.cscores()
    else:
      self.gdata['endgame'] = enddata
      with open(gamePath, "r") as file:
        data = json.load(file)
      data[self.gid] = self.gdata
      with open(gamePath, "w") as file:
        json.dump(data, file)
      return 'wait' 

  def deletegame(self):
    with open(gamePath, "r") as file:
      data = json.load(file)
    del data[self.gid]
    with open(gamePath, "w") as file:
      json.dump(data, file)
    return 'wait' 