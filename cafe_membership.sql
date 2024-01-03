-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 09:10 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cafe membership`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `users_name` varchar(20) NOT NULL,
  `users_phonenumber` int(15) NOT NULL,
  `users_id` int(15) NOT NULL,
  `users_birth_day` int(2) NOT NULL,
  `users_birth_month` int(2) NOT NULL,
  `users_birth_year` int(4) NOT NULL,
  `users_age` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`users_name`, `users_phonenumber`, `users_id`, `users_birth_day`, `users_birth_month`, `users_birth_year`, `users_age`) VALUES
('dhiya', 1172685953, 12345678, 0, 0, 0, 0),
('dede', 12345678, 123456789, 2, 12, 2003, -1),
('amni', 2147483647, 9138987, 8, 11, 2004, 19),
('', 173059325, 2147483647, 4, 9, 2003, 20);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
