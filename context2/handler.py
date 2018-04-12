# -*- coding:utf-8 -*-
import boto3
import os.path


class S3Access:
    s3 = None

    def __init__(self):
        self.s3 = boto3.client('s3')

    def upload(self, bucketname, uploadfilepath, s3folder):
        """
        S3へアップロード
        @param bucketname S3バケット名
        @param uploadfilepath アップロードするファイルのパス
        @param s3folder S3バケットの下のフォルダパス（ファイル名は含まない）
        """
        basefilename = os.path.basename(uploadfilepath)
        s3filepath = s3folder + '/' + basefilename
        self.s3.upload_file(uploadfilepath, bucketname, s3filepath)
