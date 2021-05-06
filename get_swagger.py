import requests
import pandas as pd




def getParameter(data):
    parameters = {}
    if isinstance(data, list):
        for par in data:
            if isinstance(par, dict):
                name = par.get('name', "")
                if not name:
                    raise Exception("格式不对，请确认以后再重新执行")
                value = "{}, {}, {}".format(par.get("in", ""), par.get("required", False), par.get('type', "string"))
                parameters[name] = value
        return parameters
    elif isinstance(data, dict):
        name = data.get('name', "")
        if not name:
            raise Exception("格式不对，请确认以后再重新执行")
        value = "{}, {}, {}".format(data.get("in", ""), data.get("required", False), data.get('type', "string"))
        parameters[name] = value
        return parameters
    else:
        raise Exception("数据格式不对，请确认以后再行执行")


def getSummary(text):
    if isinstance(text, str):
        if len(text) >= 10:
            return text[0:10]
        if text.__contains__(","):
            return text.split(",")[0]
        elif text.__contains__("，"):
            return text.split("，")[0]
        elif len(text) >= 10:
            return text[0:10]
        else:
            return text
    else:
        raise TypeError("参数类型不对")




if __name__ == "__main__":
    # # url = r'https://cs1.jsbooks.com.cn/mall/v2/api-docs'  # mall端的swagger
    # url = r"http://101.133.106.76:38484/business/v2/api-docs"  # business 端的swagger
    # url = r"http://106.14.149.149:8183/ops/v2/api-docs"  # ops 端的 swagger
    # file_name = "mall"
    url_dict = {
        "mall": r'https://cs1.jsbooks.com.cn/mall/v2/api-docs',
        "business": r"http://101.133.106.76:38484/business/v2/api-docs",
        "ops": r"http://106.14.149.149:8183/ops/v2/api-docs"
    }
    for module_name, url in url_dict.items():
        index = ["类型", "接口", "方法", "参数", "说明"]
        api = {}
        data = requests.get(url).json()
        paths = data.get("paths", {})
        if not isinstance(paths, dict):
            raise Exception("数据错误")
        apis = []
        for key, value in paths.items():
            api = {}
            api['接口'] = key
            if isinstance(value, dict):
                for k, v in value.items():
                    api["方法"] = k
                    api["类型"] = v.get("tags", "")
                    summary = getSummary(v.get("summary", ""))
                    #这里剔除错误的内容
                    api["说明"] = summary
                    api["参数"] = getParameter(v.get("parameters", {}))
                    temp = [api[k] for k in index]
                    apis.append(api)
        df = pd.DataFrame(apis, columns=index)
        df.to_excel("{}_api.xls".format(module_name), sheet_name="api汇总", index=False)
    # print("springfall")