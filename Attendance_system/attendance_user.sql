-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: localhost    Database: attendance
-- ------------------------------------------------------
-- Server version	8.0.23-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `subject` varchar(45) DEFAULT NULL,
  `mobile` varchar(45) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `class_div` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `class_teacher` varchar(45) DEFAULT NULL,
  `class_teacher_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,NULL,'admin','admin','admin',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(41,'Bhushan Mhatre','bhushan','bhushan','teacher','python','8446420699','1999-06-14','Male','bhushanganeshmhatre@gmail.com',NULL,'bhushanganeshmhatre@gmail.com',NULL,NULL),(42,'JItesh Wagh','jitesh','jitesh','teacher','Testing','123456789','2001-07-13','Male','jiteshwagh@gmail.com',NULL,'jiteshwagh@gmail.com',NULL,NULL),(43,'Amit Patil','amit','amit','teacher','Java','987654321','2003-05-19','Male','amitpatil@gmail.com',NULL,'amitpatil@gmail.com',NULL,NULL),(45,'Adesh patil','adesh','adesh','student',NULL,'244026213','2000-12-15','Male','adeshpatil@gmail.com','BCA-SY','karavi','Amit Patil',NULL),(46,'Aditya Patil','aditya','aditya','student',NULL,'515454154','2002-05-15','Male','adityapatil@gmail.com','BCA-SY','sonkhar','Amit Patil',NULL),(47,'Prajwal Mhatre','prajwal','prajwal','student',NULL,'2205205205','2002-06-26','Male','prajwalmhatre@gmail.con','Hotel','Rohe','Bhushan Mhatre',NULL),(48,'priyank shah','priyank','priyank','student',NULL,'758458199','2021-03-04','Male','priyank@gmail.com','BCA_TY','pen','JItesh Wagh',NULL),(49,'pranit patil','pranit','pranit','student',NULL,'98452105','2021-03-05','Male','pranit@gmail.com','BCA-SY','kane','JItesh Wagh',NULL),(50,'pradip patil','pradip','pradip','student',NULL,'8542154120','2021-03-11','Male','pradip@gmail.com','c+','bhal','Bhushan Mhatre',NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-29 11:52:18
