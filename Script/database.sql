-- --------------------------------------------------------
-- Host:                         185.12.127.155
-- Server version:               10.2.36-MariaDB - MariaDB Server
-- Server OS:                    Linux
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for hakaton
CREATE DATABASE IF NOT EXISTS `hakaton` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `hakaton`;

-- Dumping structure for table hakaton.bookmarks
CREATE TABLE IF NOT EXISTS `bookmarks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `title` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `time` int(11) NOT NULL,
  `place_id` int(11) DEFAULT NULL,
  `link` text COLLATE utf8mb4_unicode_ci DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `id` (`id`),
  KEY `uid` (`uid`),
  CONSTRAINT `bookmarks_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table hakaton.bookmarks: ~0 rows (approximately)
/*!40000 ALTER TABLE `bookmarks` DISABLE KEYS */;
INSERT INTO `bookmarks` (`id`, `uid`, `title`, `description`, `data`, `time`, `place_id`, `link`) VALUES
	(8, 9, 'Музей Эмоций', '', '{\'id\': 32703, \'title\': \'Музей Эмоций\', \'slug\': \'muzej-muzej-emotsij\', \'address\': \'пер. Нижний Сусальный, БК «Арма», д. 5, стр. 18\', \'phone\': \'+7 995 887-77-88\', \'site_url\': \'https://kudago.com/msk/place/muzej-muzej-emotsij/\', \'subway\': \'Курская\', \'is_closed\': False, \'location\': \'msk\', \'has_parking_lot\': False, \'description\': \'\'}', 1649941047, 32703, 'https://kudago.com/msk/place/muzej-muzej-emotsij/'),
	(9, 9, 'Музей мёртвых кукол', '', '{\'id\': 33097, \'title\': \'Музей мёртвых кукол\', \'slug\': \'muzej-muzej-myortvyih-kukol\', \'address\': \'ул. Малая Молчановка, д. 8, стр. 2\', \'phone\': \'+7 995 116-66-11\', \'site_url\': \'https://kudago.com/msk/place/muzej-muzej-myortvyih-kukol/\', \'subway\': \'Арбатская, Смоленская\', \'is_closed\': False, \'location\': \'msk\', \'has_parking_lot\': False, \'description\': \'\'}', 1649941704, 33097, 'https://kudago.com/msk/place/muzej-muzej-myortvyih-kukol/'),
	(10, 9, '«Центр искусств. Москва»', '', '{\'id\': 33345, \'title\': \'«Центр искусств. Москва»\', \'slug\': \'art-tsentr-tsentr-iskusstv-moskva\', \'address\': \'ул. Волхонка, д. 15\', \'phone\': \'\', \'site_url\': \'https://kudago.com/msk/place/art-tsentr-tsentr-iskusstv-moskva/\', \'subway\': \'Библиотека имени Ленина, Кропоткинская\', \'is_closed\': False, \'location\': \'msk\', \'has_parking_lot\': False, \'description\': \'\'}', 1649942904, 33345, 'https://kudago.com/msk/place/art-tsentr-tsentr-iskusstv-moskva/');
/*!40000 ALTER TABLE `bookmarks` ENABLE KEYS */;

-- Dumping structure for table hakaton.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `chat_id` int(11) NOT NULL,
  `username` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `f_name` text COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `l_name` text COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `note` text COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `status` int(11) NOT NULL DEFAULT 1,
  `step` text COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table hakaton.users: ~0 rows (approximately)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id`, `chat_id`, `username`, `f_name`, `l_name`, `note`, `status`, `step`) VALUES
	(9, 1351881907, 'dioqp9', 'sd', '', '707', 1, ''),
	(10, 430547148, 'M1sterRobott', 'Svyat', '', '732', 1, ''),
	(11, 923715146, 'MeiloreF2', 'cutie', '', '730', 1, ''),
	(12, 927785473, 'Faleay', 'Alexey', 'Boldizhar', '', 1, '');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
