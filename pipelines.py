# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import datetime
import time
class AminerPipeline(object):
    def __init__(self):
        #连接数据库，抛出异常
        try:
            self.conn = pymysql.connect(host="rm-bp151dcc75aycqd80to.mysql.rds.aliyuncs.com", user="root", passwd="Iscas123",db="knowledgeproject", port=3306, charset='utf8')
            print("数据库连接")
        except Exception as e:
            print("Error!:{0}".format(e))
        time.sleep(5)
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        #将抓取的item项里面的内容，赋值给相应的变量，这里的变量都是数据库中的字段名

        dt=datetime.datetime.now().strftime('"%Y-%m-%d %H:%M:%S"')#获取当前系统时间，并按照数据库的格式转化
        #往数据库里插入数据，并捕获异常
        print('插入数据')
        sql="insert into cra_paper(title_zh,title_en,,authors_zh,authors_en,corresponding_author,corresponding_author_email,type,doi,language,journal_conf,journal_conf_en,page_start,page_end,paper_year,cited_number,pdf,source_id)" \
            " values(item['title_zh'],item['title_en'],item['authors_zh'],item['authors_en'],item['corresponding_author'],item['corresponding_author_email'],item['type'],item['doi'],item['language'],item['journal_conf'],item['journal_conf_en'],item['page_start'],item['page_end'],item['paper_year'],item['cited_number'],item['pdf'],item['source_id'])"
        try:
            self.conn.query(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()  # 如果出错就回滚并且抛出错误收集错误信息。
            print("Error!:{0}".format(e))
        return item
    def close_spider(self,spider):
        #关闭数据库连接
        self.conn.close()

