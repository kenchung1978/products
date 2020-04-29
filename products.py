products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)      # 字串變整數
	#p = []   #做一個小清單來放名字跟價格
	products.append([name, price])
	#p.append(name)
	#p.append(price)
	#products.append(p)
print(products)


for p in products:
	print(p[0], '的價格是', p[1])       #'abc' + '123' = 'abc123', 'abc' * 3 = 'abcabcabc'


with open('products.csv', 'w', encoding='utf-8') as f:        # with 可以自動把檔案關閉 只要離開with 的架構
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')   # \n 是分行的意思
                                            # 加法只能合併字串跟字串 或是整數跟整數，透過str再把整數變字串