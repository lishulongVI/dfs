from minio import Minio

min_io = Minio(
    endpoint='127.0.0.1:9001',
    access_key='minio',
    secret_key='minio123',
    secure=False
)

if __name__ == '__main__':

    # 创建bucket
    for i in ["hello", 'world', 'kzy', 'cars']:
        if min_io.bucket_exists(i) is False:
            min_io.make_bucket(i)
    # 读取bucket
    for i in min_io.list_buckets():
        print(i.name, i.creation_date)
        # min_io.remove_bucket(i.name)
        # print(min_io.get_bucket_policy(i.name))

    # 写文件
    a = min_io.fput_object('hello', "txt", "./requirements.txt")
    print(a)
    # 下载文件
    min_io.fget_object(bucket_name='hello', object_name='txt', file_path='a1.txt')

    # 读数据
    c = min_io.get_object(bucket_name='hello', object_name='txt')

    print(c.read())

    # 查询bucket里的文件信息
    objects = min_io.list_objects(bucket_name='hello')

    for obj in objects:
        print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
              obj.etag, obj.size, obj.content_type)

    objects = min_io.list_objects_v2('hello',
                                     recursive=True)
    for obj in objects:
        print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
              obj.etag, obj.size, obj.content_type)

    # 获取到上传的文件url
    # min_io.fput_object(bucket_name='world', object_name='123.png', file_path='./66-1ZF2143214E2.png')
    print(min_io.presigned_get_object('world', '123.png', response_headers={
        'Content-Type': 'image/png',
        "Content-Disposition": 'inline;filename="image.png"'
    }))

    # 删除bucket
    # for i in min_io.list_buckets():
    #     min_io.remove_bucket(i.name)
