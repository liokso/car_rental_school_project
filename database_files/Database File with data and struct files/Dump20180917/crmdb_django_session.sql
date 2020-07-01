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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3n5brglwf9noeb3xkvdk3a4ztfm2aolw','YzY3OTc4N2NkZDg1MzM1Y2EyZjgwNzE2ZjA0YzQxNjlkNzY5NjFkYTp7fQ==','2018-10-01 05:03:20.747073'),('85mthqr5u8cakqxm65e5xw518lzgk25v','MWVmNGI2ZmNmNGIyMGNhNjA2YjQxMGI4MmRjYmUzMTk0NjIyNDZmYTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzM2MwNmRjZTE4NDk1MzI1NjkxN2YyYjM5OTIwOGZiY2Q4M2YxNjA0In0=','2018-10-01 06:41:30.616337'),('9vl8qms6cm89nnyxtpxuslabqtmd65bd','YzY3OTc4N2NkZDg1MzM1Y2EyZjgwNzE2ZjA0YzQxNjlkNzY5NjFkYTp7fQ==','2018-10-01 05:03:06.911367'),('h8w8arbbv021khv5egmce5hlkv1ukzhp','YzY3OTc4N2NkZDg1MzM1Y2EyZjgwNzE2ZjA0YzQxNjlkNzY5NjFkYTp7fQ==','2018-10-01 04:37:27.228197'),('l96ksmte128yfyek4pozekqqrprs2tkd','YzY3OTc4N2NkZDg1MzM1Y2EyZjgwNzE2ZjA0YzQxNjlkNzY5NjFkYTp7fQ==','2018-10-01 04:36:50.300362'),('m0eeojmd3d5un68yamp3wpcbq5zok5sg','YzY3OTc4N2NkZDg1MzM1Y2EyZjgwNzE2ZjA0YzQxNjlkNzY5NjFkYTp7fQ==','2018-10-01 05:46:30.064052');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-17 16:51:50
