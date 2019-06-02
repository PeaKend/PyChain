# PyChain

A small localhost blockchain in Python 3

## Usage

```
genesis.py
```

Creates the folder __data__ (where all the blocks are going to be created) and the __header__ of the Bitcoin __genesis block__.

```
mine.py
```

Mines for the next block using a __difficulty__ of 4 (4 0's for each new block). You can change the __difficulty__ variable in the script file.

```
client.py
```

Inserts __tx's__ inside the next block before they're mined.

```
utils.py
```

A __module__ containing the functions needed in the other scripts.

## Screenshots

Using __mine.py__ to find new blocks and __client.py__ to add transactions

![Mining with client](https://raw.githubusercontent.com/PeaKend/pychain/master/example_images/mining.png)

__Hexdump__ of a block without a transaction and a block with one

![Hexdump of blocks](https://raw.githubusercontent.com/PeaKend/pychain/master/example_images/hexdump.png)

