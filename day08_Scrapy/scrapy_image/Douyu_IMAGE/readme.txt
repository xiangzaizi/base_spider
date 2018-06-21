斗鱼下载图片案例

规律: offset数据偏移量的测试
默认60个数据, limit--->100以内100, 过了之后显示-->60
offset--->当前在线人数有关
一次获取100个--limit
offset += 100 --->推出停止的条件--->判断指定的值为空

字段数据抓取:
room_id
image_src
nick_name
city


注意点:
image_path--->二进制文件不直接存储数据库, 存储资源文件在硬盘里的绝对路径

scrapy有专门下载图片的管道类
PIL做图片存储
get_media_request()--->不能接收item数据
def get_media_request(self, item, info)  # 发送请求
	return [Request(x) for x in item.get(self.image_urls_field, [])]  # return直接返回一个列表返回所有的请求给引擎下载  --->给引擎迭代每一个对象
or
	for x in item.get(xxx):
	yield Request(x)  # yield返回一个对象, 当成一个生成器  --->给引擎迭代每一个对象
def item_completed(self, results, item, info):  # 
	if isinstance(item, dict) or self.images_result_field in item.fields:
		item[self.image_result_field]  = [x for ok, x in result if ok]
		# [x for ok, x in result if ok]-->拆包存储item这个iamge字段
	return item 
------>取出图片的url地址发送请求然后存储数据item这个字段

Douyu  里面的full文件默认就会存到这里, 指定后就是指定的文件夹

测试数据