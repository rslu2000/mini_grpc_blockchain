這個迷你區塊鏈專案是由德明財經科技大學盧瑞山教授與他的學生助理研究員唐林竩所共同研究開發的。
本專案開發版本的演進過程請參考版本說明：version.md

# 套件
```
pip install -r pip_install.txt
```
# 執行
GRPC_PORT=[grpc_port] python2.7 manage.py runserver [webport]\
例如:
```
GRPC_PORT=9001 python2.7 manage.py runserver 9000
```
# /index 或 /
簡易留言板
# /JoinNode?target=ip:grpc_port
加入節點
# /Send (POST)
送出資料
# /ShowNodes
查看節點
# /ShowBlocks
查看區塊
