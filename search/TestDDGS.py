from duckduckgo_search import DDGS


# 原文地址http://t.csdnimg.cn/an0AV

with DDGS() as ddgs:
    results = [r for r in ddgs.text("北京天气", max_results=20)]
    print(results)
