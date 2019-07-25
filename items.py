# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AminerItem(scrapy.Item):
    # define the fields for your item here like:
    paper_id=scrapy.Field()#论文编号
    author_link = scrapy.Field()  #作者链接
    title_zh=scrapy.Field()#论文标题中文
    title_en=scrapy.Field()#论文标题英文
    keywords_zh=scrapy.Field()#论文关键词
    keywords_en=scrapy.Field()
    abstract_zh=scrapy.Field()#论文摘要
    abstract_en=scrapy.Field()
    author_zh=scrapy.Field()#作者列表
    author_en=scrapy.Field()
    author_affi_zh=scrapy.Field()#作者单位列表
    author_affi_en=scrapy.Field()
    emails_list=scrapy.Field()#作者邮箱列表
    corresponding_author=scrapy.Field()#通信作者列表
    corresponding_author_email=scrapy.Field()#通讯作者email
    type=scrapy.Field()#文献类型
    doi=scrapy.Field()#论文DOI编号
    language=scrapy.Field()#语言
    paper_year=scrapy.Field()#出版年份
    cited_number=scrapy.Field()#引用频次
    journal_conf=scrapy.Field()#期刊、会议名称
    journal_conf_en=scrapy.Field()
    pdf=scrapy.Field()#全文链接
    page_start=scrapy.Field()#起始页码
    page_end=scrapy.Field()#终止页码
    h_index=scrapy.Field()#h指数
    paper_num=scrapy.Field()#文章数量
    author_citation=scrapy.Field()#作者总引用数
    author_id=scrapy.Field()#作者id
    organization=scrapy.Field()#机构名称
    author_title=scrapy.Field()#作者职称
    nation=scrapy.Field()#国家

    volume=scrapy.Field()#卷
    issue=scrapy.Field()#期
    article_number=scrapy.Field()#文献号
    issn=scrapy.Field()#期刊或会议集ISSN
    isbn=scrapy.Field()#国际标准书号ISBN
    funding=scrapy.Field()#致谢
    research_direction=scrapy.Field()#分类或研究方向
    conf_location=scrapy.Field()#会议地点
    conf_time=scrapy.Field()#会议时间
    source_id=scrapy.Field()#论文数据来源
    included=scrapy.Field()#论文收录信息
    paper_order=scrapy.Field()#论文在关键词搜索中排序
    create_at=scrapy.Field()#创建时间
    update_at=scrapy.Field()#修改时间
    delete_at=scrapy.Field()#删除时间
    is_deleted=scrapy.Field()#是否已删除
    mark=scrapy.Field()#备注

    title = scrapy.Field()
    author1 = scrapy.Field()
    author2 = scrapy.Field()
    href=scrapy.Field()
    abstract = scrapy.Field()
    publish_time=scrapy.Field()
    pass
