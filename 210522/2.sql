select product.category, min(product_id), product.discount from product, (select category, max(discount) as discount from product group by category) max_discount_per_category where product.category=max_discount_per_category.category and product.discount = max_discount_per_category.discount
group by product.category, product.discount
order by product.category;