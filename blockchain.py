from block import Block

class Blockchain:
    """
    Blockchain: public ledger of transactions
    A list of blocks - datasets of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        last_block = self.chain[-1]

        self.chain.append(Block.mine_block(last_block, data))

    def __repr__(self):
        return f'Blockchain : {self.chain}'

def main():

    blockchain = Blockchain()
    blockchain.add_block('test')
    blockchain.add_block('test2')

    print(blockchain)

    print(f'blockchain.py __name__: {__name__}')

if __name__ == '__main__':
    main()