from minio import Minio

min_io = Minio(
    endpoint='127.0.0.1:9000',
    access_key='minio',
    secret_key='minio123',
    secure=False
)

# min_io.make_bucket('hello')

name = 'demo.pdf'
name_zip = 'demo.zip'

path = './demo.pdf'
path_zip = './demo.zip'

min_io.fput_object('hello', name, path)

import zipfile

fzip = zipfile.ZipFile(name_zip, 'w', zipfile.ZIP_DEFLATED)

fzip.write(path)

fzip.close()
min_io.fput_object('hello', name_zip, path_zip)

import subprocess


def compress_file(path):
    """
    音频合并
    :return:
    """
    path_split = path.split('/')
    base_path = '/'.join(path_split[:-1])
    file_name = path_split[-1]
    cmd = 'cd {} && ffmpeg -i "{}" -b:a 32k -acodec mp3 -ar 44100 -ac 1 "de_{}" -y'.format(base_path, file_name,
                                                                                           file_name)

    a = subprocess.call(cmd, shell=True)
    if a != 0:
        return '', False
    return '{}/de_{}'.format(base_path, file_name), True


if __name__ == '__main__':
    print(compress_file('./path/1017.wav'))
