products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = []   #做一個小清單來放名字跟價格
	products.append([name, price])
	#p.append(name)
	#p.append(price)
	#products.append(p)
print(products)


