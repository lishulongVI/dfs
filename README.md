# fastdfs 分布式存储系统

https://github.com/happyfish100/fastdfs

```
1、海量存储
2、重复文件妙传


FastDFS是一个开源的高性能分布式文件系统。
它的主要功能包括：
    文件存储，文件同步和文件访问（文件上传和文件下载），它可以解决高容量和负载平衡问题。
    FastDFS应满足基于照片共享站点和视频共享站点等文件服务的网站的要求。

FastDFS有两个角色：
    跟踪器和存储。
    跟踪器负责文件访问的调度和负载平衡。
    存储存储文件及其功能是文件管理，包括：文件存储，文件同步，提供文件访问接口。
    它还管理元数据，这些元数据表示为文件的键值对。例如：width = 1024，键为“width”，值为“1024”。

FastDFS is an open source high performance distributed file system. It's major functions include: file storing, file syncing and file accessing (file uploading and file downloading), and it can resolve the high capacity and load balancing problem. FastDFS should meet the requirement of the website whose service based on files such as photo sharing site and video sharing site.

FastDFS has two roles: tracker and storage. The tracker takes charge of scheduling and load balancing for file access. The storage store files and it's function is file management including: file storing, file syncing, providing file access interface. It also manage the meta data which are attributes representing as key value pair of the file. For example: width=1024, the key is "width" and the value is "1024".

The tracker and storage contain one or more servers. The servers in the tracker or storage cluster can be added to or removed from the cluster by any time without affecting the online services. The servers in the tracker cluster are peer to peer.

The storarge servers organizing by the file volume/group to obtain high capacity. The storage system contains one or more volumes whose files are independent among these volumes. The capacity of the whole storage system equals to the sum of all volumes' capacity. A file volume contains one or more storage servers whose files are same among these servers. The servers in a file volume backup each other, and all these servers are load balancing. When adding a storage server to a volume, files already existing in this volume are replicated to this new server automatically, and when this replication done, system will switch this server online to providing storage services.

When the whole storage capacity is insufficiency, you can add one or more volumes to expand the storage capacity. To do this, you need to add one or more storage servers.

The identification of a file is composed of two parts: the volume name and the file name.

Client test code use client library please refer to the directory: client/test.

```


## docker

from https://github.com/happyfish100/fastdfs/blob/master/docker/dockerfile_network/README.md

```
docker run -d -e FASTDFS_IPADDR=192.168.1.234 -p 8888:8888 -p 22122:22122 -p 23000:23000 -p 8011:80 --name test-fast 镜像id/镜像名称
```

