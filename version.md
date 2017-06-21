The mini_gRPC_blockchain was developed by Professor Lu,Ruei-Shan and his student research asistant, Tang 
Lin-Yi in Takming University of Science and Technology.

The v0.1 was redesigned to get implement of the mini-blockchain using gRPC with Protobuf. The original 
mini-blockchain was implemented by just using socket and threading modules. NO gRPC was used before v0.1. 

In v0.2 we not only use gRPC but alos we tried to pack the gRPC as a python package with the 
name-p2p_grpc_blockchain, then we uploaded 
"p2p_grpc_blockchain" to pypi site. (https://pypi.python.org/)

In v0.3 we define a simple block structure and include a consesus mechanism called proof of work(POW) in 
this version. No matter in v0.2 or 0.1, we immediately created one block as long as one message was sent 
out. In v0.3 we finally have a clear block architechture. When 1 minute is passing, one block will be 
generated. We designed to adjust the difficulty of POW everytime when 100 blocks were generated.


這個迷你區塊鏈專案是由德明財經科技大學盧瑞山教授與他的學生助理研究員唐林竩所共同研究開發的。

第v0.1版是以gRPC與Protobuf的技術來實作出迷你區塊鏈的。迷你區塊鏈的前身是僅以較底層的socket技術及多執行緒技術實現完成的。
在v0.1版以前，是完全還沒用到gRPC技術的。

到了第v0.2版，我們試著引入gRPC，同時我們也嘗試地把它打包成一個Python套件，並上傳到Python的套件匯集網站Pypi.
(https://pypi.python.org/)

到了第v0.3版，我們開始定義一個較明確的區塊結構，並且引入了共識機制中的工作量證明(POW)。之前無論是v0.1版還是v0.2版，我們的設計是一有消息發送出來就是產出一個塊。
但是到了v0.3版，我們終於有了一個比較明確的區塊架構。 
我們的設計是這樣的，每當一分鐘過去，就會有一個區塊被挖出來。我們的設計是每當有100個區塊產生的時候，就去調整工作量證明中的難度一次。
