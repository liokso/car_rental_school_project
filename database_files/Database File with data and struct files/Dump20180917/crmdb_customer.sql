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
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `customer` (
  `customerID` int(11) NOT NULL,
  `customerFirstName` varchar(50) NOT NULL,
  `customerLastName` varchar(50) NOT NULL,
  `customerDOB` date DEFAULT NULL,
  `customerAddress` varchar(50) DEFAULT NULL,
  `customerOccupation` varchar(50) DEFAULT NULL,
  `customerGender` enum('M','F') DEFAULT NULL,
  PRIMARY KEY (`customerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (11010,'Jacquelyn S',' S','1968-02-16','7800 Corrinne Court','Labour','M'),(11011,'Curtis L',' L','1967-11-14','1224 Shoenic','Labour','M'),(11012,'Lauren W',' W','1972-01-28','4785 Scott Street','Labour','F'),(11013,'Ian J',' J','1972-08-16','7902 Hudson Ave.','Labour','M'),(11014,'Sydney B',' B','1972-05-19','9011 Tank Drive','Labour','M'),(11015,'Chloe Y',' Y','1983-02-10','244 Willow Pass Road','Labour','F'),(11016,'Wyatt H',' H','1983-04-18','9666 Northridge Ct.','Labour','M'),(11017,'Shannon W',' W','1948-06-16','7330 Saddlehill Lane','Labour','M'),(11018,'Clarence R',' R','1948-10-19','244 Rivewview','Labour','F'),(11019,'Luke L',' L','1982-03-10','7832 Landing Dr','Labour','M'),(11050,'Alan Z',' Z','1955-09-10','2741 Gainborough Dr.','Labour','F'),(11051,'Daniel J',' J','1955-08-14','8085 Sunnyvale Avenue','Labour','F'),(11052,'Heidi L',' L','1955-08-10','2514 Via Cordona','Labour','F'),(11053,'Ana P',' P','1984-08-10','1660 Stonyhill Circle','Labour','M'),(11054,'Deanna M',' M','1956-03-20','5825 B Way','Labour','M'),(11055,'Gilbert R',' R','1956-03-15','8811 The Trees Dr.','Labour','F'),(11056,'Michele N',' N','1957-04-13','5464 Janin Pl.','Labour','M'),(11057,'Carl A',' A','1957-10-21','6930 Lake Nadine Place','Labour','F'),(11058,'Marc D',' D','1958-04-10','6645 Sinaloa','Labour','F'),(11059,'Ashlee A',' A','1958-04-13','8255 Highland Road','Labour','F'),(11111,'Meredith G',' G','1966-02-13','7610 Northridge Ct.','Labour','M'),(11112,'Crystal W',' W','1966-09-19','2773 Kirkwood Dr','Labour','F'),(11113,'Micheal B',' B','1966-02-13','596 Marfargoa Drive','Labour','M'),(11114,'Leslie M',' M','1966-05-18','7941 Cristobal','Labour','M'),(11115,'Alvin C',' C','1966-02-21','7759 Azalea Avenue','Labour','M'),(11116,'Clinton C',' C','1966-10-10','7943 Cunha Ct.','Labour','M'),(11117,'April D',' D','1965-02-13','485 Ash Lane','Labour','F'),(11119,'Evan J',' J','1939-04-20','4157 Sierra Ridge','Retiree','F'),(11150,'Russell S',' S','1945-03-25','4755 Easley Drive','Retiree','F'),(11151,'Melinda G',' G','1946-02-15','805 Rainier Dr.','Labour','F'),(11152,'James W',' W','1980-01-20','6827 Seagull Court','Labour','F'),(11153,'Angela J',' J','1980-06-13','8877 Weatherly Drive','Labour','F'),(11154,'Megan W',' W','1980-08-13','6898 Holiday Hills','Labour','F'),(11155,'Hunter R',' R','1980-01-16','8356 Mori Court','Labour','F'),(11156,'Maria R',' R','1980-02-10','9452 Mariposa Ct.','Labour','M'),(11157,'Hannah L',' L','1979-06-23','1832 Preston Ct.','Labour','M'),(11158,'Jason W',' W','1979-10-18','6771 Bundros Court','Labour','F'),(11159,'Brianna H',' H','1979-09-20','6793 Bonifacio St.','Labour','F'),(11210,'Edward W',' W','1952-06-18','1039 Adelaide St.','Researcher','M'),(11213,'Stephanie M',' M','1953-05-24','5514 Grant Street','Researcher','M'),(11214,'Charles M',' M','1953-11-10','2719 Little Dr','Researcher','F'),(11215,'Ana P',' P','1954-06-13','3114 Arlington Way','Researcher','M'),(11216,'Jasmine T',' T','1954-05-10','8328 San Francisco','Researcher','F'),(11217,'Natalie A',' A','1954-02-23','6592 Bent Tree Lane','Researcher','F'),(11218,'Olivia B',' B','1954-09-23','3964 Stony Hill Circle','Researcher','M'),(11219,'Charles C',' C','1954-12-11','6871 Bel Air Dr.','Researcher','F'),(11250,'Shannon L',' L','1959-03-21','4185 Keywood Ct.','Manager','F'),(11251,'Xavier L',' L','1936-07-14','9245 Dantley Way','Retiree','M'),(11252,'Nicholas T',' T','1936-06-10','504 O St.','Retiree','M'),(11253,'José H',' H','1937-02-18','5703 Donald Dr.','Retiree','M'),(11254,'Johnathan V',' V','1937-03-13','9430 Versailles Pl','Retiree','M'),(11255,'Colin L',' L','1937-04-14','6083 San Jose','Retiree','F'),(11256,'Katelyn H',' H','1937-09-10','7496 Deerfield Dr.','Retiree','M'),(11257,'Jacqueline P',' P','1937-01-16','4076 Northwood Dr','Retiree','F'),(11258,'Xavier H',' H','1937-06-18','2707 Virgil Street','Retiree','F'),(11259,'Victoria S',' S','1969-03-10','3623 Barquentine Court','Manager','M'),(11310,'Erin S',' S','1957-07-19','7541 Black Point Pl','Manager','M'),(11311,'Gabrielle L',' L','1957-08-14','8619 Parkside Dr.','Manager','F'),(11312,'Sara R',' R','1957-04-13','7375 Kipling Court','Manager','M'),(11313,'Trevor J',' J','1957-02-10','4697 Yosemite Dr.','Manager','F'),(11314,'Mya F',' F','1957-12-13','8439 Rio Grande Drive','Manager','F'),(11315,'Hailey W',' W','1957-10-13','6321 Maya','Manager','F'),(11316,'Luke A',' A','1957-11-20','419 Deermeadow Way','Manager','F'),(11317,'Victoria R',' R','1956-09-20','9268 Keller Ridge','Manager','M'),(11318,'Jessica W',' W','1956-10-16','1652 Willcrest Circle','Manager','M'),(11319,'Jade B',' B','1941-04-10','8119 Northridge Ct','Retiree','F'),(11350,'Cara Z',' Z','1941-01-24','7280 Greendell Pl','Retiree','M'),(11351,'Anne R',' R','1943-04-16','7113 Eastgate Ave.','Retiree','M'),(11352,'Raymond R',' R','1944-03-10','24, impasse Ste-Madeleine','Retiree','F'),(11353,'Carrie O',' O','1945-06-23','1883 Cowell Rd.','Retiree','M'),(11354,'Deanna S',' S','1946-02-13','Dunckerstr 22525','Manager','M'),(11355,'Roberto G',' G','1946-12-18','3545 Chickpea Ct.','Manager','M'),(11356,'Terrence C',' C','1984-05-10','6613 Thornhill Place','Manager','F'),(11357,'Ramon Y',' Y','1983-03-13','3245 Vista Oak Dr.','Manager','M'),(11358,'Cynthia M',' M','1982-11-23','6757 Pamplona Ct.','Manager','F'),(11359,'Jarrod P',' P','1982-09-14','7657 H St.','Manager','M'),(11410,'Maurice G',' G','1972-08-15','15, avenue de la Gare','Manager','M'),(11411,'Devin R',' R','1958-02-21','Postenweg 2428','Manager','M'),(11412,'Sydney B',' B','1958-04-19','Postfach 99 92 92','Manager','M'),(11413,'Megan S',' S','1958-04-25','8192 Seagull Court','Manager','F'),(11414,'Ian R',' R','1958-03-28','726 W. Buchanan Rd.','Manager','M'),(11415,'Randy S',' S','1948-06-15','Ro?str 5538','Manager','M'),(11416,'Katrina B',' B','1949-03-29','8205, rue Malar','Manager','F'),(11417,'Lacey Z',' Z','1949-02-16','4, rue de Linois','Manager','F'),(11418,'Rafael H',' H','1949-02-19','Zeiter Weg 7765','Manager','M'),(11419,'Kyle S',' S','1949-02-28','9381 Alpine Rd.','Manager','M'),(11459,'Tasha D',' D','1976-10-23','9627 Kendall Rd','Nurse','M'),(11510,'Seth R',' R','1957-07-23','5989 Concord Ave','Nurse','M'),(11511,'Caleb P',' P','1957-06-24','2324 Cherry Street','Nurse','F'),(11512,'Natalie C',' C','1958-08-23','3481 Broadmoor Drive','Nurse','M'),(11513,'Alyssa H',' H','1958-09-10','5780 Conifer Terrace','Nurse','M'),(11514,'Dalton D',' D','1958-04-10','8033 Danesta Dr.','Nurse','F'),(11515,'Shannon H',' H','1958-02-15','4679 Duke Way','Nurse','F'),(11516,'Mya G',' G','1958-10-13','8826 Fine Drive','Nurse','F'),(11517,'Katherine B',' B','1958-06-10','8761 Dancing Court','Nurse','F'),(11518,'Edward W',' W','1959-05-20','2747 Carmel Dr.','Nurse','F'),(11519,'Jerome N',' N','1959-03-20','9537 Ridgewood Drive','Nurse','M'),(11535,'Alexandria H',' H','1930-07-18','11, rue de la Cavalerie','Retiree','M'),(11550,'Deb T',' T','1972-08-18','7553 Harness Circle','Nurse','M'),(11551,'Shannon A',' A','1971-05-15','268, avenue de l?Europe','Nurse','F'),(11552,'Eddie R',' R','1971-05-10','Heiderplatz 662','Nurse','M'),(11553,'Sharon L',' L','1971-09-19','6804 Coldwater Drive','Nurse','F'),(11554,'Sydney S',' S','1930-09-18','88, avenue de l? Union Centrale','Retiree','F'),(11556,'Lucas E',' E','1971-05-24','3663 A St.','Nurse','M'),(11557,'Felicia R',' R','1971-01-25','9557 Steven Circle','Nurse','M'),(11558,'Ivan M',' M','1971-08-11','5086 Nottingham Place','Nurse','M'),(11559,'Frederick S',' S','1971-12-26','Rotth?user Weg 636','Nurse','M');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
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
