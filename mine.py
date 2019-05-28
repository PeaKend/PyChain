#!/usr/bin/env python3

import utils
import codecs
import os
import sys

##############
difficulty = 4
##############

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def mineNewBlock(prevBlock = utils.getLastBlock(), debug = False):
  while True:
    nonce = utils.setNonce()
    timestamp = utils.setTimestamp()
    prevBlock = codecs.decode(prevBlock, 'hex')
    prevBlock = codecs.encode(prevBlock, 'hex')

    block = (
            utils.setVersion() +
            prevBlock +
            utils.setMerkleRoot() +
            timestamp +
            utils.setBits() +
            nonce
            )

    nonce = utils.setNonce()
    block = utils.getHash(block)
    print('Trying nonce: ' + str(nonce))
    sys.stdout.write(CURSOR_UP_ONE)
    sys.stdout.write(ERASE_LINE)
    if debug == True:
      print('BLOCK:', block)

    if block[:difficulty] == '0' * difficulty and block[difficulty:difficulty+1] != '0':
      if utils.getTx() != '':
        print('BLOCK FOUND:\n' + block + '\ntx: ' + '\'' + utils.getTx() + '\'')
      else:
        print('BLOCK FOUND:\n' + block + '\ntx: \'\'')
      utils.createBlock(block)
      utils.writeToBlock(block, utils.setVersion(), utils.getLittleEndian(prevBlock), utils.setMerkleRoot(), timestamp, utils.setBits(), nonce)
      utils.writeTx(block)
      utils.createNewTxFile()
      return mineNewBlock(block)

mineNewBlock()
