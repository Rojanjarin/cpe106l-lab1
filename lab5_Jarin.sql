-- create (format: Variable_name data_type and whatever)
CREATE TABLE MENU (
    Food VARCHAR(100) PRIMARY KEY,
    Price INTEGER NOT NULL
);

-- insert
INSERT INTO MENU VALUES ('BBQ', 150);
INSERT INTO MENU VALUES ('Pork Sisig', 180);
INSERT INTO MENU VALUES ('Chicken Sisig', 170);
INSERT INTO MENU VALUES ('Beef Sisig', 190);
INSERT INTO MENU VALUES ('Fish Sisig', 200);
INSERT INTO MENU VALUES ('Sinigang na Manok', 160);
INSERT INTO MENU VALUES ('Adobong Manok', 140);
INSERT INTO MENU VALUES ('Nuts', 80);
INSERT INTO MENU VALUES ('Fried Chicken', 130);
INSERT INTO MENU VALUES ('Tilapia', 120);

-- fetch
SELECT * FROM MENU WHERE Food = 'Pork Sisig' ;
SELECT * FROM MENU WHERE Food = 'Beef Sisig' ;
SELECT * FROM MENU WHERE Food = 'Chicken Sisig' ;
SELECT * FROM MENU WHERE Food = 'Fish Sisig' ;