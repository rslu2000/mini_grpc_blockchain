#coding:utf-8
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from p2ptest.p2p import p2p
from p2ptest.enum.enum import *
from p2ptest.block import block

def index(request):
    try:
        body = request.POST["data"]
        b = block.Block()
        b.create(body.encode('utf-8'))
        print("<= [broadcast Block]:%s" % b.pb2.blockhash)
        p2p.Node.broadcast(SERVICE*TRANSACTION+BLOCKBROADCAST,b.pb2)
        return HttpResponseRedirect('/index')
    except Exception as e:
        pass
    blocks=block.Chain.showtolist()
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
        reponse += "%s\n<br>" % node
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
    response = block.Chain.show()
    response=response.replace('\r\n','<br><br>')
    return HttpResponse(response)
