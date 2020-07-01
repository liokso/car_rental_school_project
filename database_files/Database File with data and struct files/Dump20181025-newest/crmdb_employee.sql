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
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `employee` (
  `employeeID` int(11) NOT NULL AUTO_INCREMENT,
  `employeeFirstName` varchar(50) NOT NULL,
  `employeeLastName` varchar(50) NOT NULL,
  `employeeDOB` date DEFAULT NULL,
  `employeeAddress` varchar(50) DEFAULT NULL,
  `employeeCityID` int(11) DEFAULT NULL,
  `employeeEmail` varchar(100) DEFAULT NULL,
  `employeePhoneNumber` int(11) DEFAULT NULL,
  `roleID` int(11) DEFAULT NULL,
  `employeeUsername` varchar(50) DEFAULT NULL,
  `employeePassword` varchar(100) DEFAULT NULL,
  `employeeEmailVerify` varchar(40) NOT NULL,
  `employeeLoginAttempt` int(11) NOT NULL,
  PRIMARY KEY (`employeeID`),
  KEY `roleID` (`roleID`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`roleID`) REFERENCES `employeerole` (`roleid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'Nick','Elodeon','1977-12-01','12 Avatar St',3,'nick@elodeon.au',55555555,1,'nick_e','12','0',0),(2,'Bob','Afett','1995-08-08','32 Mandalore St',37,'bob@afett.mandalore',55555555,2,'bob_a','34','0',0),(3,'Sky','Walker','1990-04-15','9 Tatooine St',3,'sky@walker.tatooine',55555555,2,'sky_w','56','0',0),(4,'root1','Elodeon','1977-12-01','12 Avatar St',3,'nick@elodeon.au',55555555,1,'root1','1','0',0);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-25 22:45:41
