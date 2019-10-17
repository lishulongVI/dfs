## MinIo 

> 开源的对象存储服务，兼容s3云存储服务接口，非常适合存储大容量非结构化的数据。图片，视频，日志文件，备份数据和 容器，虚拟机镜像等，而一个对象文件是可以是任意大小的，[kb,5T]
>
> 轻量的服务，有js ，python ，go ，java 等sdk



## 快速启动

1. https://docs.min.io/cn/minio-docker-quickstart-guide.html

   ```
   docker run -p 9000:9000 --name minio1 \
     -e "MINIO_ACCESS_KEY=minio" \
     -e "MINIO_SECRET_KEY=minio123" \
     -v /Users/li/Desktop/minio/data:/data \
     -v /Users/li/Desktop/minio/config:/root/.minio \
     minio/minio server /data
     
     
     
     
   Object API (Amazon S3 compatible):
      Go:         https://docs.min.io/docs/golang-client-quickstart-guide
      Java:       https://docs.min.io/docs/java-client-quickstart-guide
      Python:     https://docs.min.io/docs/python-client-quickstart-guide
      JavaScript: https://docs.min.io/docs/javascript-client-quickstart-guide
      .NET:       https://docs.min.io/docs/dotnet-client-quickstart-guide
   ```

2. 在Docker中运行MinIO分布式模式

   > 分布式MinIO可以通过 [Docker Compose](https://docs.min.io/cn/deploy-minio-on-docker-compose) 或者 [Swarm mode](https://docs.min.io/cn/deploy-minio-on-docker-swarm)进行部署。这两者之间的主要区别是Docker Compose创建了单个主机，多容器部署，而Swarm模式创建了一个多主机，多容器部署。
   >
   > 这意味着Docker Compose可以让你快速的在你的机器上快速使用分布式MinIO-非常适合开发，测试环境；而Swarm模式提供了更健壮，生产级别的部署。



## Minui 纠删码快速入门

> 使用erasure code 和 checksum 来保护数据免受硬件故障和无声数据的损坏，即时丢失一半的硬盘，也可以恢复数据





## 分布式

```
export MINIO_ACCESS_KEY=<ACCESS_KEY>
export MINIO_SECRET_KEY=<SECRET_KEY>
minio server http://192.168.1.11/export1 http://192.168.1.11/export2 \
               http://192.168.1.11/export3 http://192.168.1.11/export4 \
               http://192.168.1.12/export1 http://192.168.1.12/export2 \
               http://192.168.1.12/export3 http://192.168.1.12/export4 \
               http://192.168.1.13/export1 http://192.168.1.13/export2 \
               http://192.168.1.13/export3 http://192.168.1.13/export4 \
               http://192.168.1.14/export1 http://192.168.1.14/export2 \
               http://192.168.1.14/export3 http://192.168.1.14/export4
```









## SDK











DW ：data warehouse 翻译成数据仓库
DW数据分层，由下到上为 DWD,DWB,DWS
DWD：data warehouse detail 细节数据层，有的也称为 ODS层，是业务层与数据仓库的隔离层
DWB：data warehouse base 基础数据层，存储的是客观数据，一般用作中间层，可以认为是大量指标的数据层。
DWS：data warehouse service 服务数据层，基于DWB上的基础数据，整合汇总成分析某一个主题域的服务数据，一般是宽表。





