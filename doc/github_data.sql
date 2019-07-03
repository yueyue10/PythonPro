/*
Navicat MySQL Data Transfer

Source Server         : zhaoyj
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : spider_2019

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2019-07-03 16:36:05
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `github_data`
-- ----------------------------
DROP TABLE IF EXISTS `github_data`;
CREATE TABLE `github_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `news_url` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=155 DEFAULT CHARSET=utf8mb4;