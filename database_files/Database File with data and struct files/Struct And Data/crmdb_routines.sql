-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: localhost    Database: crmdb
-- ------------------------------------------------------
-- Server version	8.0.11

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
 1 AS `employeeCity`,
 1 AS `employeeState`,
 1 AS `employeeEmail`,
 1 AS `employeePhoneNumber`,
 1 AS `roleID`*/;
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
 1 AS `employeeID`,
 1 AS `employeePassword`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_returncartypecity`
--

DROP TABLE IF EXISTS `v_returncartypecity`;
/*!50001 DROP VIEW IF EXISTS `v_returncartypecity`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `v_returncartypecity` AS SELECT 
 1 AS `returnStoreCity`,
 1 AS `bodyType`,
 1 AS `returnDate`,
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
 1 AS `pickupStoreCity`,
 1 AS `bodyType`,
 1 AS `pickupDate`,
 1 AS `quantity`*/;
SET character_set_client = @saved_cs_client;

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
/*!50001 VIEW `v_employee` AS select `employee`.`employeeID` AS `employeeID`,`employee`.`employeeFirstName` AS `employeeFirstName`,`employee`.`employeeLastName` AS `employeeLastName`,`employee`.`employeeDOB` AS `employeeDOB`,`employee`.`employeeAddress` AS `employeeAddress`,`employee`.`employeeCity` AS `employeeCity`,`employee`.`employeeState` AS `employeeState`,`employee`.`employeeEmail` AS `employeeEmail`,`employee`.`employeePhoneNumber` AS `employeePhoneNumber`,`employee`.`roleID` AS `roleID` from `employee` */;
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
/*!50001 VIEW `v_salesorder` AS select `so`.`orderID` AS `orderID`,`so`.`createDate` AS `createDate`,`so`.`pickupDate` AS `pickupDate`,`so`.`pickupStoreID` AS `pickupStoreID`,`pst`.`storeName` AS `pickupStoreName`,`pst`.`storeCity` AS `pickupStoreCity`,`pst`.`storeState` AS `pickupStoreState`,`so`.`returnDate` AS `returnDate`,`so`.`returnStoreID` AS `returnStoreID`,`rst`.`storeName` AS `returnStoreName`,`rst`.`storeCity` AS `returnStoreCity`,`rst`.`storeState` AS `returnStoreState`,`ct`.`customerID` AS `customerID`,`ct`.`customerFirstName` AS `customerFirstName`,`ct`.`customerLastName` AS `customerLastName`,`ct`.`customerDOB` AS `customerDOB`,`ct`.`customerAddress` AS `customerAddress`,`ct`.`customerOccupation` AS `customerOccupation`,`ct`.`customerGender` AS `customerGender`,`vh`.`vehicleID` AS `vehicleID`,`vh`.`makeName` AS `makeName`,`vh`.`model` AS `model`,`vh`.`series` AS `series`,`vh`.`seriesYear` AS `seriesYear`,`vh`.`priceNew` AS `priceNew`,`vh`.`engineSize` AS `engineSize`,`vh`.`fuelSystem` AS `fuelSystem`,`vh`.`tankCapacity` AS `tankCapacity`,`vh`.`power` AS `power`,`vh`.`seatingCapacity` AS `seatingCapacity`,`vh`.`standardTransmission` AS `standardTransmission`,`vh`.`bodyType` AS `bodyType`,`vh`.`wheelDrive` AS `wheelDrive`,`vh`.`wheelBase` AS `wheelBase` from ((((`salesorder` `so` join `store` `pst` on((`so`.`pickupStoreID` = `pst`.`storeID`))) join `store` `rst` on((`so`.`returnStoreID` = `rst`.`storeID`))) join `customer` `ct` on((`ct`.`customerID` = `so`.`customerID`))) join `vehicle` `vh` on((`vh`.`vehicleID` = `so`.`vehicleID`))) */;
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
/*!50001 VIEW `v_employeepassword` AS select `employee`.`employeeID` AS `employeeID`,`employee`.`employeePassword` AS `employeePassword` from `employee` */;
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
/*!50001 VIEW `v_returncartypecity` AS select `so`.`returnStoreCity` AS `returnStoreCity`,`so`.`bodyType` AS `bodyType`,`so`.`returnDate` AS `returnDate`,count(`so`.`orderID`) AS `quantity` from `v_salesorder` `so` group by `so`.`returnStoreCity`,`so`.`bodyType`,month(`so`.`returnDate`) */;
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
/*!50001 VIEW `v_pickupcartypecity` AS select `so`.`pickupStoreCity` AS `pickupStoreCity`,`so`.`bodyType` AS `bodyType`,`so`.`pickupDate` AS `pickupDate`,count(`so`.`orderID`) AS `quantity` from `v_salesorder` `so` group by `so`.`pickupStoreCity`,`so`.`bodyType`,month(`so`.`pickupDate`) */;
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

-- Dump completed on 2018-09-07 10:53:44
