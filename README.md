# PyChain

A small localhost blockchain written in Python 3

## Usage

```
genesis.py
```

Creates the __header__ of the genesis block (_using Bitcoin genesis in this case_)

```
mine.py
```

Mines for the next block using a __difficulty__ of 4 (4 0's for each new block). You can change the __difficulty__ variable in the script file

```
client.py
```

Inserts __tx's__ inside the next block before they're mined

```
utils.py
```

A __module__ containing the functions needed in the other scripts

## Screenshots

Using __mine.py__ to find new blocks and __client.py__ to add transactions

![Mining with client](https://raw.githubusercontent.com/PeaKend/pychain/master/example_images/mining.png)

__Hexdump__ of a block without a transaction and a block with one

![Hexdump of blocks](https://raw.githubusercontent.com/PeaKend/pychain/master/example_images/hexdump.png)

## Authors

* __Facundo Atrio__ - _Project_

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



