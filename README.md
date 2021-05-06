用例生成脚本介绍：
    通过脚本可以把swagger接口信息转换为httprunner的测试脚本，同时保存本次swagger信息history_time.json以及和上次信息对比本次生成代码中跟新了那些接口信息update_time.json。
    脚本在生成用例的时候会先把历史记录（最后的一次历史记录）和最新的swagger内容进行对比，如果同名的接口有改变，则把修改以后的接口和新增的接口内容记录下来，保存到
    update_time.json中。update_time.json为本次脚本运行的时候需要生成的脚本内容信息。
    脚本运行步骤：在create_case.py中配置url_dict信息。url_dict中配置了swagger地址url，url为swagger的数据信息地址，通过http协议get方法可以获取到swagger中接口信息内容。
                prefix信息为前缀信息，swagger中的接口路径最终形成url地址信息形式为：http[s]://host:port/prefix/path。
                parameter_key为公共的参数的键，会在最终生成的用例脚本中的参数位置。
                parameter_value为公共参数的参数数据地址，会和parameter_key一起生成用例脚本的参数。
                生成用例的时候运行python create_case.py文件，会在create_case.py文件夹下生成history文件夹用于记录swagger数据以及update数据，生成testcases的用例文件。

生成用例的介绍：最终会生成用例路径testcases/api/module/tags/paths/接口_method.py.infancy和testcases/api/module/tags/paths/接口_method.csv两个文件。
        testcases/api/module/tags/paths/接口_method.py.infancy文件为脚本文件，再后续编写文件的时候把.infancy去掉转化为.py文件，py文件进行参数化的处理。
        testcases/api/module/tags/paths/接口_method.csv文件为参数化文件，在编写脚本的时候把参数写在该文件中。
