-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2024-09-28 08:47:59
-- 伺服器版本： 10.4.32-MariaDB
-- PHP 版本： 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `refrigerator1`
--

-- --------------------------------------------------------

--
-- 資料表結構 `app_user`
--

CREATE TABLE `app_user` (
  `app_id` int(11) NOT NULL,
  `app_account` varchar(20) DEFAULT NULL,
  `app_password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `app_user`
--

INSERT INTO `app_user` (`app_id`, `app_account`, `app_password`) VALUES
(1, 'admin', 'admin');

-- --------------------------------------------------------

--
-- 資料表結構 `manufacturer`
--

CREATE TABLE `manufacturer` (
  `manufacturer_id` int(11) NOT NULL,
  `manufacturer_name` varchar(20) DEFAULT NULL,
  `manufacturer_phone` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `manufacturer`
--

INSERT INTO `manufacturer` (`manufacturer_id`, `manufacturer_name`, `manufacturer_phone`) VALUES
(0, '測試廠商', '0900000000');

-- --------------------------------------------------------

--
-- 資料表結構 `picture`
--

CREATE TABLE `picture` (
  `picture_id` int(11) NOT NULL,
  `picture_name` varchar(20) DEFAULT NULL,
  `picture_data` longblob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `picture`
--

INSERT INTO `picture` (`picture_id`, `picture_name`, `picture_data`) VALUES
(1, 'test', 0x616161);

-- --------------------------------------------------------

--
-- 資料表結構 `stock`
--

CREATE TABLE `stock` (
  `stock_id` int(11) NOT NULL,
  `stock_name` varchar(20) DEFAULT NULL,
  `stock_indate` date DEFAULT NULL,
  `stock_expiration` date DEFAULT NULL,
  `stock_num` int(11) DEFAULT NULL,
  `stock_lownum` int(11) DEFAULT NULL,
  `manufacturer_id` int(11) DEFAULT NULL,
  `picture_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `stock`
--

INSERT INTO `stock` (`stock_id`, `stock_name`, `stock_indate`, `stock_expiration`, `stock_num`, `stock_lownum`, `manufacturer_id`, `picture_id`) VALUES
(0, '測試品項', '2024-04-04', '2024-07-04', 6, 2, 0, 1);

-- --------------------------------------------------------

--
-- 資料表結構 `temperature`
--

CREATE TABLE `temperature` (
  `temperature_id` int(11) NOT NULL,
  `temperature_num` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `temperature`
--

INSERT INTO `temperature` (`temperature_id`, `temperature_num`) VALUES
(1, -22.00);

-- --------------------------------------------------------

--
-- 資料表結構 `web_user`
--

CREATE TABLE `web_user` (
  `web_id` int(11) NOT NULL,
  `web_account` varchar(255) DEFAULT NULL,
  `web_password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- 傾印資料表的資料 `web_user`
--

INSERT INTO `web_user` (`web_id`, `web_account`, `web_password`) VALUES
(1, 'admin', 'admin');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `app_user`
--
ALTER TABLE `app_user`
  ADD PRIMARY KEY (`app_id`);

--
-- 資料表索引 `manufacturer`
--
ALTER TABLE `manufacturer`
  ADD PRIMARY KEY (`manufacturer_id`);

--
-- 資料表索引 `picture`
--
ALTER TABLE `picture`
  ADD PRIMARY KEY (`picture_id`);

--
-- 資料表索引 `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`stock_id`),
  ADD KEY `manufacturer_id` (`manufacturer_id`),
  ADD KEY `picture_id` (`picture_id`);

--
-- 資料表索引 `temperature`
--
ALTER TABLE `temperature`
  ADD PRIMARY KEY (`temperature_id`);

--
-- 資料表索引 `web_user`
--
ALTER TABLE `web_user`
  ADD PRIMARY KEY (`web_id`);

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `stock`
--
ALTER TABLE `stock`
  ADD CONSTRAINT `stock_ibfk_1` FOREIGN KEY (`manufacturer_id`) REFERENCES `manufacturer` (`manufacturer_id`) ON DELETE SET NULL,
  ADD CONSTRAINT `stock_ibfk_2` FOREIGN KEY (`picture_id`) REFERENCES `picture` (`picture_id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
