## 豆瓣封我ip了

避免被封的办法：

1. 高级匿名代理ip。 我试了几个网上免费的代理ip，没有鸟用，可能是因为是免费的。

2. 使用并修改cookies。 `cookies= {"Cookie": "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))}` 有网友说豆瓣上可以用这种办法，我现在ip被封了，也没法尝试

3. 设置时间差。


## 豆瓣搜索返回不了结果

google 和百度都没问题。 也许因为豆瓣动态加载，需要用selenium才能实现爬虫。

## xml and xpath

To find tag that contains certain texts
	`file = tree.xpath('//h2[text()="File " or text()="Image "]')`
	
To collect the text of the node, use 
'.../text()'

To collect the property of the node, use 
'.../@title'

每一部电影占据一个li，但是我们要的是a
titles = tree.xpath('//*[@id = "content"] / div / div[1] / ol / li / div / div[2] / div[1] / a')

根据text找node。
tree.xpath("//a[text()='后页>']")
