#!/usr/bin/env python3

import hashlib
import codecs
import time
import random
import os

# declare beginning and end of byte values
version_position     = { "begin" : 0,   "end" : 8   }
prev_block_position  = { "begin" : 8,   "end" : 72  }
merkle_root_position = { "begin" : 72,  "end" : 136 }
timestamp_position   = { "begin" : 136, "end" : 144 }
bits_position        = { "begin" : 144, "end" : 152 }
nonce_position       = { "begin" : 152, "end" : 160 }

def getHash(block):
  block_bin = codecs.decode(block, 'hex')
  block_hash = hashlib.sha256(hashlib.sha256(block_bin).digest()).digest()
  block_hash = codecs.encode(block_hash[::-1], 'hex').decode('ascii')
  return block_hash

def getLittleEndian(_hash):
  _hash = codecs.decode(_hash, 'hex')
  return str.encode(codecs.encode(_hash[::-1], 'hex').decode('ascii'))

def getVersion(block_name):
  return open('data/' + block_name, 'rb').read()[version_position["begin"]:version_position["end"]]

def getPrevBlock(block_name):
  return open('data/' + block_name, 'rb').read()[prev_block_position["begin"]:prev_block_position["end"]]

def getMerkleRoot(block_name):
  return open('data/' + block_name, 'rb').read()[merkle_root_position["begin"]:merkle_root_position["end"]]

def getTimestamp(block_name):
  return open('data/' + block_name, 'rb').read()[timestamp_position["begin"]:timestamp_position["end"]]

def getBits(block_name):
  return open('data/' + block_name, 'rb').read()[bits_position["begin"]:bits_position["end"]]

def getNonce(block_name):
  return open('data/' + block_name, 'rb').read()[nonce_position["begin"]:nonce_position["end"]]

def getBlockList():
  for _file in os.listdir('data/'):
    print(_file)

def getTx():
  tx = open('tx', 'r').read()
  return tx

def setVersion(version = b'01000000'):
  return version

def getLastBlock():
  last_block_time = 0
  last_block_name = ''
  for _file in os.listdir('data/'):
    block = open('data/' + _file, 'rb').read()
    block = codecs.encode(block, 'hex')
    block_time = block[136:144]
    if block_time != b'':
      block_time = int(block_time, 16).to_bytes(4, 'little')
      block_time = codecs.encode(block_time, 'hex')
      block_time = int(block_time, 16)
      if block_time > last_block_time:
        last_block_time = block_time
        last_block_name = _file
  return last_block_name[0:64]

def setPrevBlock(block_name):
  prev_block = open('data/' + block_name, 'rb').read()
  prev_block = codecs.encode(prev_block, 'hex')
  prev_block = getHash(prev_block)
  prev_block = codecs.encode(prev_block, 'ascii')
  return prev_block

def createNewTxFile():
  return open('tx', 'w').write('')

def setMerkleRoot():
  tx = open('tx', 'r').read()
  tx = str.encode(tx)
  tx_hash = hashlib.sha256(hashlib.sha256(tx).digest()).digest()
  tx_hash = codecs.encode(tx_hash[::-1], 'hex').decode('ascii')
  return str.encode(tx_hash)

def setTimestamp():
  timestamp = int(time.time()).to_bytes(4, 'little')
  timestamp = codecs.encode(timestamp, 'hex')
  return timestamp

def setBits():
  return b'FFFF001D'

def setNonce():
  nonce = random.randint(0, 4294967295).to_bytes(4, 'little')
  nonce = codecs.encode(nonce, 'hex')
  return nonce

def createBlock(block_name):
  open('data/' + block_name + '.bin', 'w').write('')

def writeToBlock(block_name, version, prev_block, merkle_root, timestamp, bits, nonce):
  open('data/' + block_name + '.bin', 'ab').write(codecs.decode(version, 'hex'))
  open('data/' + block_name + '.bin', 'ab').write(codecs.decode(prev_block, 'hex'))
  open('data/' + block_name + '.bin', 'ab').write(codecs.decode(merkle_root, 'hex'))
  open('data/' + block_name + '.bin', 'ab').write(codecs.decode(timestamp, 'hex'))
  open('data/' + block_name + '.bin', 'ab').write(codecs.decode(bits, 'hex'))
  open('data/' + block_name + '.bin', 'ab').write(codecs.decode(nonce, 'hex'))

def writeTx(block_name):
  tx = open('tx', 'r').read()
  tx = codecs.encode(str.encode(tx), 'hex')
  open('data/' + block_name + '.bin', 'ab').write(codecs.decode(tx, 'hex'))
