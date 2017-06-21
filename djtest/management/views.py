#coding:utf-8
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from p2p_grpc_blockchain.p2p import p2p
from p2p_grpc_blockchain.enum.enum import *
from p2p_grpc_blockchain.block import block
from p2p_grpc_blockchain.transaction import transaction
import time

def index(request):
    try:
        body = request.POST["data"]
        tx = transaction.Transaction()
        tx.create(body.encode('utf-8'))
        print("<= [broadcast Tx]:%s" % tx.pb2.txhash)
        tx.Broadcast()
        return HttpResponseRedirect('/index')
    except Exception as e:
        print (e)
    blocks=block.Chain.showtolist()
    txsdict=transaction.Transaction.Transactions
    for box in blocks:
        blocktxs=[]
        box.time=time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(float(box.pb2.unixtime)+28800))
        for txhash in box.pb2.txshash:
            blocktxs.append({"time":time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(float(txsdict[txhash].pb2.unixtime)+28800)),"body":txsdict[txhash].pb2.body })
            box.txs=blocktxs

    return render(request,'index.html',{"blocks":blocks})



def JoinNode(request):
    target = ""
    try:
        target = request.GET["target"]
    except:
        target = "127.0.0.1:8001"
    resule = "JoinNode%s" % ("Success" if p2p.grpcJoinNode(target) else "Fails")
    return HttpResponseRedirect('/index')
    
def ShowNodes(request):
    nodeslist = list(p2p.Node.getNodesList())
    response = ""
    for node in nodeslist:
        response += "%s\n<br>" % node
    return HttpResponse(response)

def Send(request):
    body = request.body
    beforeH = block.Chain.getHeight()
    b = block.Block()
    b.create(body)
    afterH = block.Chain.getHeight()
    if afterH-beforeH == 1:
        print("<= [broadcast Block]:%s" % b.pb2.blockhash)
        p2p.Node.broadcast(SERVICE*TRANSACTION+BLOCKBROADCAST,b.pb2)
    return HttpResponse("test \n")

def ShowBlocks(request):
    response=block.Chain.showtolist()
    
    return render(request,'showblock.html',{"blocks":response})
