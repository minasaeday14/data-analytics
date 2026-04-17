/*
a) The actor table includes information about each actor, including actor_id, first_name, last_name, and last_update.
b) The film table includes information about each film, including film_id, title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, and last_update.
c) The film_actor table contains both actor_id and film_id.
d) The rental table includes information about each rental transaction, such as rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, and last_update. This information is a little hard to read by itself because it mostly uses ID numbers instead of descriptive names.
e) The inventory table includes information about copies of films in stock, including inventory_id, film_id, store_id, and last_update.
f) To understand the names of all films that were rented on a specific date, I would need to use the rental, inventory, and film tables. The rental table shows when a rental happened and which inventory item was rented, the inventory table connects each inventory item to a film_id, and the film table provides the film title. These tables are related through inventory_id and film_id.
*/

SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;
