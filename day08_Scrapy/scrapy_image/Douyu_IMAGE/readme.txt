��������ͼƬ����

����: offset����ƫ�����Ĳ���
Ĭ��60������, limit--->100����100, ����֮����ʾ-->60
offset--->��ǰ���������й�
һ�λ�ȡ100��--limit
offset += 100 --->�Ƴ�ֹͣ������--->�ж�ָ����ֵΪ��

�ֶ�����ץȡ:
room_id
image_src
nick_name
city


ע���:
image_path--->�������ļ���ֱ�Ӵ洢���ݿ�, �洢��Դ�ļ���Ӳ����ľ���·��

scrapy��ר������ͼƬ�Ĺܵ���
PIL��ͼƬ�洢
get_media_request()--->���ܽ���item����
def get_media_request(self, item, info)  # ��������
	return [Request(x) for x in item.get(self.image_urls_field, [])]  # returnֱ�ӷ���һ���б������е��������������  --->���������ÿһ������
or
	for x in item.get(xxx):
	yield Request(x)  # yield����һ������, ����һ��������  --->���������ÿһ������
def item_completed(self, results, item, info):  # 
	if isinstance(item, dict) or self.images_result_field in item.fields:
		item[self.image_result_field]  = [x for ok, x in result if ok]
		# [x for ok, x in result if ok]-->����洢item���iamge�ֶ�
	return item 
------>ȡ��ͼƬ��url��ַ��������Ȼ��洢����item����ֶ�

Douyu  �����full�ļ�Ĭ�Ͼͻ�浽����, ָ�������ָ�����ļ���

��������