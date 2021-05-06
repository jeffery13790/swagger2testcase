create_case.py文件可以生成在testcases文件夹下的用例，
生成的用例需要填写对应的csv文件中的数据，
同时配置对应的函数：get_x_tenant_id(), get_base_url()。

get_swagger.py文件统计swagger的接口情况。
运行脚本:1, python create_case.py
				 2, python get_swagger.py
				 
				 
create_case.py生成半成品的用例*_test.py.infancy和对应的参数文件*.csv文件。
在使用的时候去掉用例文件的后缀名.infancy把文件转换为py文件，然后做后续的处理
使之生成完整的测试脚本。



##问题点：
当一个url地址对应于多个method的时候，参数会串。这个需要修改。