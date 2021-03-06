#-*- coding:utf-8 -*-

from django.db import connection

class SQLDbmpInceptionBusiness(object):

    def __ini__(self):
        pass

    def get_business_by_id(self, inception_business_id):
        """获得审核业务组信息"""
        if not inception_business_id:
            return None

        sql = """
            SELECT dib.inception_business_id,
                dib.inception_record_id,
                dib.mysql_business_id,
                dib.execute_status,
                dmb.name
            FROM dbmp_inception_business AS dib
            INNER JOIN dbmp_mysql_business AS dmb
                ON dib.mysql_business_id = dmb.mysql_business_id
                AND dib.inception_business_id = {inception_business_id}
        """.format(inception_business_id = inception_business_id)

        cursor = connection.cursor()
        cursor.execute(sql)
        results = self._dict_fetchone(cursor)
        return results

    def get_business_by_id_2(self, inception_business_id):
        """获得审核业务组信息"""
        if not inception_business_id:
            return None

        sql = """
            SELECT dib.inception_business_id,
                dib.inception_record_id,
                dib.mysql_business_id,
                dib.execute_status,
                dir.sql_text,
                dir.tag,
                dir.remark,
                dir.charset,
                dmb.name
            FROM dbmp_inception_business AS dib
            INNER JOIN dbmp_inception_record AS dir
                ON dib.inception_record_id = dir.inception_record_id
                AND dib.inception_business_id = {inception_business_id}
            INNER JOIN dbmp_mysql_business AS dmb
                ON dib.mysql_business_id = dmb.mysql_business_id
        """.format(inception_business_id = inception_business_id)

        cursor = connection.cursor()
        cursor.execute(sql)
        results = self._dict_fetchone(cursor)
        return results

    def find_businesses_by_inception_record_id(self, inception_record_id):
        """获得审核数据库信息"""
        if not inception_record_id:
            return None

        sql = """
            SELECT dib.inception_business_id,
                dib.inception_record_id,
                dib.mysql_business_id,
                dib.execute_status,
                dmb.name,
                dmb.remark
            FROM dbmp_inception_business AS dib
            INNER JOIN dbmp_mysql_business AS dmb
                ON dib.mysql_business_id = dmb.mysql_business_id
                AND dib.inception_record_id = {inception_record_id}
        """.format(inception_record_id = inception_record_id)

        cursor = connection.cursor()
        cursor.execute(sql)
        results = self._dict_fetchall(cursor)
        return results

    def _dict_fetchone(self, cursor):
        "转化所有的行为dict"
        columns = [col[0] for col in cursor.description]
        return dict(zip(columns, cursor.fetchone()))

    def _dict_fetchall(self, cursor):
        "转化所有的行为dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
