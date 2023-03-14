use bike_stores;

SELECT
	ord.order_id,
	concat(cus.first_name, ' ', cus.last_name) as customer,
	cus.city,
	cus.state,
	ord.order_date,
	sum(ite.quantity) as total_units,
	sum(ite.quantity * ite.list_price) as revenue,
	pro.product_name,
	bra.brand_name,
	cat.category_name, 
	sto.store_name,
	concat(sta.first_name, ' ', sta.last_name) as sales_rep
FROM sales.orders ord
JOIN sales.customers cus ON ord.customer_id = cus.customer_id
JOIN sales.order_items ite ON ord.order_id = ite.order_id
JOIN production.products pro ON ite.product_id = pro.product_id
JOIN production.categories cat ON pro.category_id = cat.category_id
JOIN sales.stores sto ON ord.store_id = sto.store_id
JOIN sales.staffs sta ON ord.staff_id = sta.staff_id
JOIN production.brands bra ON pro.brand_id = bra.brand_id
GROUP BY 
	ord.order_id,
	concat(cus.first_name, ' ', cus.last_name), 
	cus.city, 
	cus.state,
	ord.order_date,
	pro.product_name,
	bra.brand_name,
	cat.category_name,
	sto.store_name,
	concat(sta.first_name, ' ', sta.last_name)