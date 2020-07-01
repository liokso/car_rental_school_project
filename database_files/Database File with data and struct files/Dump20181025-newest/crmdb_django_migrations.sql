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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-09-17 03:53:01.956521'),(2,'auth','0001_initial','2018-09-17 03:53:05.300707'),(3,'admin','0001_initial','2018-09-17 03:53:05.826443'),(4,'admin','0002_logentry_remove_auto_add','2018-09-17 03:53:05.844290'),(5,'admin','0003_logentry_add_action_flag_choices','2018-09-17 03:53:05.859263'),(6,'contenttypes','0002_remove_content_type_name','2018-09-17 03:53:07.206724'),(7,'auth','0002_alter_permission_name_max_length','2018-09-17 03:53:07.485337'),(8,'auth','0003_alter_user_email_max_length','2018-09-17 03:53:07.785521'),(9,'auth','0004_alter_user_username_opts','2018-09-17 03:53:07.804516'),(10,'auth','0005_alter_user_last_login_null','2018-09-17 03:53:08.228638'),(11,'auth','0006_require_contenttypes_0002','2018-09-17 03:53:08.238651'),(12,'auth','0007_alter_validators_add_error_messages','2018-09-17 03:53:08.254569'),(13,'auth','0008_alter_user_username_max_length','2018-09-17 03:53:08.498200'),(14,'auth','0009_alter_user_last_name_max_length','2018-09-17 03:53:09.024164'),(15,'employees','0001_initial','2018-09-17 03:53:09.138857'),(16,'employees','0002_auto_20180917_1352','2018-09-17 03:53:09.187821'),(17,'sessions','0001_initial','2018-09-17 03:53:09.364329'),(18,'customers','0001_initial','2018-10-25 12:25:26.510627'),(19,'employees','0003_auto_20181007_1553','2018-10-25 12:25:27.025057'),(20,'employees','0004_auto_20181007_1814','2018-10-25 12:25:27.404700'),(21,'employees','0005_auto_20181007_1815','2018-10-25 12:25:29.474656'),(22,'employees','0006_auto_20181011_1906','2018-10-25 12:25:30.036733'),(23,'employees','0003_auto_20181008_1557','2018-10-25 12:25:30.458516'),(24,'employees','0007_merge_20181023_2033','2018-10-25 12:25:30.869375');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-25 22:45:42
