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
-- Table structure for table `customerphonenumber`
--

DROP TABLE IF EXISTS `customerphonenumber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `customerphonenumber` (
  `customerID` int(11) NOT NULL,
  `phoneNumber` char(13) NOT NULL,
  PRIMARY KEY (`customerID`,`phoneNumber`),
  CONSTRAINT `customerphonenumber_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `customer` (`customerid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customerphonenumber`
--

LOCK TABLES `customerphonenumber` WRITE;
/*!40000 ALTER TABLE `customerphonenumber` DISABLE KEYS */;
INSERT INTO `customerphonenumber` VALUES (11010,'111543535016'),(11011,'111543535011'),(11012,'717535016'),(11013,'817535018'),(11014,'431535015'),(11015,'208535014'),(11016,'135535017'),(11017,'111543535019'),(11018,'111543535013'),(11019,'262535011'),(11050,'111543535013'),(11051,'111543535015'),(11052,'111543535016'),(11053,'859535011'),(11054,'111543535019'),(11055,'111543535012'),(11056,'111543535017'),(11057,'111543535018'),(11058,'111543535014'),(11059,'111543535011'),(11111,'111543535017'),(11112,'111543535013'),(11113,'111543535013'),(11114,'111543535011'),(11115,'111543535019'),(11116,'111543535018'),(11117,'111543535018'),(11119,'111543535018'),(11150,'111543535019'),(11151,'111543535011'),(11152,'355535015'),(11153,'847535011'),(11154,'918535018'),(11155,'891535012'),(11156,'158535019'),(11157,'974535017'),(11158,'694535017'),(11159,'319535018'),(11210,'229535011'),(11213,'293535015'),(11214,'389535011'),(11215,'446535013'),(11216,'939535013'),(11217,'300535015'),(11218,'414535014'),(11219,'755535011'),(11250,'111543535011'),(11251,'243535011'),(11252,'377535014'),(11253,'712535013'),(11254,'494535016'),(11255,'599535013'),(11256,'249535011'),(11257,'796535011'),(11258,'559535014'),(11259,'230535013'),(11310,'233535016'),(11311,'783535017'),(11312,'296535017'),(11313,'120535012'),(11314,'522535014'),(11315,'767535015'),(11316,'786535013'),(11317,'663535019'),(11318,'702535018'),(11319,'819535016'),(11350,'111543535011'),(11351,'111543535014'),(11352,'111543535013'),(11353,'111543535011'),(11354,'111543535014'),(11355,'111543535012'),(11356,'111543535018'),(11357,'111543535014'),(11358,'111543535018'),(11359,'111543535015'),(11410,'111543535017'),(11411,'111543535017'),(11412,'111543535015'),(11413,'111543535011'),(11414,'111543535011'),(11415,'111543535014'),(11416,'111543535015'),(11417,'111543535017'),(11418,'111543535015'),(11419,'111543535017'),(11459,'111543535017'),(11510,'199535014'),(11511,'786535013'),(11512,'178535014'),(11513,'805535018'),(11514,'994535015'),(11515,'458535011'),(11516,'211535011'),(11517,'802535013'),(11518,'446535017'),(11519,'934535019'),(11535,'111543535018'),(11550,'111543535012'),(11551,'111543535015'),(11552,'111543535015'),(11553,'111543535011'),(11554,'111543535019'),(11556,'111543535015'),(11557,'111543535019'),(11558,'111543535019'),(11559,'111543535011');
/*!40000 ALTER TABLE `customerphonenumber` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-17 16:51:49
