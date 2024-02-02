CREATE TABLE UserAccount (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    email VARCHAR(40),
    username VARCHAR(40),
    pass_word VARCHAR(40),
    phone_number BIGINT NOT NULL,
    created_date DATETIME,
    is_active BOOLEAN,
    PRIMARY KEY (user_id)
);
CREATE TABLE UserProfile (
    user_profile_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    profile_picture VARCHAR(50),
    modified_date DATETIME,
    created_date DATETIME,
    PRIMARY KEY (user_profile_id),
    FOREIGN KEY (user_id) REFERENCES UserAccount(user_id)
);

CREATE TABLE Package (
    package_id INT NOT NULL AUTO_INCREMENT,
    base_price INT NOT NULL,
    max_photos INT NOT NULL,
    package_name VARCHAR(50),
    PRIMARY KEY (package_id)
);

CREATE TABLE Cart (
    cart_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    quantity INT NOT NULL,
    package_id INT NOT NULL,
    PRIMARY KEY (cart_id),
    FOREIGN KEY (user_id) REFERENCES UserProfile(user_id)
);



-- ALTER TABLE Cart
-- ADD FOREIGN KEY (user_id) REFERENCES UserProfile(user_id),

-- ALTER TABLE Cart
-- ADD FOREIGN KEY (package_id) REFERENCES Package(package_id);

-- ALTER TABLE Cart
-- ADD COLUMN package_id INT NOT NULL;

CREATE TABLE Orders (
    order_id INT NOT NULL AUTO_INCREMENT,
    order_date DATETIME,
    cart_id INT NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id)
);

-- ALTER TABLE Orders
-- DROP COLUMN user_id;


-- ALTER TABLE Orders
-- DROP FOREIGN KEY Orders_ibfk_1;
-- ALTER TABLE Orders
-- ADD FOREIGN KEY (cart_id) REFERENCES Cart(cart_id);

CREATE TABLE PaymentType (
    type_id INT NOT NULL AUTO_INCREMENT,
    payment_type VARCHAR(30),
    PRIMARY KEY (type_id)
);


CREATE TABLE Payment (
    payment_id INT NOT NULL AUTO_INCREMENT,
    payment_date DATETIME,
    type_id VARCHAR(30),
    payment_amount INT NOT NULL,
    payment_status VARCHAR(30),
    order_id INT NOT NULL,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (type_id) REFERENCES PaymentType(type_id);
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)

);
-- ALTER TABLE Payment
-- CHANGE COLUMN payment_type type_id INT NOT NULL;
-- ALTER TABLE Payment
-- ADD FOREIGN KEY (type_id) REFERENCES PaymentType(type_id);

ALTER TABLE Payment
ADD FOREIGN KEY (order_id) REFERENCES Orders(order_id);

ALTER TABLE Payment
ADD order_id INT NOT NULL;

