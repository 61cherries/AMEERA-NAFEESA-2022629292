-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 01, 2024 at 04:50 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `luxury_car_rental`
--

-- --------------------------------------------------------

--
-- Table structure for table `cust_info`
--

CREATE TABLE `cust_info` (
  `cust_name` varchar(30) NOT NULL,
  `cust_phone` int(10) NOT NULL,
  `car_model` varchar(10) NOT NULL,
  `rental_duration` varchar(10) NOT NULL,
  `rental_price` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cust_info`
--

INSERT INTO `cust_info` (`cust_name`, `cust_phone`, `car_model`, `rental_duration`, `rental_price`) VALUES
('hani rasyiqah', 165010441, 'Car A ', '2 days', 'RM2400'),
('iman', 126754441, 'Car A', '3', '3600'),
('adam', 162730998, 'Car C', '3', '4200'),
('kinshinko', 133195278, 'Car B', '4', '6400'),
('hanna', 1126033628, 'Car C', '3', '4200'),
('hanna', 1126033628, 'Car C', '3', '4200'),
('hanna', 1126033628, 'Car C', '3', '4200'),
('mark', 165432265, 'Car A', '4', '4800');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
