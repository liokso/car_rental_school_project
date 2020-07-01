
-- Create 'CRMdb' database
CREATE DATABASE CRMdb DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; /*Insensitive database*/

USE CRMdb;

CREATE TABLE CityList (
cityID INT NOT NULL,
cityName VARCHAR(50),
cityState VARCHAR(5),
cityCountry VARCHAR(50),
PRIMARY KEY (cityID)
);

-- Create 'Store' table
CREATE TABLE Store (
storeID INT NOT NULL,
storeName VARCHAR(50),
storeAddress VARCHAR(50),
storePhoneNumber VARCHAR(13),
storeCityID int(50),
PRIMARY KEY (storeID),
FOREIGN KEY (storeCityID) REFERENCES CityList(cityID)
);

-- Create 'Customer' table
CREATE TABLE Customer (
customerID INT NOT NULL,
customerFirstName VARCHAR(50) NOT NULL,
customerLastName VARCHAR(50) NOT NULL,
customerDOB DATE,
customerAddress VARCHAR(50),
customerOccupation VARCHAR(50),
customerGender VARCHAR(10),
PRIMARY KEY (customerID)
);

-- Create 'CustomerPhoneNumber' table
CREATE TABLE CustomerPhoneNumber (
customerID INT NOT NULL,
phoneNumber CHAR(13),
PRIMARY KEY (customerID,phoneNumber),
FOREIGN KEY (customerID) REFERENCES Customer(customerID)
);

-- Create 'EmployeeRole' table
CREATE TABLE EmployeeRole (
roleID INT NOT NULL AUTO_INCREMENT,
roleName VARCHAR(30) NOT NULL,
roleAccessLevel INT NOT NULL,
PRIMARY KEY (roleID)
);

-- Create 'Employee' table
CREATE TABLE Employee (
employeeID INT NOT NULL AUTO_INCREMENT,
employeeFirstName VARCHAR(50) NOT NULL,
employeeLastName VARCHAR(50) NOT NULL,
employeeDOB DATE,
employeeAddress VARCHAR(50),
employeeCityID INT,
employeeEmail VARCHAR(100),
employeePhoneNumber INT,
roleID INT,
employeeUsername VARCHAR(50),
employeePassword VARCHAR(100),
PRIMARY KEY (employeeID),
FOREIGN KEY (roleID) REFERENCES EmployeeRole(roleID) 
);

-- Create 'Vehicle' table
CREATE TABLE Vehicle (
vehicleID INT NOT NULL,
makeName VARCHAR(50),
model VARCHAR(50),
series VARCHAR(50),
seriesYear int,
priceNew DECIMAL(15,2),
engineSize DECIMAL(2,1),
fuelSystem  VARCHAR(50),
tankCapacity DECIMAL(4,1),
power DECIMAL(5,1),
seatingCapacity INT,
standardTransmission VARCHAR(15),
bodyType VARCHAR(50),
wheelDrive CHAR(3),
wheelBase DECIMAL(5,1),
PRIMARY KEY (vehicleID)
);

-- Create 'SalesOrder' table
CREATE TABLE SalesOrder (
orderID INT NOT NULL,
createDate DATE,
pickupDate DATE,
pickupStoreID INT,
returnDate DATE,
returnStoreID INT,
customerID INT,
vehicleID INT,
PRIMARY KEY (orderID),
FOREIGN KEY (pickupStoreID) REFERENCES Store(storeID),
FOREIGN KEY (returnStoreID) REFERENCES Store(storeID),
FOREIGN KEY (customerID) REFERENCES Customer(customerID),
FOREIGN KEY (vehicleID) REFERENCES Vehicle(vehicleID)
);

