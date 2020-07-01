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
-- Table structure for table `citylist`
--

DROP TABLE IF EXISTS `citylist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `citylist` (
  `cityID` int(11) NOT NULL,
  `cityName` varchar(50) DEFAULT NULL,
  `cityState` varchar(5) DEFAULT NULL,
  `cityCountry` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cityID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citylist`
--

LOCK TABLES `citylist` WRITE;
/*!40000 ALTER TABLE `citylist` DISABLE KEYS */;
INSERT INTO `citylist` VALUES (1,'Alexandria                    ','NSW','Australia'),(2,'Bendigo                       ','VIC','Australia'),(3,'Brisbane                      ','QLD','Australia'),(4,'Caloundra                     ','QLD','Australia'),(5,'Cloverdale                    ','SA','Australia'),(6,'Coffs Harbour                 ','NSW','Australia'),(7,'Cranbourne                    ','VIC','Australia'),(8,'Darlinghurst                  ','NSW','Australia'),(9,'East Brisbane                 ','QLD','Australia'),(10,'Findon                        ','SA','Australia'),(11,'Geelong                       ','VIC','Australia'),(12,'Gold Coast                    ','QLD','Australia'),(13,'Goulburn                      ','NSW','Australia'),(14,'Hawthorne                     ','QLD','Australia'),(15,'Hervey Bay                    ','QLD','Australia'),(16,'Hobart                        ','TAS','Australia'),(17,'Lane Cove                     ','NSW','Australia'),(18,'Lavender Bay                  ','NSW','Australia'),(19,'Malabar                       ','NSW','Australia'),(20,'Matraville                    ','NSW','Australia'),(21,'Melbourne                     ','VIC','Australia'),(22,'Melton                        ','VIC','Australia'),(23,'Milsons Point                 ','NSW','Australia'),(24,'Newcastle                     ','NSW','Australia'),(25,'North Ryde                    ','NSW','Australia'),(26,'North Sydney                  ','NSW','Australia'),(27,'Perth                         ','SA','Australia'),(28,'Port Macquarie                ','NSW','Australia'),(29,'Rhodes                        ','NSW','Australia'),(30,'Rockhampton                   ','QLD','Australia'),(31,'Seaford                       ','VIC','Australia'),(32,'Silverwater                   ','NSW','Australia'),(33,'South Melbourne               ','VIC','Australia'),(34,'Springwood                    ','NSW','Australia'),(35,'St. Leonards                  ','NSW','Australia'),(36,'Sunbury                       ','VIC','Australia'),(37,'Sydney                        ','NSW','Australia'),(38,'Townsville                    ','QLD','Australia'),(39,'Warrnambool                   ','VIC','Australia'),(40,'Wollongong                    ','NSW','Australia');
/*!40000 ALTER TABLE `citylist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-25 22:45:43
