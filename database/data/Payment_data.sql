INSERT INTO Payment (payment_date,type_id, payment_amount, payment_status, order_id)
    VALUES (
        '2024-02-02 10:15:03',
        1,
        200,
        'paid',
        1
    );

INSERT INTO Payment (payment_date,type_id, payment_amount, payment_status, order_id)
    VALUES (
        now(),
        2,
        100,
        'paid',
        2
    );
