-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: project_j
-- ------------------------------------------------------
-- Server version	8.0.13

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
-- Table structure for table `health_001`
--

DROP TABLE IF EXISTS `health_001`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `health_001` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `county` varchar(25) NOT NULL,
  `restaurants` decimal(10,0) NOT NULL,
  `population` decimal(10,0) NOT NULL,
  `percentage` decimal(19,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `health_001`
--

LOCK TABLES `health_001` WRITE;
/*!40000 ALTER TABLE `health_001` DISABLE KEYS */;
INSERT INTO `health_001` VALUES (1,'Cleburne',16,25603,42.10),(2,'Prentiss',16,1014,41.30),(3,'Jasper',4,16529,40.80),(4,'Holmes',4,18509,39.70),(5,'Coal',1,5709,39.50),(6,'Ashley',15,20958,39.20),(7,'St Francis',10,239,38.90),(8,'Lawrence',6,16970,38.80),(9,'Lafayette',3,7163,38.80),(10,'Mississippi',32,44232,38.80),(11,'Haskell',4,1976,38.70),(12,'Randolph',8,17561,38.60),(13,'Poinsett',17,24144,38.50),(14,'Lawrence',6,12601,38.40),(15,'Sevier',97,94570,38.30),(16,'Claiborne',5,9164,38.20),(17,'Cocke',16,35201,38.10),(18,'Bell',24,27841,38.00),(19,'Yazoo',10,27811,38.00),(20,'Quitman',4,2235,38.00);
/*!40000 ALTER TABLE `health_001` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-06 18:44:15
