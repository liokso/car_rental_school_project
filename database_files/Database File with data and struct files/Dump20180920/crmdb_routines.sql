-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: crmdb
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary view structure for view `v_cities`
--

DROP TABLE IF EXISTS `v_cities`;
/*!50001 DROP VIEW IF EXISTS `v_cities`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_cities` AS SELECT 
 1 AS `cityID`,
 1 AS `cityName`,
 1 AS `cityState`,
 1 AS `cityCountry`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_store`
--

DROP TABLE IF EXISTS `v_store`;
/*!50001 DROP VIEW IF EXISTS `v_store`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_store` AS SELECT 
 1 AS `storeID`,
 1 AS `storeName`,
 1 AS `storeAddress`,
 1 AS `storePhoneNumber`,
 1 AS `storeCityID`,
 1 AS `storeCity`,
 1 AS `storeState`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_returncartypecity`
--

DROP TABLE IF EXISTS `v_returncartypecity`;
/*!50001 DROP VIEW IF EXISTS `v_returncartypecity`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_returncartypecity` AS SELECT 
 1 AS `returnCity`,
 1 AS `make`,
 1 AS `model`,
 1 AS `so.bodyType and bodyType`,
 1 AS `pickupDate`,
 1 AS `dateMonth`,
 1 AS `dateQuarter`,
 1 AS `dateYear`,
 1 AS `quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_pickupcartypecity`
--

DROP TABLE IF EXISTS `v_pickupcartypecity`;
/*!50001 DROP VIEW IF EXISTS `v_pickupcartypecity`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_pickupcartypecity` AS SELECT 
 1 AS `pickupCity`,
 1 AS `make`,
 1 AS `model`,
 1 AS `so.bodyType and bodyType`,
 1 AS `pickupDate`,
 1 AS `dateMonth`,
 1 AS `dateQuarter`,
 1 AS `dateYear`,
 1 AS `quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_pickupdiffcarscity`
--

DROP TABLE IF EXISTS `v_pickupdiffcarscity`;
/*!50001 DROP VIEW IF EXISTS `v_pickupdiffcarscity`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_pickupdiffcarscity` AS SELECT 
 1 AS `CityID`,
 1 AS `pickupCity`,
 1 AS `dateMonthNum`,
 1 AS `dateMonth`,
 1 AS `dateQuarter`,
 1 AS `dateYear`,
 1 AS `quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_customer`
--

DROP TABLE IF EXISTS `v_customer`;
/*!50001 DROP VIEW IF EXISTS `v_customer`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_customer` AS SELECT 
 1 AS `customerID`,
 1 AS `customerFirstName`,
 1 AS `customerLastName`,
 1 AS `customerDOB`,
 1 AS `customerAddress`,
 1 AS `customerOccupation`,
 1 AS `customerGender`,
 1 AS `phoneNumber`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_carpcitypmonth`
--

DROP TABLE IF EXISTS `v_carpcitypmonth`;
/*!50001 DROP VIEW IF EXISTS `v_carpcitypmonth`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_carpcitypmonth` AS SELECT 
 1 AS `city`,
 1 AS `cityID`,
 1 AS `make`,
 1 AS `model`,
 1 AS `dateMonth`,
 1 AS `dateQuarter`,
 1 AS `dateYear`,
 1 AS `quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_employee`
--

DROP TABLE IF EXISTS `v_employee`;
/*!50001 DROP VIEW IF EXISTS `v_employee`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_employee` AS SELECT 
 1 AS `employeeID`,
 1 AS `employeeFirstName`,
 1 AS `employeeLastName`,
 1 AS `employeeDOB`,
 1 AS `employeeAddress`,
 1 AS `employeeCityID`,
 1 AS `employeeCity`,
 1 AS `employeeState`,
 1 AS `employeeEmail`,
 1 AS `employeePhoneNumber`,
 1 AS `roleID`,
 1 AS `employeeUsername`,
 1 AS `employeePassword`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_returndiffcarscity`
--

DROP TABLE IF EXISTS `v_returndiffcarscity`;
/*!50001 DROP VIEW IF EXISTS `v_returndiffcarscity`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_returndiffcarscity` AS SELECT 
 1 AS `cityID`,
 1 AS `returnCity`,
 1 AS `dateMonthNum`,
 1 AS `dateMonth`,
 1 AS `dateQuarter`,
 1 AS `dateYear`,
 1 AS `quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_salesorder`
--

DROP TABLE IF EXISTS `v_salesorder`;
/*!50001 DROP VIEW IF EXISTS `v_salesorder`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_salesorder` AS SELECT 
 1 AS `orderID`,
 1 AS `createDate`,
 1 AS `pickupDate`,
 1 AS `pickupStoreID`,
 1 AS `pickupStoreName`,
 1 AS `pickupStoreCity`,
 1 AS `pickupStoreState`,
 1 AS `returnDate`,
 1 AS `returnStoreID`,
 1 AS `returnStoreName`,
 1 AS `returnStoreCity`,
 1 AS `returnStoreState`,
 1 AS `customerID`,
 1 AS `customerFirstName`,
 1 AS `customerLastName`,
 1 AS `customerDOB`,
 1 AS `customerAddress`,
 1 AS `customerOccupation`,
 1 AS `customerGender`,
 1 AS `vehicleID`,
 1 AS `makeName`,
 1 AS `model`,
 1 AS `series`,
 1 AS `seriesYear`,
 1 AS `priceNew`,
 1 AS `engineSize`,
 1 AS `fuelSystem`,
 1 AS `tankCapacity`,
 1 AS `power`,
 1 AS `seatingCapacity`,
 1 AS `standardTransmission`,
 1 AS `bodyType`,
 1 AS `wheelDrive`,
 1 AS `wheelBase`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_employeepassword`
--

DROP TABLE IF EXISTS `v_employeepassword`;
/*!50001 DROP VIEW IF EXISTS `v_employeepassword`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_employeepassword` AS SELECT 
 1 AS `employeeUsername`,
 1 AS `employeePassword`,
 1 AS `roleAccessLevel`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_pickupcarcity`
--

DROP TABLE IF EXISTS `v_pickupcarcity`;
/*!50001 DROP VIEW IF EXISTS `v_pickupcarcity`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_pickupcarcity` AS SELECT 
 1 AS `CityID`,
 1 AS `pickupCity`,
 1 AS `carID`,
 1 AS `dateMonthNum`,
 1 AS `dateMonth`,
 1 AS `dateQuarter`,
 1 AS `dateYear`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_returncarcity`
--

DROP TABLE IF EXISTS `v_returncarcity`;
/*!50001 DROP VIEW IF EXISTS `v_returncarcity`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_returncarcity` AS SELECT 
 1 AS `returnCity`,
 1 AS `cityID`,
 1 AS `carID`,
 1 AS `dateMonthNum`,
 1 AS `dateMonth`,
 1 AS `dateQuarter`,
 1 AS `dateYear`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_cities`
--

/*!50001 DROP VIEW IF EXISTS `v_cities`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_cities` AS select `citylist`.`cityID` AS `cityID`,`citylist`.`cityName` AS `cityName`,`citylist`.`cityState` AS `cityState`,`citylist`.`cityCountry` AS `cityCountry` from `citylist` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_store`
--

/*!50001 DROP VIEW IF EXISTS `v_store`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_store` AS select `st`.`storeID` AS `storeID`,`st`.`storeName` AS `storeName`,`st`.`storeAddress` AS `storeAddress`,`st`.`storePhoneNumber` AS `storePhoneNumber`,`st`.`storeCityID` AS `storeCityID`,`cl`.`cityName` AS `storeCity`,`cl`.`cityState` AS `storeState` from (`store` `st` join `citylist` `cl` on((`cl`.`cityID` = `st`.`storeID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_returncartypecity`
--

/*!50001 DROP VIEW IF EXISTS `v_returncartypecity`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_returncartypecity` AS select `so`.`returnStoreCity` AS `returnCity`,`so`.`makeName` AS `make`,`so`.`model` AS `model`,(`so`.`bodyType` and `so`.`bodyType`) AS `so.bodyType and bodyType`,`so`.`pickupDate` AS `pickupDate`,month(`so`.`pickupDate`) AS `dateMonth`,quarter(`so`.`pickupDate`) AS `dateQuarter`,year(`so`.`pickupDate`) AS `dateYear`,count(`so`.`orderID`) AS `quantity` from `v_salesorder` `so` group by `returnCity`,`so`.`model`,`so`.`bodyType`,`dateMonth`,`dateYear` order by `returnCity` asc,`quantity` desc,`dateMonth` asc,`dateQuarter` asc,`dateYear` asc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_pickupcartypecity`
--

/*!50001 DROP VIEW IF EXISTS `v_pickupcartypecity`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_pickupcartypecity` AS select `so`.`pickupStoreCity` AS `pickupCity`,`so`.`makeName` AS `make`,`so`.`model` AS `model`,(`so`.`bodyType` and `so`.`bodyType`) AS `so.bodyType and bodyType`,`so`.`pickupDate` AS `pickupDate`,month(`so`.`pickupDate`) AS `dateMonth`,quarter(`so`.`pickupDate`) AS `dateQuarter`,year(`so`.`pickupDate`) AS `dateYear`,count(`so`.`orderID`) AS `quantity` from `v_salesorder` `so` group by `pickupCity`,`so`.`model`,`so`.`bodyType`,`dateMonth`,`dateYear` order by `pickupCity` asc,`quantity` desc,`dateMonth` asc,`dateQuarter` asc,`dateYear` asc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_pickupdiffcarscity`
--

/*!50001 DROP VIEW IF EXISTS `v_pickupdiffcarscity`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_pickupdiffcarscity` AS select `v_pickupcarcity`.`CityID` AS `CityID`,`v_pickupcarcity`.`pickupCity` AS `pickupCity`,`v_pickupcarcity`.`dateMonthNum` AS `dateMonthNum`,`v_pickupcarcity`.`dateMonth` AS `dateMonth`,`v_pickupcarcity`.`dateQuarter` AS `dateQuarter`,`v_pickupcarcity`.`dateYear` AS `dateYear`,count(`v_pickupcarcity`.`carID`) AS `quantity` from `v_pickupcarcity` group by `v_pickupcarcity`.`pickupCity`,`v_pickupcarcity`.`dateMonthNum`,`v_pickupcarcity`.`dateQuarter`,`v_pickupcarcity`.`dateYear` order by `v_pickupcarcity`.`pickupCity` asc,`v_pickupcarcity`.`dateYear` desc,`v_pickupcarcity`.`dateMonth` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_customer`
--

/*!50001 DROP VIEW IF EXISTS `v_customer`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_customer` AS select `c`.`customerID` AS `customerID`,`c`.`customerFirstName` AS `customerFirstName`,`c`.`customerLastName` AS `customerLastName`,`c`.`customerDOB` AS `customerDOB`,`c`.`customerAddress` AS `customerAddress`,`c`.`customerOccupation` AS `customerOccupation`,`c`.`customerGender` AS `customerGender`,`pn`.`phoneNumber` AS `phoneNumber` from (`customer` `c` join `customerphonenumber` `pn` on((`c`.`customerID` = `pn`.`customerID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_carpcitypmonth`
--

/*!50001 DROP VIEW IF EXISTS `v_carpcitypmonth`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_carpcitypmonth` AS select `so`.`pickupStoreCity` AS `city`,`sc`.`cityID` AS `cityID`,`so`.`makeName` AS `make`,`so`.`model` AS `model`,month(`so`.`pickupDate`) AS `dateMonth`,quarter(`so`.`pickupDate`) AS `dateQuarter`,year(`so`.`pickupDate`) AS `dateYear`,count(`so`.`orderID`) AS `quantity` from (`v_salesorder` `so` join `v_cities` `sc` on((`sc`.`cityName` = `so`.`pickupStoreCity`))) group by `city`,`so`.`model`,`dateMonth`,`dateYear`,`make` order by `city` asc,`dateYear` desc,`so`.`pickupDate` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_employee`
--

/*!50001 DROP VIEW IF EXISTS `v_employee`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_employee` AS select `em`.`employeeID` AS `employeeID`,`em`.`employeeFirstName` AS `employeeFirstName`,`em`.`employeeLastName` AS `employeeLastName`,`em`.`employeeDOB` AS `employeeDOB`,`em`.`employeeAddress` AS `employeeAddress`,`em`.`employeeCityID` AS `employeeCityID`,`cl`.`cityName` AS `employeeCity`,`cl`.`cityState` AS `employeeState`,`em`.`employeeEmail` AS `employeeEmail`,`em`.`employeePhoneNumber` AS `employeePhoneNumber`,`em`.`roleID` AS `roleID`,`em`.`employeeUsername` AS `employeeUsername`,`em`.`employeePassword` AS `employeePassword` from (`employee` `em` join `citylist` `cl` on((`cl`.`cityID` = `em`.`employeeCityID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_returndiffcarscity`
--

/*!50001 DROP VIEW IF EXISTS `v_returndiffcarscity`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_returndiffcarscity` AS select `v_returncarcity`.`cityID` AS `cityID`,`v_returncarcity`.`returnCity` AS `returnCity`,`v_returncarcity`.`dateMonthNum` AS `dateMonthNum`,`v_returncarcity`.`dateMonth` AS `dateMonth`,`v_returncarcity`.`dateQuarter` AS `dateQuarter`,`v_returncarcity`.`dateYear` AS `dateYear`,count(`v_returncarcity`.`carID`) AS `quantity` from `v_returncarcity` group by `v_returncarcity`.`returnCity`,`v_returncarcity`.`dateMonthNum`,`v_returncarcity`.`dateQuarter`,`v_returncarcity`.`dateYear` order by `v_returncarcity`.`returnCity` asc,`v_returncarcity`.`dateYear` desc,`v_returncarcity`.`dateMonth` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_salesorder`
--

/*!50001 DROP VIEW IF EXISTS `v_salesorder`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_salesorder` AS select `so`.`orderID` AS `orderID`,`so`.`createDate` AS `createDate`,`so`.`pickupDate` AS `pickupDate`,`so`.`pickupStoreID` AS `pickupStoreID`,`pst`.`storeName` AS `pickupStoreName`,`pst`.`storeCity` AS `pickupStoreCity`,`pst`.`storeState` AS `pickupStoreState`,`so`.`returnDate` AS `returnDate`,`so`.`returnStoreID` AS `returnStoreID`,`rst`.`storeName` AS `returnStoreName`,`rst`.`storeCity` AS `returnStoreCity`,`rst`.`storeState` AS `returnStoreState`,`ct`.`customerID` AS `customerID`,`ct`.`customerFirstName` AS `customerFirstName`,`ct`.`customerLastName` AS `customerLastName`,`ct`.`customerDOB` AS `customerDOB`,`ct`.`customerAddress` AS `customerAddress`,`ct`.`customerOccupation` AS `customerOccupation`,`ct`.`customerGender` AS `customerGender`,`vh`.`vehicleID` AS `vehicleID`,`vh`.`makeName` AS `makeName`,`vh`.`model` AS `model`,`vh`.`series` AS `series`,`vh`.`seriesYear` AS `seriesYear`,`vh`.`priceNew` AS `priceNew`,`vh`.`engineSize` AS `engineSize`,`vh`.`fuelSystem` AS `fuelSystem`,`vh`.`tankCapacity` AS `tankCapacity`,`vh`.`power` AS `power`,`vh`.`seatingCapacity` AS `seatingCapacity`,`vh`.`standardTransmission` AS `standardTransmission`,`vh`.`bodyType` AS `bodyType`,`vh`.`wheelDrive` AS `wheelDrive`,`vh`.`wheelBase` AS `wheelBase` from ((((`salesorder` `so` join `v_store` `pst` on((`so`.`pickupStoreID` = `pst`.`storeID`))) join `v_store` `rst` on((`so`.`returnStoreID` = `rst`.`storeID`))) join `customer` `ct` on((`ct`.`customerID` = `so`.`customerID`))) join `vehicle` `vh` on((`vh`.`vehicleID` = `so`.`vehicleID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_employeepassword`
--

/*!50001 DROP VIEW IF EXISTS `v_employeepassword`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_employeepassword` AS select `em`.`employeeUsername` AS `employeeUsername`,`em`.`employeePassword` AS `employeePassword`,`er`.`roleAccessLevel` AS `roleAccessLevel` from (`employee` `em` join `employeerole` `er` on((`er`.`roleID` = `em`.`roleID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_pickupcarcity`
--

/*!50001 DROP VIEW IF EXISTS `v_pickupcarcity`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_pickupcarcity` AS select `so`.`pickupStoreID` AS `CityID`,`so`.`pickupStoreCity` AS `pickupCity`,`so`.`vehicleID` AS `carID`,month(`so`.`pickupDate`) AS `dateMonthNum`,monthname(`so`.`pickupDate`) AS `dateMonth`,quarter(`so`.`pickupDate`) AS `dateQuarter`,year(`so`.`pickupDate`) AS `dateYear` from `v_salesorder` `so` group by `pickupCity`,`dateMonth`,`dateYear`,`carID` order by `pickupCity` asc,`carID` asc,`so`.`pickupDate` desc,`dateQuarter` desc,`dateYear` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_returncarcity`
--

/*!50001 DROP VIEW IF EXISTS `v_returncarcity`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_returncarcity` AS select `so`.`returnStoreCity` AS `returnCity`,`so`.`returnStoreID` AS `cityID`,`so`.`vehicleID` AS `carID`,month(`so`.`returnDate`) AS `dateMonthNum`,monthname(`so`.`returnDate`) AS `dateMonth`,quarter(`so`.`returnDate`) AS `dateQuarter`,year(`so`.`returnDate`) AS `dateYear` from `v_salesorder` `so` group by `returnCity`,`dateMonth`,`dateYear`,`carID` order by `returnCity` asc,`carID` asc,`so`.`returnDate` desc,`dateQuarter` desc,`dateYear` desc */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-20 21:37:01
