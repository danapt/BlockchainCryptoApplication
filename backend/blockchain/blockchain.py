from backend.blockchain.block import Block


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

    def replace_chain(self, chain):
        """
        Replace the local chain with incoming one if the following applies:
        - the incoming chain is longer than the local one.
        - the incoming chain is formatted properly
        """
        if len(chain) <= len(self.chain):
             raise Exception('Cannot replace. the incoming chain must be longer.')

        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'Can not replace. the incoming chain is invalid: {e}')

        self.chain = chain

    @staticmethod
    def is_valid_chain(chain):
        """
        Validate the incoming chain.
        Enforce the following rules of blockchain:
            - teh cain must start with genesis block
            - blocks must be formatted correctly
        """
        if chain[0] != Block.genesis():
            raise  Exception('the genesis block must be valid')
        for i in range(1,len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block,block)




def main():
    blockchain = Blockchain()
    blockchain.add_block('test')
    blockchain.add_block('test2')

    print(blockchain)

    print(f'blockchain.py __name__: {__name__}')


if __name__ == '__main__':
    main()
