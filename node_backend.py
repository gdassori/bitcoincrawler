__author__ = 'mirko'

class NodeBackend(object):
    def get_block(self, block_num=None, block_hash=None):
        raise NotImplementedError

    def get_mempool_txs(self):
        raise NotImplementedError

    def get_inputs_from_transaction(self, tx):
        raise NotImplementedError

    def get_outputs_from_transaction(self, tx):
        raise NotImplementedError

    def get_transactions_from_block(self, block):
        raise NotImplementedError

    def get_missing_blocks(self, cur_block, margin_blocks):
        raise NotImplementedError
