CREATE DATABASE  IF NOT EXISTS `walldb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `walldb`;
-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: walldb
-- ------------------------------------------------------
-- Server version	5.6.35

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
  `comment` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `message_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,'Happy birthday sweetheart!','2018-07-11 17:31:09','2018-07-11 17:31:09',14,2),(2,'Yes indeed !!!','2018-07-11 17:34:12','2018-07-11 17:34:12',20,2),(3,'fhgjjh','2018-07-11 17:35:35','2018-07-11 17:35:35',20,2),(4,'You are right!','2018-07-11 17:51:23','2018-07-11 17:51:23',7,2),(5,'Yes, that\'s right','2018-07-11 18:00:31','2018-07-11 18:00:31',15,2),(6,'So what???','2018-07-11 18:01:34','2018-07-11 18:01:34',16,2),(7,'Hello Judith!','2018-07-11 18:07:58','2018-07-11 18:07:58',18,3),(8,'Stay positive!!!','2018-07-11 18:09:28','2018-07-11 18:09:28',16,3),(9,'I confirm it also...it\'s true!','2018-07-11 18:10:13','2018-07-11 18:10:13',15,3),(10,'Sure, that\'s correct!','2018-07-11 18:11:18','2018-07-11 18:11:18',7,3),(11,'Thank you Judith!','2018-07-11 18:12:01','2018-07-11 18:12:01',1,3),(12,'what the heck!','2018-07-11 18:13:23','2018-07-11 18:13:23',20,1),(13,'Thank you Viny, I like yours too!','2018-07-11 18:13:49','2018-07-11 18:13:49',19,1),(14,'Hi Terra, how are u today?','2018-07-11 18:14:36','2018-07-11 18:14:36',18,1),(15,'Starting my day with a positive attitude today','2018-07-11 18:15:46','2018-07-11 18:15:46',6,1),(16,'What the hell is this?','2018-07-11 21:20:09','2018-07-11 21:20:09',17,1);
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
  `message` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users1_idx` (`user_id`),
  CONSTRAINT `fk_messages_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'Have a nice day everyone!','2018-07-11 13:04:09','2018-07-11 13:04:09',1),(3,'Do something Good for your Life, work hard and succeed!','2018-07-11 13:10:06','2018-07-11 13:10:06',1),(4,'Do something Good for your Life, work hard and succeed!','2018-07-11 13:13:53','2018-07-11 13:13:53',1),(5,'Do something Good for your Life, work hard and succeed!','2018-07-11 13:16:41','2018-07-11 13:16:41',1),(6,'Do something Good for your Life, work hard and succeed!','2018-07-11 13:20:18','2018-07-11 13:20:18',1),(7,'Do something Good for your Life, work hard and succeed!','2018-07-11 13:24:22','2018-07-11 13:24:22',1),(9,'My new message','2018-07-11 14:35:47','2018-07-11 14:35:47',1),(10,'kjehfgkaleJGlt\'hk;l','2018-07-11 14:39:07','2018-07-11 14:39:07',1),(11,'Enjoy your day!!!','2018-07-11 14:53:58','2018-07-11 14:53:58',1),(12,'fjvkhfdkkjl;gklk;','2018-07-11 14:56:26','2018-07-11 14:56:26',1),(13,'cvmnbsmvbm,n','2018-07-11 14:58:15','2018-07-11 14:58:15',1),(14,'HAPPY BIRTHDAY TO MYSELF!!!','2018-07-11 14:59:15','2018-07-11 14:59:15',1),(15,'Today is Wednesday? ','2018-07-11 15:03:36','2018-07-11 15:03:36',1),(16,'yes yes yes yes!!!!','2018-07-11 15:07:00','2018-07-11 15:07:00',1),(17,'kdlkglbdgkb;\'l;\'','2018-07-11 15:07:49','2018-07-11 15:07:49',1),(18,'Hi, my name is Viny, this is my first post.','2018-07-11 15:12:21','2018-07-11 15:12:21',2),(19,'How are you Judith? I like your posts...','2018-07-11 15:13:36','2018-07-11 15:13:36',2),(20,'cbnvnvmnbnb','2018-07-11 15:23:26','2018-07-11 15:23:26',2);
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
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Judith','Love','jsmith@gmail.com','$2b$12$9bfrhCuIKYKqbLVaQykX5e57ys9vetZtN/T3f9.supjFUu9rrh9dy','2018-07-11 13:00:57','2018-07-11 13:00:57'),(2,'Viny','Manya','vinymanya@gmail.com','$2b$12$FBmS/Mwq29bwjZhelksEw.W5j9ZjIPh5220F5..I1KR3sVUvDpgNm','2018-07-11 15:11:35','2018-07-11 15:11:35'),(3,'Terra','Nova','test@test.com','$2b$12$nk/30lVPTVaNdgzCObsdPeAKPJHNe8HDfpTSk8WgiTzA8jNAaCOMe','2018-07-11 18:02:38','2018-07-11 18:02:38');
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

-- Dump completed on 2018-07-13 22:47:22
