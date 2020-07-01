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
-- Table structure for table `store`
--

DROP TABLE IF EXISTS `store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `store` (
  `storeID` int(11) NOT NULL,
  `storeName` varchar(50) DEFAULT NULL,
  `storeAddress` varchar(50) DEFAULT NULL,
  `storePhoneNumber` varchar(13) DEFAULT NULL,
  `storeCityID` int(50) DEFAULT NULL,
  PRIMARY KEY (`storeID`),
  KEY `storeCityID` (`storeCityID`),
  CONSTRAINT `store_ibfk_1` FOREIGN KEY (`storeCityID`) REFERENCES `citylist` (`cityid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store`
--

LOCK TABLES `store` WRITE;
/*!40000 ALTER TABLE `store` DISABLE KEYS */;
INSERT INTO `store` VALUES (1,'Alexandria_store','3761 N. 14th St','1115435350162',1),(2,'Coffs Harbour_store','2243 W St.','1115435350110',6),(3,'Darlinghurst_store','5844 Linden Land','1115435350184',8),(4,'Goulburn_store','1825 Village Pl.','1115435350162',13),(5,'Lane Cove_store','7553 Harness Circle','1115435350131',17),(6,'Lavender Bay_store','7305 Humphrey Drive','1115435350151',18),(7,'Malabar_store','2612 Berry Dr','1115435350184',19),(8,'Matraville_store','942 Brook Street','1115435350126',20),(9,'Milsons Point_store','624 Peabody Road','1115435350164',23),(10,'Newcastle_store','3839 Northgate Road','1115435350110',24),(11,'North Ryde_store','7800 Corrinne Court','1115435350169',25),(12,'North Sydney_store','1224 Shoenic','1115435350117',26),(13,'Port Macquarie_store','4785 Scott Street','7175350164',28),(14,'Rhodes_store','7902 Hudson Ave.','8175350185',29),(15,'Silverwater_store','9011 Tank Drive','4315350156',32),(16,'Springwood_store','244 Willow Pass Road','2085350142',34),(17,'St. Leonards_store','9666 Northridge Ct.','1355350171',35),(18,'Sydney_store','7330 Saddlehill Lane','1115435350195',37),(19,'Wollongong_store','244 Rivewview','1115435350137',40),(20,'Brisbane_store','7832 Landing Dr','2625350112',3),(21,'Caloundra_store','7156 Rose Dr.','5505350163',4),(22,'East Brisbane_store','8148 W. Lake Dr.','6225350158',9),(23,'Gold Coast_store','1769 Nicholas Drive','5895350185',12),(24,'Hawthorne_store','4499 Valley Crest','4525350188',14),(25,'Hervey Bay_store','8734 Oxford Place','7465350186',15),(26,'Rockhampton_store','2596 Franklin Canyon Road','1115435350178',30),(27,'Townsville_store','8211 Leeds Ct.','1115435350131',38),(28,'Cloverdale_store','213 Valencia Place','1115435350184',5),(29,'Findon_store','9111 Rose Ann Ave','1115435350116',10),(30,'Perth_store','6385 Mark Twain','1115435350146',27),(31,'Hobart_store','636 Vine Hill Way','1115435350182',16),(32,'Bendigo_store','6465 Detroit Ave.','1115435350195',2),(33,'Cranbourne_store','626 Bentley Street','1115435350169',7),(34,'Geelong_store','5927 Rainbow Dr','1115435350137',11),(35,'Melbourne_store','5167 Condor Place','1115435350136',21),(36,'Melton_store','1873 Mt. Whitney Dr','1115435350177',22),(37,'Seaford_store','3981 Augustine Drive','1155350183',31),(38,'South Melbourne_store','8915 Woodside Way','2295350112',33),(39,'Sunbury_store','8357 Sandy Cove Lane','1115435350114',36),(40,'Warrnambool_store','9353 Creekside Dr.','1115435350183',39);
/*!40000 ALTER TABLE `store` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-25 22:45:45
