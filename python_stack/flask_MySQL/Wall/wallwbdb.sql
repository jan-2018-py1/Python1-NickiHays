-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: walldb
-- ------------------------------------------------------
-- Server version	5.7.21-log

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
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `comment` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,5,8,'Hi Michael','2018-02-12 00:06:42','2018-02-12 00:06:42'),(2,3,8,'Comments Comments','2018-02-12 00:12:41','2018-02-12 00:12:41'),(3,2,8,'Hi Holly','2018-02-12 00:16:49','2018-02-12 00:16:49'),(4,5,9,'Howdy! Comments are cool','2018-02-12 00:25:31','2018-02-12 00:25:31'),(5,1,9,'I like comments','2018-02-12 00:31:09','2018-02-12 00:31:09');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` text NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`user_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,2,'This is the very first message! Yay!!','2018-02-09 00:11:11','2018-02-09 00:11:11'),(2,5,'Hello World! This is my first message. How are you?','2018-02-11 23:23:27','2018-02-11 23:23:27'),(3,5,'Yay posts! Yay posts!','2018-02-11 23:47:30','2018-02-11 23:47:30'),(4,6,'Post Post Post Post Post Post Post Post Post','2018-02-11 23:54:37','2018-02-11 23:54:37'),(5,6,'Post Post Post Post Post Post Post Post Post Post Post Post Post Post Post Posting a Message','2018-02-11 23:55:39','2018-02-11 23:55:39');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(225) NOT NULL,
  `last_name` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `password` varchar(225) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Nicki','Arthur','sna@abc.com','fc5e038d38a57032085441e7fe7010b0','2018-02-08 22:57:53','2018-02-08 22:57:53'),(2,'Nicki','Hays','snh@abc.com','fc5e038d38a57032085441e7fe7010b0','2018-02-09 00:04:25','2018-02-09 00:04:25'),(3,'Nicki','Hays','snh@abc.com','fc5e038d38a57032085441e7fe7010b0','2018-02-09 00:05:06','2018-02-09 00:05:06'),(4,'James','Wold','jsh@mc.com','5f902080cdaea3e0b5488745da2c9481','2018-02-09 00:12:37','2018-02-09 00:12:37'),(5,'Holly','Jones','hbj@abc.com','d4fcfd41c186e2af0918e7e8a798842c','2018-02-11 23:22:55','2018-02-11 23:22:55'),(6,'Michael','Johnson','mjc@abc.com','2887f48a873232a855bd54cf3150f039','2018-02-11 23:54:06','2018-02-11 23:54:06'),(7,'holly','jones','abc@abc.com','23b431acfeb41e15d466d75de822307c','2018-02-11 23:59:48','2018-02-11 23:59:48'),(8,'Brian','Townsend','blt@abc.com','23ac5ddcf3ec5087a81eb18cb2235dae','2018-02-12 00:06:26','2018-02-12 00:06:26'),(9,'Jeremy','Smith','jms@abc.com','b88dd520e48c139b63908982a40f4784','2018-02-12 00:24:36','2018-02-12 00:24:36');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-12  0:33:50
