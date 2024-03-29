SELECT u.user_id, u.first_name, u.last_name, c.quantity, o.order_date, p.payment_amount
FROM UserAccount u
INNER JOIN Cart c
ON u.user_id = c.user_id
inner JOIN Orders o
ON c.cart_id = o.cart_id
inner JOIN Payment p
On o.order_id = p.order_id;