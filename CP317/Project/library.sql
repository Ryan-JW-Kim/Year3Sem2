-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	5.7.36

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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `year` int(11) DEFAULT NULL,
  `quantity` int(11) NOT NULL,
  `reserved` int(11) NOT NULL,
  `taken_copies` int(11) NOT NULL,
  `available` int(11) NOT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=MyISAM AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'To Kill a Mockingbird','Harper Lee',1960,5,1,2,2),(2,'1984','George Orwell',1949,7,2,1,4),(3,'Pride and Prejudice','Jane Austen',1813,3,0,1,2),(4,'The Catcher in the Rye','J.D. Salinger',1951,4,0,3,1),(5,'Lord of the Flies','William Golding',1954,6,1,2,3),(6,'The Great Gatsby','F. Scott Fitzgerald',1925,8,2,1,5),(7,'Animal Farm','George Orwell',1945,5,0,2,3),(8,'Brave New World','Aldous Huxley',1932,6,0,2,4),(9,'One Hundred Years of Solitude','Gabriel Garcia Marquez',1967,4,1,0,3),(10,'The Hobbit','J.R.R. Tolkien',1937,5,1,2,2),(11,'The Lord of the Rings','J.R.R. Tolkien',1954,7,1,1,5),(12,'Crime and Punishment','Fyodor Dostoevsky',1866,3,0,2,1),(13,'The Brothers Karamazov','Fyodor Dostoevsky',1880,4,1,1,2),(14,'Anna Karenina','Leo Tolstoy',1877,6,1,2,3),(15,'War and Peace','Leo Tolstoy',1869,8,2,1,5),(16,'The Picture of Dorian Gray','Oscar Wilde',1890,3,0,1,2),(17,'The Adventures of Huckleberry Finn','Mark Twain',1884,5,0,3,2),(18,'The Adventures of Tom Sawyer','Mark Twain',1876,4,1,1,2),(19,'Moby Dick','Herman Melville',1851,3,0,1,2),(20,'Frankenstein','Mary Shelley',1818,4,1,0,3),(21,'Dracula','Bram Stoker',1897,6,0,2,4),(22,'The Canterbury Tales','Geoffrey Chaucer',1400,2,0,1,1),(23,'Heart of Darkness','Joseph Conrad',1899,3,0,1,2),(24,'The Sound and the Fury','William Faulkner',1929,5,1,2,2),(25,'Beloved','Toni Morrison',1987,7,2,1,4),(26,'The Handmaid\'s Tale','Margaret Atwood',1985,3,0,1,2),(27,'The Sun Also Rises','Ernest Hemingway',1926,4,0,3,1),(28,'Slaughterhouse-Five','Kurt Vonnegut',1969,6,1,2,3),(29,'The Color Purple','Alice Walker',1982,8,2,1,5),(30,'The Alchemist','Paulo Coelho',1988,5,0,2,3),(31,'The Name of the Rose','Umberto Eco',1980,6,0,2,4),(32,'The Hitchhiker\'s Guide to the Galaxy','Douglas Adams',1979,4,1,0,3),(33,'The Shining','Stephen King',1977,5,1,2,2),(34,'The Silence of the Lambs','Thomas Harris',1988,7,1,1,5),(35,'The Godfather','Mario Puzo',1969,3,0,2,1),(36,'The Da Vinci Code','Dan Brown',2003,4,1,1,2),(37,'Jurassic Park','Michael Crichton',1990,6,1,2,3),(38,'The Hunger Games','Suzanne Collins',2008,8,2,1,5),(39,'Harry Potter and the Sorcerer\'s Stone','J.K. Rowling',1997,5,0,3,2),(40,'The Girl with the Dragon Tattoo','Stieg Larsson',2005,4,1,1,2),(41,'Gone Girl','Gillian Flynn',2012,3,0,1,2),(42,'The Fault in Our Stars','John Green',2012,4,1,0,3),(43,'The Girl on the Train','Paula Hawkins',2015,6,0,2,4);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `type` enum('student','staff') NOT NULL,
  `books` varchar(255) DEFAULT NULL,
  `reserved` varchar(255) DEFAULT NULL,
  `overdue` varchar(255) DEFAULT NULL,
  `fines` decimal(10,2) DEFAULT NULL,
  `max_fines` decimal(10,2) DEFAULT NULL,
  `is_allowed` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `books` (`books`),
  KEY `reserved` (`reserved`),
  KEY `overdue` (`overdue`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'John','Doe','student','1,4,5','3','2,6',10.50,20.00,1),(2,'Jane','Doe','staff','2,3,8','5','7,9',20.00,50.00,1),(3,'Bob','Smith','student','6,7,12','10','11',5.00,10.00,1),(4,'Alice','Johnson','staff','9,11','12','',0.00,50.00,1),(5,'David','Lee','student','14,15','13','',0.00,10.00,1),(6,'Emily','Wong','student','16,17,18','','',0.00,10.00,1),(7,'Chris','Chen','student','19,20','','',0.00,10.00,1),(8,'Sarah','Kim','staff','10,12,13','','',0.00,50.00,1),(9,'Michael','Garcia','student','11,13','','',0.00,10.00,1),(10,'Alex','Nguyen','student','15,17,18','','',0.00,10.00,1),(11,'Jessica','Zhang','student','19,20','','',0.00,10.00,1),(12,'Ethan','Brown','staff','1,4,8','2,6','5',15.00,50.00,1),(13,'Lily','Wang','staff','3,7','4','1,10',30.00,50.00,1),(14,'Jacob','Garcia','student','1,2,3','4,5,6','7,8,9',25.00,10.00,0),(15,'Olivia','Martinez','student','10,11,12','13','',0.00,10.00,1);
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

-- Dump completed on 2023-04-06 10:02:48
