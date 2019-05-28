#!/usr/bin/env python3

import utils
import codecs

gen_version =     b'01000000'
gen_prev_block =  b'0000000000000000000000000000000000000000000000000000000000000000'
gen_merkle_root = b'3BA3EDFD7A7B12B27AC72C3E67768F617FC81BC3888A51323A9FB8AA4B1E5E4A'
gen_timestamp =   b'29AB5F49'
gen_bits =        b'FFFF001D'
gen_nonce =       b'1DAC2B7C'

gen_hex =         (
                  gen_version +
                  gen_prev_block +
                  gen_merkle_root +
                  gen_timestamp +
                  gen_bits +
                  gen_nonce
                  )

open('data/' + utils.getHash(gen_hex) + '.bin', 'w').write('')

open('data/' + utils.getHash(gen_hex) + '.bin', 'ab').write(codecs.decode(gen_version, 'hex'))
open('data/' + utils.getHash(gen_hex) + '.bin', 'ab').write(codecs.decode(gen_prev_block, 'hex'))
open('data/' + utils.getHash(gen_hex) + '.bin', 'ab').write(codecs.decode(gen_merkle_root, 'hex'))
open('data/' + utils.getHash(gen_hex) + '.bin', 'ab').write(codecs.decode(gen_timestamp, 'hex'))
open('data/' + utils.getHash(gen_hex) + '.bin', 'ab').write(codecs.decode(gen_bits, 'hex'))
open('data/' + utils.getHash(gen_hex) + '.bin', 'ab').write(codecs.decode(gen_nonce, 'hex'))
