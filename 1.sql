/*
Navicat MySQL Data Transfer
Source Server         : mysql
Source Server Version : 50532
Source Host           : localhost:3306
Source Database       : student
Target Server Type    : MYSQL
Target Server Version : 50532
File Encoding         : 65001
Date: 2019-11-28 15:09:36
*/
 
SET FOREIGN_KEY_CHECKS=0;
 
-- ----------------------------
-- Table structure for `admin_login_k`
-- ----------------------------
DROP TABLE IF EXISTS `admin_login_k`;
CREATE TABLE `admin_login_k` (
  `admin_id` char(20) NOT NULL,
  `admin_pass` char(20) DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
-- ----------------------------
-- Records of admin_login_k
-- ----------------------------
INSERT INTO `admin_login_k` VALUES ('admin', 'admin');
 
-- ----------------------------
-- Table structure for `student_k`
-- ----------------------------
DROP TABLE IF EXISTS `student_k`;
CREATE TABLE `student_k` (
  `id` char(20) NOT NULL,
  `name` char(20) DEFAULT NULL,
  `gender` char(5) DEFAULT NULL,
  `age` char(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
-- ----------------------------
-- Records of student_k
-- ----------------------------
INSERT INTO `student_k` VALUES ('182085211003', 'a', '女', '22');
INSERT INTO `student_k` VALUES ('182085211004', 'b', '女', '18');
INSERT INTO `student_k` VALUES ('182085211005', 'abc', '男', '23');
INSERT INTO `student_k` VALUES ('182085211006', 'abc', '女', '24');
INSERT INTO `student_k` VALUES ('182085211008', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('182085211009', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('182085211010', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('182085211011', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('1820852110111', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('182085211012', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('182085211013', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('182085211014', 'Tom2', '男', '23');
INSERT INTO `student_k` VALUES ('182085211015', 'Tom1', '男', '23');
INSERT INTO `student_k` VALUES ('182085211016', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('182085211017', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('182085211018', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('182085211019', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('182085211020', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('182085211021', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('1820852110211', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('182085211022', 'Tom1', '男', '23');
INSERT INTO `student_k` VALUES ('182085211023', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('182085211024', 'Tom', '男', '23');
INSERT INTO `student_k` VALUES ('182085211034', 'Tom', '男', '23');
 
-- ----------------------------
-- Table structure for `stu_login_k`
-- ----------------------------
DROP TABLE IF EXISTS `stu_login_k`;
CREATE TABLE `stu_login_k` (
  `stu_id` char(20) NOT NULL,
  `stu_pass` char(20) DEFAULT NULL,
  PRIMARY KEY (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
-- ----------------------------
-- Records of stu_login_k
-- ----------------------------
INSERT INTO `stu_login_k` VALUES ('182085211000', '123456');
 
-- ----------------------------
-- Table structure for `t_course`
-- ----------------------------
DROP TABLE IF EXISTS `t_course`;
CREATE TABLE `t_course` (
  `SNO` char(255) NOT NULL,
  `COURSE` char(255) DEFAULT NULL,
  `CREDIT` char(255) DEFAULT NULL,
  `GRADE` char(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
-- ----------------------------
-- Records of t_course
-- ----------------------------
INSERT INTO `t_course` VALUES ('08300205', '程序设计', '4', '88');
INSERT INTO `t_course` VALUES ('08300205', '数据库', '2.5', '90');
INSERT INTO `t_course` VALUES ('08300205', '力学', '5', '92');
INSERT INTO `t_course` VALUES ('08080929', '数据库', '2.5', '85');
INSERT INTO `t_course` VALUES ('09350124', '数据库', '2.5', '92');
INSERT INTO `t_course` VALUES ('09620233', '数据库', '2.5', '80');
INSERT INTO `t_course` VALUES ('09300218', '数据库', '2.5', '78');
INSERT INTO `t_course` VALUES ('09010122', '数据库', '2.5', '87');
INSERT INTO `t_course` VALUES ('08080929', '程序设计', '4', '86');
INSERT INTO `t_course` VALUES ('09010122', '程序设计', '4', '80');
INSERT INTO `t_course` VALUES ('08300516', '程序设计', '4', '76');
 
-- ----------------------------
-- Table structure for `t_st`
-- ----------------------------
DROP TABLE IF EXISTS `t_st`;
CREATE TABLE `t_st` (
  `SNO` char(11) NOT NULL,
  `SNAME` char(255) DEFAULT NULL,
  `SSEX` char(255) DEFAULT NULL,
  `AGE` char(255) DEFAULT NULL,
  `DEPT` char(255) DEFAULT NULL,
  PRIMARY KEY (`SNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
-- ----------------------------
-- Records of t_st
-- ----------------------------
INSERT INTO `t_st` VALUES ('08080929', '刘超世', '男', '19', '计算机应用技术');
INSERT INTO `t_st` VALUES ('08300205', '李媛媛', '女', '19', '软件工程');
INSERT INTO `t_st` VALUES ('09300218', '王海超', '男', '19', '软件工程');
INSERT INTO `t_st` VALUES ('09350124', '王彤', '女', '19', '通信原理');
INSERT INTO `t_st` VALUES ('09620233', '陈晓丽', '女', '21', '通信工程');