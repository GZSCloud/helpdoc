'''
help(docx)，dir(document),document.__doc__，python -m pydoc -p 1234等措施，都难以查看import进来的模块，github上往往只有代码， 没有帮助文件，只有在pypi中找到模块，进入模块的主页，再跳过去查看documentation。如python-docx就是如此。
应用scrapy开发一个爬虫，输入一个模块名称就能够将它的documentation爬下来，合并为一个md文件，保留文档格式。(:- 文档多半是pydoc生成的 :-)
'''
# 参考系列文章：https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html
