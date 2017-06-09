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
