-- Create ‘v_SalesOder’ view
CREATE VIEW v_SalesOrder as
SELECT so.orderID, so.createDate, so.pickupDate, so.pickupStoreID,
pst.storeName as pickupStoreName, pst.storeCity as pickupStoreCity,
pst.storeState as pickupStoreState, so.returnDate, so.returnStoreID, 
rst.storeName as returnStoreName, rst.storeCity as returnStoreCity,
rst.storeState as returnStoreState, ct.*, vh.*
FROM SalesOrder so 
JOIN v_Store pst ON so.pickupStoreID = pst.storeID
JOIN v_Store rst ON so.returnStoreID = rst.storeID
JOIN Customer ct ON ct.customerID = so.customerID
JOIN Vehicle vh ON vh.vehicleID = so.vehicleID;

-- Create ‘v_PickupCarTypeCity’ view, this view groups different cars by store and month (pickup)
CREATE VIEW v_PickupCarCity as
SELECT so.pickupStoreID as CityID, so.pickupStoreCity as pickupCity, so.vehicleID as carID, MONTH(so.pickupDate) as dateMonthNum, MONTHNAME(so.pickupDate) as dateMonth, QUARTER(so.pickupDate) AS dateQuarter,
		YEAR(so.pickupDate) AS dateYear
FROM v_SalesOrder so
GROUP BY pickupCity, dateMonth, dateYear, carID
ORDER BY pickupCity ASC, carID ASC, so.pickupDate DESC, dateQuarter DESC, dateYear DESC;

CREATE VIEW v_PickupDiffCarsCity as
SELECT CityID, pickupCity, dateMonthNum, dateMonth, dateQuarter, dateYear, COUNT(carID) as numDiffCars FROM v_PickupCarCity
GROUP BY pickupCity, dateMonthNum, dateQuarter, dateYear
ORDER BY pickupCity ASC, dateYear DESC, dateMonth DESC;

-- Create ‘v_ReturnCarTypeCity’ view, this view groups different cars by store and month(return)
CREATE VIEW v_ReturnCarCity as
SELECT so.returnStoreCity as returnCity, so.returnStoreID as cityID, so.vehicleID as carID, MONTH(so.returnDate) as dateMonthNum, MONTHNAME(so.returnDate) as dateMonth, QUARTER(so.returnDate) AS dateQuarter,
		YEAR(so.returnDate) AS dateYear
FROM v_SalesOrder so
GROUP BY returnCity, dateMonth, dateYear, carID
ORDER BY returnCity ASC, carID ASC, so.returnDate DESC, dateQuarter DESC, dateYear DESC;

CREATE VIEW v_ReturnDiffCarsCity as
SELECT cityID, returnCity, dateMonthNum, dateMonth, dateQuarter, dateYear, COUNT(carID) as numDiffCars FROM v_ReturnCarCity 
GROUP BY returnCity, dateMonthNum, dateQuarter, dateYear
ORDER BY returnCity ASC, dateYear DESC, dateMonth DESC;

-- View to create v_CarpCitypMonth, this view return car model by time (month, quarter and year)
CREATE VIEW v_CarpCitypMonth as
SELECT so.pickupStoreCity as city, sc.cityID, so.makeName as make,so.model as model, MONTH(so.pickupDate) as dateMonth, QUARTER(so.pickupDate) AS dateQuarter,
		YEAR(so.pickupDate) AS dateYear,COUNT(so.orderID) as quantity
FROM v_SalesOrder so
JOIN v_cities sc on sc.cityName = so.pickupStoreCity
GROUP BY city, model, dateMonth, dateYear, make
ORDER BY city ASC, dateYear DESC, so.pickupDate DESC;

-- Create view with ID of makes
CREATE VIEW v_VehicleMake as
select distinct makeName, ROW_NUMBER() OVER(ORDER BY (SELECT NULL)) as rowNum from vehicle group by makeName order by rowNum;

-- Create view with ID of models
CREATE VIEW v_VehicleModel as
select distinct model, ROW_NUMBER() OVER(ORDER BY (SELECT NULL)) as rowNum from vehicle group by model order by rowNum;

