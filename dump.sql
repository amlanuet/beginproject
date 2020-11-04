-- MySQL dump 10.13  Distrib 5.7.32, for Linux (x86_64)
--
-- Host: localhost    Database: uwebHistory
-- ------------------------------------------------------
-- Server version	5.7.32-0ubuntu0.18.04.1

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `message_id` int AUTO_INCREMENT PRIMARY KEY,
  `message` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dump completed on 2020-11-04 11:57:11
