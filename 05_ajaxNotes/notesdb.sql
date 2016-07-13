CREATE DATABASE  IF NOT EXISTS `notesdb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `notesdb`;
-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: notesdb
-- ------------------------------------------------------
-- Server version	5.5.41-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `notes`
--

DROP TABLE IF EXISTS `notes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `description` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notes`
--

LOCK TABLES `notes` WRITE;
/*!40000 ALTER TABLE `notes` DISABLE KEYS */;
INSERT INTO `notes` VALUES (4,'Python','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus rutrum id lacus sit amet dapibus. Nullam a dignissim quam. Interdum et malesuada fames ac ante ipsum primis in faucibus.','2016-07-12 17:05:01','2016-07-12 19:33:38'),(35,'PHP','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus rutrum id lacus sit amet dapibus. Nullam a dignissim quam. Interdum et malesuada fames ac ante ipsum primis in faucibus.','2016-07-12 18:16:55','2016-07-12 18:17:00'),(60,'Flask','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus rutrum id lacus sit amet dapibus. Nullam a dignissim quam. Interdum et malesuada fames ac ante ipsum primis in faucibus   d  ','2016-07-12 23:54:57','2016-07-13 00:04:50'),(61,'Well','adipiscing elit. Vivamus rutrum id lacus sit amet dapibus. Nullam a dignissim quam. Interdum et malesuada fames ac ante ipsum primis in faucibus.','2016-07-12 23:57:29','2016-07-12 23:57:46'),(64,'Damn',NULL,'2016-07-13 00:06:42','2016-07-13 00:06:42');
/*!40000 ALTER TABLE `notes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-13  0:13:43
