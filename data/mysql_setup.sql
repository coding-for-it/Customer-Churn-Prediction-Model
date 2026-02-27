CREATE DATABASE IF NOT EXISTS churn_db;

USE churn_db;

CREATE TABLE IF NOT EXISTS customers (
    customerID VARCHAR(50),
    gender VARCHAR(10),
    SeniorCitizen INT,
    Partner VARCHAR(10),
    tenure INT,
    MonthlyCharges FLOAT,
    TotalCharges FLOAT,
    Churn VARCHAR(10)
);

-- Insert 2 sample rows
INSERT INTO customers VALUES 
('0001-A', 'Female', 0, 'Yes', 5, 80.5, 400.5, 'Yes'),
('0002-B', 'Male', 1, 'No', 24, 70.0, 1700.0, 'No');

SELECT * FROM churn_db.customers;

