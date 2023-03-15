
import pandas as pd
import pyodbc

#соединение с сервером
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-UH7H0R6V;DATABASE=bike_stores;Trusted_Connection=yes')

query = 'SELECT * FROM '

#импорт таблиц
orders = pd.read_sql(query+' sales.orders', cnxn)
customers = pd.read_sql(query+' sales.customers', cnxn)
order_items = pd.read_sql(query+' sales.order_items', cnxn)
stores = pd.read_sql(query+' sales.stores', cnxn)
staffs = pd.read_sql(query+' sales.staffs', cnxn)
products = pd.read_sql(query+' production.products', cnxn)
categories = pd.read_sql(query+' production.categories', cnxn)
brands = pd.read_sql(query+' production.brands', cnxn)

#joins
result = orders.merge(customers, on = 'customer_id', how = 'inner', suffixes = ('.ord','.cus'))
result = result.merge(order_items, on = 'order_id', how = 'inner', suffixes = ('.ord','.ite'))
result = result.merge(stores, on = 'store_id', how = 'inner', suffixes = ('.ord','.sto'))
result = result.merge(staffs, on = 'staff_id', how = 'inner', suffixes = ('.ord','.sta'))
result = result.merge(products, on = 'product_id', how = 'inner', suffixes = ('.ite','.pro'))
result = result.merge(categories, on = 'category_id', how = 'inner', suffixes = ('.pro','.cat'))
result = result.merge(brands, on = 'brand_id', how = 'inner', suffixes = ('.pro','.bra'))

#создание столбцов с полными именами и выручкой
result['customer'] = result['first_name.ord'] + ' ' + result['last_name.ord']
result['revenue'] = result['quantity'] * result['list_price.ite']
result['sales_rep'] = result['first_name.sta'] + ' ' + result['last_name.sta']

#выбор нужных столбцов
col_list = ['order_id', 'customer', 'city.ord', 'state.ord', 'order_date', 'quantity', 'revenue', 'product_name', 'brand_name', 'category_name', 'store_name', 'sales_rep']

#создание таблицы
table = result[col_list].sort_values(by='order_id', ignore_index=True)

#пример загрузки данных
cursor = cnxn.cursor()

for index, row in table.iterrows()
    cursor.execute('INSERT INTO dbo.pandas_test values (?, ?)', int(table.loc[index, 'order_id']), int(table.loc[1, 'revenue']))
cnxn.commit()
