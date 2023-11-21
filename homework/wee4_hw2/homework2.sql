-- homework 1. select 5 rows from customer table

---1) Check the amount of customer each store

select store_id, count(*) from customer group by store_id;

---2) Select data of store2

select * from customer where store_id=2;

---3) Validate data

select count(*) from customer where store_id=2;

-- 280

select distinct store_id from customer where store_id=2;

--- 1

-- homework 2. insert 3 rows into customer table

insert into
    customer (
        customer_id,
        store_id,
        first_name,
        last_name,
        email,
        address_id,
        active,
        create_date,
        last_update
    )
values (
        600,
        2,
        'Sunny',
        'Tester1',
        'sunny.tester1@aws.com',
        1,
        '1',
        time(),
        time()
    ), (
        601,
        1,
        'Alice',
        'Tester2',
        'alice.tester1@aws.com',
        2,
        '1',
        time(),
        time()
    ), (
        602,
        2,
        'Kevin',
        'Tester3',
        'kevin.tester1@aws.com',
        3,
        '0',
        time(),
        time()
    );

select * from customer where customer_id >=600;

-- homework 3. move 5 customers from store_id=1 to store_id=2

--- 1) Check the amount of customer in store_id=1 before update

select count(*) from customer where store_id = 1;

-- 327

--- 2) Check 5 customers in store_id=1 before update

select * from customer where store_id = 1 limit 5;

-- customer_id: 1,2,3,5,7

--- 3) Update 5 customers from store_id=1 to store_id=2

update customer
set store_id = 2
where customer_id in (
        select customer_id
        from customer
        where store_id = 1
        limit 5
    );

--- 4) Check the amount of customer in store_id=1 after update

select count(*) from customer where store_id = 1;

-- 322

--- 5) Check 5 customers in store_id=1 after update

select * from customer where store_id = 1 limit 5;

-- customer_id: 10,12,15,17,19

-- homework 4. select customer who store manager is Mike

select store_id, count(*) from customer group by store_id;

select
    count(customer.customer_id)
from customer
    join store
    join staff on store.manager_staff_id = staff.staff_id and staff.first_name = 'Mike'
where
    customer.store_id = store.store_id;

-- 322

select *
from customer
    join store
    join staff on store.manager_staff_id = staff.staff_id and staff.first_name = 'Mike'
where
    customer.store_id = store.store_id;