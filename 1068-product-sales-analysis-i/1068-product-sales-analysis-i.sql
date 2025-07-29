# Write your MySQL query statement below
Select s.product_name , p.year, p.price
from Sales p  join Product s 
on p.product_id=s.product_id