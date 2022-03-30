from uuid import uuid4

from django.utils import timezone
from django.http import Http404
from braces.views import CsrfExemptMixin
from rest_framework.views import APIView
from rest_framework.response import Response

from .blockchain import Blockchain


# Creating our Blockchain
blockchain = Blockchain()
# Creating an address for the node running our server
node_address = uuid4().hex
root_node = 'e36f0158f0aed45b3bc755dc52ed4560d'


class MineBlockAPIView(APIView):
    """
    Mining a new block
    """

    def get(self, request, *args, **kwargs):
        previous_block = blockchain.get_last_block()
        previous_nonce = previous_block['nonce']
        nonce = blockchain.proof_of_work(previous_nonce)
        previous_hash = blockchain.hash(previous_block)
        blockchain.add_transaction(
            sender=root_node,
            receiver=node_address,
            amount=1.15,
            time=timezone.now().isoformat()
        )
        block = blockchain.create_block(nonce, previous_hash)

        data = {
            'message': 'Congratulations, you just mined a block!',
            'index': block['index'],
            'timestamp': block['timestamp'],
            'nonce': block['nonce'],
            'previous_hash': block['previous_hash'],
            'transactions': block['transactions']
        }

        return Response(data)


class GetChainAPIView(APIView):
    """
    Getting the full Blockchain
    """

    def get(self, request, *args, **kwargs):
        data = {'chain': blockchain.chain, 'length': len(blockchain.chain)}
        return Response(data)


class IsValidAPIView(APIView):
    """
    Checking if the Blockchain is valid
    """

    def get(self, request, *args, **kwargs):
        if blockchain.is_chain_valid(blockchain.chain):
            data = {'message': 'All good. The Blockchain is valid.'}
        else:
            data = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}

        return Response(data)


class AddTransactionAPIView(CsrfExemptMixin, APIView):
    """
    Adding a new transaction to the Blockchain
    """

    def post(self, request, *args, **kwargs):
        transaction_keys = ['sender', 'receiver', 'amount', 'time']

        if not all(key in request.data for key in transaction_keys):
            return Http404('Some elements of the transaction are missing')

        index = blockchain.add_transaction(
            request.data['sender'],
            request.data['receiver'],
            request.data['amount'],
            request.data['time'],
        )
        data = {'message': f'This transaction will be added to Block {index}'}

        return Response(data)


class ConnectNodeAPIView(CsrfExemptMixin, APIView):
    """
    Connecting new nodes
    """

    def post(self, request, *args, **kwargs):
        nodes = request.data.get('nodes')

        if nodes is None:
            return Http404("No node")

        for node in nodes:
            blockchain.add_node(node)

        data = {
            'message': 'All the nodes are now connected. The Sudocoin Blockchain now contains the following nodes:',
            'total_nodes': list(blockchain.nodes)
        }

        return Response(data)


class ReplaceChainAPIView(APIView):
    """
    Replacing the chain by the longest chain if needed
    """

    def get(self, request, *args, **kwargs):
        if blockchain.replace_chain():
            data = {
                'message': 'The nodes had different chains so the chain was replaced by the longest one.',
                'new_chain': blockchain.chain
            }
        else:
            data = {
                'message': 'All good. The chain is the largest one.',
                'actual_chain': blockchain.chain
            }

        return Response(data)
