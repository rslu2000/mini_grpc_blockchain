#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from p2ptest.p2p import p2p
from p2ptest.enum.enum import *
from p2ptest.block import block


def JoinNode(request):
    target = ""
    try:
        target = request.GET["target"]
    except:
        target = "127.0.0.1:8001"
    resule = "JoinNode%s" % ("Success"  if p2p.grpcJoinNode(target) else "Fails")
    return HttpResponse(resule)
    
def ShowNodes(request):
    nodeslist = list(p2p.Node.getNodesList())
    response = ""
    for node in nodeslist:
        reponse += "%s\n" % node
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