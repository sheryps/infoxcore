-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2022 at 05:57 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `coreappbasebackend2`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add acnt_monthdays', 7, 'add_acnt_monthdays'),
(26, 'Can change acnt_monthdays', 7, 'change_acnt_monthdays'),
(27, 'Can delete acnt_monthdays', 7, 'delete_acnt_monthdays'),
(28, 'Can view acnt_monthdays', 7, 'view_acnt_monthdays'),
(29, 'Can add acntexpensest', 8, 'add_acntexpensest'),
(30, 'Can change acntexpensest', 8, 'change_acntexpensest'),
(31, 'Can delete acntexpensest', 8, 'delete_acntexpensest'),
(32, 'Can view acntexpensest', 8, 'view_acntexpensest'),
(33, 'Can add branch_registration', 9, 'add_branch_registration'),
(34, 'Can change branch_registration', 9, 'change_branch_registration'),
(35, 'Can delete branch_registration', 9, 'delete_branch_registration'),
(36, 'Can view branch_registration', 9, 'view_branch_registration'),
(37, 'Can add conditions', 10, 'add_conditions'),
(38, 'Can change conditions', 10, 'change_conditions'),
(39, 'Can delete conditions', 10, 'delete_conditions'),
(40, 'Can view conditions', 10, 'view_conditions'),
(41, 'Can add course', 11, 'add_course'),
(42, 'Can change course', 11, 'change_course'),
(43, 'Can delete course', 11, 'delete_course'),
(44, 'Can view course', 11, 'view_course'),
(45, 'Can add create_team', 12, 'add_create_team'),
(46, 'Can change create_team', 12, 'change_create_team'),
(47, 'Can delete create_team', 12, 'delete_create_team'),
(48, 'Can view create_team', 12, 'view_create_team'),
(49, 'Can add department', 13, 'add_department'),
(50, 'Can change department', 13, 'change_department'),
(51, 'Can delete department', 13, 'delete_department'),
(52, 'Can view department', 13, 'view_department'),
(53, 'Can add designation', 14, 'add_designation'),
(54, 'Can change designation', 14, 'change_designation'),
(55, 'Can delete designation', 14, 'delete_designation'),
(56, 'Can view designation', 14, 'view_designation'),
(57, 'Can add internship', 15, 'add_internship'),
(58, 'Can change internship', 15, 'change_internship'),
(59, 'Can delete internship', 15, 'delete_internship'),
(60, 'Can view internship', 15, 'view_internship'),
(61, 'Can add internship_type', 16, 'add_internship_type'),
(62, 'Can change internship_type', 16, 'change_internship_type'),
(63, 'Can delete internship_type', 16, 'delete_internship_type'),
(64, 'Can view internship_type', 16, 'view_internship_type'),
(65, 'Can add project', 17, 'add_project'),
(66, 'Can change project', 17, 'change_project'),
(67, 'Can delete project', 17, 'delete_project'),
(68, 'Can view project', 17, 'view_project'),
(69, 'Can add project_taskassign', 18, 'add_project_taskassign'),
(70, 'Can change project_taskassign', 18, 'change_project_taskassign'),
(71, 'Can delete project_taskassign', 18, 'delete_project_taskassign'),
(72, 'Can view project_taskassign', 18, 'view_project_taskassign'),
(73, 'Can add user_registration', 19, 'add_user_registration'),
(74, 'Can change user_registration', 19, 'change_user_registration'),
(75, 'Can delete user_registration', 19, 'delete_user_registration'),
(76, 'Can view user_registration', 19, 'view_user_registration'),
(77, 'Can add trainer_task', 20, 'add_trainer_task'),
(78, 'Can change trainer_task', 20, 'change_trainer_task'),
(79, 'Can delete trainer_task', 20, 'delete_trainer_task'),
(80, 'Can view trainer_task', 20, 'view_trainer_task'),
(81, 'Can add topic', 21, 'add_topic'),
(82, 'Can change topic', 21, 'change_topic'),
(83, 'Can delete topic', 21, 'delete_topic'),
(84, 'Can view topic', 21, 'view_topic'),
(85, 'Can add tester_status', 22, 'add_tester_status'),
(86, 'Can change tester_status', 22, 'change_tester_status'),
(87, 'Can delete tester_status', 22, 'delete_tester_status'),
(88, 'Can view tester_status', 22, 'view_tester_status'),
(89, 'Can add test_status', 23, 'add_test_status'),
(90, 'Can change test_status', 23, 'change_test_status'),
(91, 'Can delete test_status', 23, 'delete_test_status'),
(92, 'Can view test_status', 23, 'view_test_status'),
(93, 'Can add tasks', 24, 'add_tasks'),
(94, 'Can change tasks', 24, 'change_tasks'),
(95, 'Can delete tasks', 24, 'delete_tasks'),
(96, 'Can view tasks', 24, 'view_tasks'),
(97, 'Can add reported_issue', 25, 'add_reported_issue'),
(98, 'Can change reported_issue', 25, 'change_reported_issue'),
(99, 'Can delete reported_issue', 25, 'delete_reported_issue'),
(100, 'Can view reported_issue', 25, 'view_reported_issue'),
(101, 'Can add qualification', 26, 'add_qualification'),
(102, 'Can change qualification', 26, 'change_qualification'),
(103, 'Can delete qualification', 26, 'delete_qualification'),
(104, 'Can view qualification', 26, 'view_qualification'),
(105, 'Can add promissory', 27, 'add_promissory'),
(106, 'Can change promissory', 27, 'change_promissory'),
(107, 'Can delete promissory', 27, 'delete_promissory'),
(108, 'Can view promissory', 27, 'view_promissory'),
(109, 'Can add previous team', 28, 'add_previousteam'),
(110, 'Can change previous team', 28, 'change_previousteam'),
(111, 'Can delete previous team', 28, 'delete_previousteam'),
(112, 'Can view previous team', 28, 'view_previousteam'),
(113, 'Can add paymentlist', 29, 'add_paymentlist'),
(114, 'Can change paymentlist', 29, 'change_paymentlist'),
(115, 'Can delete paymentlist', 29, 'delete_paymentlist'),
(116, 'Can view paymentlist', 29, 'view_paymentlist'),
(117, 'Can add leave', 30, 'add_leave'),
(118, 'Can change leave', 30, 'change_leave'),
(119, 'Can delete leave', 30, 'delete_leave'),
(120, 'Can view leave', 30, 'view_leave'),
(121, 'Can add internship_paydata', 31, 'add_internship_paydata'),
(122, 'Can change internship_paydata', 31, 'change_internship_paydata'),
(123, 'Can delete internship_paydata', 31, 'delete_internship_paydata'),
(124, 'Can view internship_paydata', 31, 'view_internship_paydata'),
(125, 'Can add extracurricular', 32, 'add_extracurricular'),
(126, 'Can change extracurricular', 32, 'change_extracurricular'),
(127, 'Can delete extracurricular', 32, 'delete_extracurricular'),
(128, 'Can view extracurricular', 32, 'view_extracurricular'),
(129, 'Can add attendance', 33, 'add_attendance'),
(130, 'Can change attendance', 33, 'change_attendance'),
(131, 'Can delete attendance', 33, 'delete_attendance'),
(132, 'Can view attendance', 33, 'view_attendance'),
(133, 'Can add acntspayslip', 34, 'add_acntspayslip'),
(134, 'Can change acntspayslip', 34, 'change_acntspayslip'),
(135, 'Can delete acntspayslip', 34, 'delete_acntspayslip'),
(136, 'Can view acntspayslip', 34, 'view_acntspayslip'),
(137, 'Can add probation', 35, 'add_probation'),
(138, 'Can change probation', 35, 'change_probation'),
(139, 'Can delete probation', 35, 'delete_probation'),
(140, 'Can view probation', 35, 'view_probation'),
(141, 'Can add project_modules', 36, 'add_project_modules'),
(142, 'Can change project_modules', 36, 'change_project_modules'),
(143, 'Can delete project_modules', 36, 'delete_project_modules'),
(144, 'Can view project_modules', 36, 'view_project_modules'),
(145, 'Can add project_table', 37, 'add_project_table'),
(146, 'Can change project_table', 37, 'change_project_table'),
(147, 'Can delete project_table', 37, 'delete_project_table'),
(148, 'Can view project_table', 37, 'view_project_table'),
(149, 'Can add project_module_assign', 38, 'add_project_module_assign'),
(150, 'Can change project_module_assign', 38, 'change_project_module_assign'),
(151, 'Can delete project_module_assign', 38, 'delete_project_module_assign'),
(152, 'Can view project_module_assign', 38, 'view_project_module_assign'),
(153, 'Can add event', 39, 'add_event'),
(154, 'Can change event', 39, 'change_event'),
(155, 'Can delete event', 39, 'delete_event'),
(156, 'Can view event', 39, 'view_event'),
(157, 'Can add example', 40, 'add_example'),
(158, 'Can change example', 40, 'change_example'),
(159, 'Can delete example', 40, 'delete_example'),
(160, 'Can view example', 40, 'view_example');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$duzhjXBh0Rnlv8dZbd12C0$6tnD6ggL62zOvKnHA0f/Bn/ky9sJsrts/dEwLy4pe6M=', NULL, 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2022-03-18 12:39:19.763504');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_app_acntexpensest`
--

CREATE TABLE `base_app_acntexpensest` (
  `id` bigint(20) NOT NULL,
  `payee` varchar(100) NOT NULL,
  `payacnt` varchar(200) NOT NULL,
  `paymethod` varchar(100) NOT NULL,
  `paydate` varchar(100) NOT NULL,
  `refno` varchar(100) NOT NULL,
  `amount` int(11) NOT NULL,
  `tax` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `category` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_acntexpensest`
--

INSERT INTO `base_app_acntexpensest` (`id`, `payee`, `payacnt`, `paymethod`, `paydate`, `refno`, `amount`, `tax`, `total`, `category`, `description`) VALUES
(1, 'test', '00000000000', 'testing', '2022-03-16', '000000', 15000, 500, 15500, 'testing', 'testing  '),
(2, 'testing', '000', 'test', '2022-03-21', '00', 2000, 10, 2010, 'test', 'test '),
(3, 'test', '00', 'test', '2022-03-15', '00', 3000, 10, 3010, 'testing', 'test  ');

-- --------------------------------------------------------

--
-- Table structure for table `base_app_acntspayslip`
--

CREATE TABLE `base_app_acntspayslip` (
  `id` bigint(20) NOT NULL,
  `basic_salary` int(11) NOT NULL,
  `eno` varchar(100) NOT NULL,
  `hra` int(11) NOT NULL,
  `conveyns` varchar(100) NOT NULL,
  `tax` int(11) NOT NULL,
  `incentives` int(11) NOT NULL,
  `fromdate` date DEFAULT NULL,
  `todate` date DEFAULT NULL,
  `taxengine` varchar(100) NOT NULL,
  `incometax` int(11) NOT NULL,
  `uan` varchar(100) NOT NULL,
  `pf` int(11) NOT NULL,
  `esi` varchar(100) NOT NULL,
  `pro` varchar(100) NOT NULL,
  `leavesno` int(11) NOT NULL,
  `pf_tax` int(11) NOT NULL,
  `delay` int(11) NOT NULL,
  `basictype` varchar(255) NOT NULL,
  `hratype` varchar(255) NOT NULL,
  `contype` varchar(255) NOT NULL,
  `protype` varchar(255) NOT NULL,
  `instype` varchar(255) NOT NULL,
  `deltype` varchar(255) NOT NULL,
  `leatype` varchar(255) NOT NULL,
  `pftype` varchar(255) NOT NULL,
  `esitype` varchar(255) NOT NULL,
  `department_id` bigint(20) DEFAULT NULL,
  `designation_id` bigint(20) DEFAULT NULL,
  `user_id_id` bigint(20) DEFAULT NULL,
  `pending_status` varchar(25) NOT NULL,
  `net_salary` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_acntspayslip`
--

INSERT INTO `base_app_acntspayslip` (`id`, `basic_salary`, `eno`, `hra`, `conveyns`, `tax`, `incentives`, `fromdate`, `todate`, `taxengine`, `incometax`, `uan`, `pf`, `esi`, `pro`, `leavesno`, `pf_tax`, `delay`, `basictype`, `hratype`, `contype`, `protype`, `instype`, `deltype`, `leatype`, `pftype`, `esitype`, `department_id`, `designation_id`, `user_id_id`, `pending_status`, `net_salary`) VALUES
(2, 20000, '', 0, '0', 0, 0, '2022-05-11', NULL, '', 0, '', 0, '0', '', 0, 0, 6, 'Earning for Employee', 'Deduction for Employee', 'Deduction for Employee', 'Deduction for Employee', 'Deduction for Employee', 'Deduction for Employee', '', 'Deduction for Employee', 'Deduction for Employee', 2, 4, 10, '0', 0),
(3, 20000, '', 0, '0', 0, 0, '2022-06-11', NULL, '', 0, '', 0, '0', '', 0, 0, 20, 'Earning for Employee', 'Deduction for Employee', 'Deduction for Employee', 'Deduction for Employee', 'Deduction for Employee', 'Deduction for Employee', '', 'Deduction for Employee', 'Deduction for Employee', 2, 6, 9, '0', 0);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_acnt_monthdays`
--

CREATE TABLE `base_app_acnt_monthdays` (
  `id` bigint(20) NOT NULL,
  `month_fromdate` date DEFAULT NULL,
  `month_todate` date DEFAULT NULL,
  `month_workingdays` int(11) NOT NULL,
  `month_holidays` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_acnt_monthdays`
--

INSERT INTO `base_app_acnt_monthdays` (`id`, `month_fromdate`, `month_todate`, `month_workingdays`, `month_holidays`) VALUES
(1, '2022-04-01', '2022-04-30', 26, 4),
(2, '2022-05-01', '2022-05-31', 25, 6);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_attendance`
--

CREATE TABLE `base_app_attendance` (
  `id` bigint(20) NOT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(200) NOT NULL,
  `attendance_status` varchar(200) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_attendance`
--

INSERT INTO `base_app_attendance` (`id`, `date`, `status`, `attendance_status`, `user_id`) VALUES
(2, '2022-04-12', '', '1', 9),
(3, '2022-04-14', '', '1', 9),
(4, '2022-04-22', '', '0', 9),
(5, '2022-04-28', '', '1', 10),
(6, '2022-04-11', '', '1', 10);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_branch_registration`
--

CREATE TABLE `base_app_branch_registration` (
  `id` bigint(20) NOT NULL,
  `branch_name` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `branch_admin` varchar(100) NOT NULL,
  `branch_type` varchar(100) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_branch_registration`
--

INSERT INTO `base_app_branch_registration` (`id`, `branch_name`, `location`, `branch_admin`, `branch_type`, `mobile`, `email`, `logo`, `status`) VALUES
(1, 'Infox carnival', 'Kochi', 'anand', 'head', '8975485214', 'infox@gmail.com', 'images/infox.jpeg', '');

-- --------------------------------------------------------

--
-- Table structure for table `base_app_conditions`
--

CREATE TABLE `base_app_conditions` (
  `id` bigint(20) NOT NULL,
  `condition1` varchar(1000) NOT NULL,
  `condition2` varchar(1000) NOT NULL,
  `condition3` varchar(1000) NOT NULL,
  `condition4` varchar(1000) NOT NULL,
  `condition5` varchar(1000) NOT NULL,
  `condition6` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_conditions`
--

INSERT INTO `base_app_conditions` (`id`, `condition1`, `condition2`, `condition3`, `condition4`, `condition5`, `condition6`) VALUES
(1, ' You will be under probation for six months with no salary /stipend from the date of appointment and on your services during the said probation period being found satisfactory, the Company will offer you a starting salary in between 1.4 L – 1.8L per annum based on your performance in the probation period.', ' Your normal working hours’ will be 54 hours’ per week, to be worked Monday to Saturday. If company suggests at times, you are requested to work on holidays also.', 'You are entitled for 12 days leave for each 12 months continued service.', 'If company suggests at times, you are requested to relocate to other job locations also.', ' The notice period for resigning from the job is 2 months, on your relieve, you have to complete and submit all the assigned work properly, unless you have to pay the compensation.', 'The Company has the rights to terminate you from the job immediately at any time for genuine reasons like mis behaviour, malpractices, spy works, lack of performances in work, illegal activities and so on.');

-- --------------------------------------------------------

--
-- Table structure for table `base_app_course`
--

CREATE TABLE `base_app_course` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `total_fee` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_course`
--

INSERT INTO `base_app_course` (`id`, `name`, `total_fee`) VALUES
(1, 'Django', 40000),
(2, 'Bootstrap', 20000),
(3, 'C#', 10000),
(4, 'Kubernets', 70000);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_create_team`
--

CREATE TABLE `base_app_create_team` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `trainer` varchar(200) NOT NULL,
  `progress` int(11) NOT NULL,
  `status` varchar(200) NOT NULL,
  `team_count` int(11) NOT NULL,
  `team_status` varchar(200) NOT NULL,
  `trainer_id` varchar(200) DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  `startdate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_create_team`
--

INSERT INTO `base_app_create_team` (`id`, `name`, `trainer`, `progress`, `status`, `team_count`, `team_status`, `trainer_id`, `enddate`, `startdate`) VALUES
(4, '       team1', 'Trainerrrrr', 0, '', 0, '1', '2', '2022-05-07', '2022-04-28'),
(5, '   team2', 'Trainerrrrr', 100, '', 0, '1', '2', NULL, NULL),
(6, '    team xq', 'Trainer1', 0, '', 0, '1', '4', NULL, NULL),
(7, ' testn', 'Trainer1', 0, '', 0, '1', '4', NULL, NULL),
(8, ' nnnnnnns', 'Trainer1', 0, '', 0, '0', '4', '2022-04-30', '2022-04-29'),
(9, 'team7', 'Trainer1', 0, '', 0, '1', '4', '2022-05-07', '2022-04-27');

-- --------------------------------------------------------

--
-- Table structure for table `base_app_department`
--

CREATE TABLE `base_app_department` (
  `id` bigint(20) NOT NULL,
  `department` varchar(100) NOT NULL,
  `files` varchar(100) DEFAULT NULL,
  `status` varchar(100) NOT NULL,
  `branch_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_department`
--

INSERT INTO `base_app_department` (`id`, `department`, `files`, `status`, `branch_id`) VALUES
(2, 'python', 'images/icons8-python-150_BPlXDds.png', '', 1),
(3, 'machine learning', 'images/icons8-java-150_-_Copy_Byb7vAv.png', '', 1);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_designation`
--

CREATE TABLE `base_app_designation` (
  `id` bigint(20) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `files` varchar(100) DEFAULT NULL,
  `status` varchar(100) NOT NULL,
  `branch_id` bigint(20) DEFAULT NULL,
  `department_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_designation`
--

INSERT INTO `base_app_designation` (`id`, `designation`, `files`, `status`, `branch_id`, `department_id`) VALUES
(1, 'admin', 'icons8-manager-90.png', '', 1, 2),
(2, 'manager', 'icons8-manager-90.png', '', 1, 2),
(3, 'project manager', 'icons8-manager-90.png', '', 1, 2),
(4, 'team leader', 'icons8-manager-90.png', '', 1, 2),
(5, 'tester', 'icons8-manager-90.png', '', 1, 2),
(6, 'developer', 'icons8-manager-90.png', '', 1, 2),
(7, 'trainingmanager', 'icons8-manager-90.png', '', 1, 2),
(8, 'trainer', 'icons8-manager-90.png', '', 1, 2),
(9, 'trainee', 'icons8-manager-90.png', '', 1, 2),
(10, 'account', 'icons8-manager-90.png', '', 1, 2),
(11, 'hr', 'icons8-manager-90.png', '', 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_extracurricular`
--

CREATE TABLE `base_app_extracurricular` (
  `id` bigint(20) NOT NULL,
  `internshipdetails` varchar(240) DEFAULT NULL,
  `internshipduration` varchar(240) DEFAULT NULL,
  `internshipcertificate` varchar(100) DEFAULT NULL,
  `onlinetrainingdetails` varchar(240) DEFAULT NULL,
  `onlinetrainingduration` varchar(240) DEFAULT NULL,
  `onlinetrainingcertificate` varchar(100) DEFAULT NULL,
  `projecttitle` varchar(240) DEFAULT NULL,
  `projectduration` varchar(240) DEFAULT NULL,
  `projectdescription` longtext DEFAULT NULL,
  `projecturl` varchar(240) DEFAULT NULL,
  `skill1` varchar(240) DEFAULT NULL,
  `skill2` varchar(240) DEFAULT NULL,
  `skill3` varchar(240) DEFAULT NULL,
  `status` varchar(240) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_app_internship`
--

CREATE TABLE `base_app_internship` (
  `id` bigint(20) NOT NULL,
  `reg_date` date DEFAULT NULL,
  `fullname` varchar(200) NOT NULL,
  `collegename` varchar(200) NOT NULL,
  `reg_no` varchar(200) NOT NULL,
  `course` varchar(200) NOT NULL,
  `stream` varchar(200) NOT NULL,
  `platform` varchar(200) NOT NULL,
  `start_date` varchar(200) NOT NULL,
  `end_date` varchar(200) NOT NULL,
  `mobile` varchar(200) NOT NULL,
  `alternative_no` varchar(200) NOT NULL,
  `email` varchar(254) NOT NULL,
  `profile_pic` varchar(100) DEFAULT NULL,
  `attach_file` varchar(100) DEFAULT NULL,
  `rating` varchar(200) NOT NULL,
  `hrmanager` varchar(200) NOT NULL,
  `guide` varchar(200) NOT NULL,
  `qr` varchar(200) NOT NULL,
  `status` varchar(200) NOT NULL,
  `complete_status` varchar(10) NOT NULL,
  `verify_status` varchar(10) NOT NULL,
  `total_fee` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `pay_date` date DEFAULT NULL,
  `balance` int(11) NOT NULL,
  `total_pay` int(11) NOT NULL,
  `branch_id` bigint(20) DEFAULT NULL,
  `internshiptype_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_internship`
--

INSERT INTO `base_app_internship` (`id`, `reg_date`, `fullname`, `collegename`, `reg_no`, `course`, `stream`, `platform`, `start_date`, `end_date`, `mobile`, `alternative_no`, `email`, `profile_pic`, `attach_file`, `rating`, `hrmanager`, `guide`, `qr`, `status`, `complete_status`, `verify_status`, `total_fee`, `amount`, `pay_date`, `balance`, `total_pay`, `branch_id`, `internshiptype_id`) VALUES
(2, '2022-03-15', 'Intern3', 'intern2 college', 'INT002', 'B.COM', 'INTStream', 'INTPF', '03/20/2022', '03/26/2022', '126126126', '325325325', 'Intern2@gmail.com', 'images/face26.jpg', 'images/face26_6LtQNxC.jpg', '', '', '', '/home/apgbadgk6j6n/public_html/managezone.in/infox-main/media\\2.png', '', '1', '1', 55000, 0, NULL, 0, 0, 1, 1),
(3, '2022-03-16', 'AKHIL RAJ M R', 'testing..', 'testing..', 'B.TECH', 'testing..', 'testing..', '2022-03-17', '2022-03-31', '123456789', '123456789', 'testing@gmail.com', 'images/JR8ilHf_CSJFei2.jpg', 'images/JR8ilHf_NOb1tIj.jpg', 'Good', 'Anand Sekhar', '', '/home/apgbadgk6j6n/public_html/managezone.in/infox-main/media\\3.png', '', '0', '1', 55000, 10000, '2022-04-08', 45000, 10000, 1, 1),
(4, '2022-03-19', 'amal cs', 'amal cs', 'amal cs13', 'MCA', 'amal cs', 'amal cs', '2022-03-20', '2022-03-31', '123456789', '123456798', 'dsfgsdfg', 'images/face5_cI3YfIr.jpg', 'images/face8.jpg', '', '', '', '/home/apgbadgk6j6n/public_html/managezone.in/infox-main/media\\4.png', '', '1', '0', 0, 0, NULL, 0, 0, 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_internship_paydata`
--

CREATE TABLE `base_app_internship_paydata` (
  `id` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `amount` int(11) NOT NULL,
  `internship_user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_internship_paydata`
--

INSERT INTO `base_app_internship_paydata` (`id`, `date`, `amount`, `internship_user_id`) VALUES
(1, '2022-04-08', 10000, 3);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_internship_type`
--

CREATE TABLE `base_app_internship_type` (
  `id` bigint(20) NOT NULL,
  `type` varchar(100) NOT NULL,
  `duration` varchar(100) NOT NULL,
  `fee` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_internship_type`
--

INSERT INTO `base_app_internship_type` (`id`, `type`, `duration`, `fee`) VALUES
(1, 'python', '6 month', '55000'),
(2, 'React', '3 Months', '30000');

-- --------------------------------------------------------

--
-- Table structure for table `base_app_leave`
--

CREATE TABLE `base_app_leave` (
  `id` bigint(20) NOT NULL,
  `from_date` date DEFAULT NULL,
  `to_date` date DEFAULT NULL,
  `reason` longtext NOT NULL,
  `leave_status` varchar(200) NOT NULL,
  `status` varchar(200) NOT NULL,
  `designation_id` varchar(200) NOT NULL,
  `leaveapprovedstatus` varchar(200) NOT NULL,
  `leave_rejected_reason` varchar(300) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_leave`
--

INSERT INTO `base_app_leave` (`id`, `from_date`, `to_date`, `reason`, `leave_status`, `status`, `designation_id`, `leaveapprovedstatus`, `leave_rejected_reason`, `user_id`) VALUES
(1, '2022-04-22', '2022-04-30', 'test', 'full Day', '', '7', '0', '', 1),
(2, '2022-04-22', '2022-04-30', 'submit', '0', 'pending', '', '', '', 9),
(3, '2022-04-22', '2022-04-30', '123', 'full Day', '', '7', '0', '', 1),
(4, '2022-04-22', '2022-04-30', 'submit', 'full Day', '', '', '', '', 9),
(5, '2022-04-23', '2022-05-07', 'test1', 'full Day', '', '', '', '', 9),
(6, '2022-04-23', '2022-05-07', 'test1', 'full Day', '', '', '0', '', 9),
(7, '2022-04-22', '2022-05-04', 'nn', 'full Day', '', '', '0', '', 9),
(8, '2022-04-22', '2022-05-04', 'nn', 'full Day', '', '6', '2', 'uu', 9),
(9, '2022-04-22', '2022-04-30', 'aaa', 'full Day', '', '6', '1', '', 9),
(10, '2022-04-23', '2022-04-23', 'test', 'full Day', '', 'hr', '0', '', 11),
(11, '2022-04-28', '2022-05-07', 'test', 'full Day', '', '11', '0', '', 11),
(12, '2022-04-28', '2022-05-06', 'test1', 'full Day', '', '11', '0', '', 11),
(13, '2022-04-23', '2022-05-03', 'test', 'full Day', '', '11', '0', '', 12),
(14, '2022-04-23', '2022-04-23', 'test', 'half Day', '', '11', '0', '', 12),
(15, '2022-04-29', '2022-04-29', 'test', 'full Day', '', '11', '0', '', 12),
(16, '2022-05-07', '2022-05-07', 'test', 'full Day', '', '11', '0', '', 11),
(17, '2022-04-27', '2022-05-06', 'maria', 'full Day', '', '11', '0', '', 11),
(18, '2022-04-29', '2022-05-05', 'test', 'full Day', '', '5', '0', '', 14),
(19, '2022-04-29', '2022-05-02', 'df', 'full Day', '', '5', '0', '', 14),
(20, '2022-04-29', '2022-05-02', 'df', 'full Day', '', '5', '0', '', 14);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_paymentlist`
--

CREATE TABLE `base_app_paymentlist` (
  `id` bigint(20) NOT NULL,
  `amount_pay` int(11) NOT NULL,
  `amount_date` date DEFAULT NULL,
  `current_date` date DEFAULT NULL,
  `amount_status` varchar(200) DEFAULT NULL,
  `amount_downlod` varchar(100) DEFAULT NULL,
  `balance_amt` int(11) NOT NULL,
  `course_id` bigint(20) DEFAULT NULL,
  `user_id_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_app_previousteam`
--

CREATE TABLE `base_app_previousteam` (
  `id` bigint(20) NOT NULL,
  `pstatus` varchar(200) NOT NULL,
  `progress` int(11) NOT NULL,
  `teamname_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_previousteam`
--

INSERT INTO `base_app_previousteam` (`id`, `pstatus`, `progress`, `teamname_id`, `user_id`) VALUES
(1, '0', 0, 4, 3),
(2, '0', 0, 5, 5),
(3, '0', 0, 5, 5),
(4, '0', 0, 4, 5),
(5, '0', 10, 8, 3),
(6, '0', 0, 9, 5),
(7, '0', 0, 7, 5),
(8, '0', 0, 6, 3),
(9, '0', 0, 6, 5);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_probation`
--

CREATE TABLE `base_app_probation` (
  `id` bigint(20) NOT NULL,
  `startdate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  `reason` longtext NOT NULL,
  `extension` int(11) NOT NULL,
  `stopdate` date DEFAULT NULL,
  `renewdate` date DEFAULT NULL,
  `status` int(11) NOT NULL,
  `team_id` bigint(20) DEFAULT NULL,
  `trainer_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `stop_reason` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_probation`
--

INSERT INTO `base_app_probation` (`id`, `startdate`, `enddate`, `reason`, `extension`, `stopdate`, `renewdate`, `status`, `team_id`, `trainer_id`, `user_id`, `stop_reason`) VALUES
(1, NULL, NULL, '', 38, '2022-03-18', '2022-04-14', 0, NULL, NULL, 3, 'test'),
(2, NULL, NULL, '', 9, '2022-04-16', '2022-04-25', 0, NULL, NULL, 3, 'test1'),
(3, NULL, NULL, '', 2, '2022-04-23', '2022-04-30', 0, NULL, NULL, 3, 'vv'),
(4, NULL, NULL, '', 0, '2022-04-25', '2022-04-25', 0, NULL, NULL, 3, 'fg'),
(5, NULL, NULL, '', 2, '2022-04-24', '2022-04-26', 0, NULL, NULL, 3, 'test');

-- --------------------------------------------------------

--
-- Table structure for table `base_app_project`
--

CREATE TABLE `base_app_project` (
  `id` bigint(20) NOT NULL,
  `project` varchar(100) DEFAULT NULL,
  `rejectdate` date DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `startdate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  `files` varchar(100) DEFAULT NULL,
  `progress` varchar(100) NOT NULL,
  `user_reason` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `branch_id` bigint(20) DEFAULT NULL,
  `department_id` bigint(20) DEFAULT NULL,
  `designation_id` bigint(20) DEFAULT NULL,
  `projectmanager_id` bigint(20) DEFAULT NULL,
  `tester_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_project`
--

INSERT INTO `base_app_project` (`id`, `project`, `rejectdate`, `description`, `startdate`, `enddate`, `files`, `progress`, `user_reason`, `status`, `branch_id`, `department_id`, `designation_id`, `projectmanager_id`, `tester_id`) VALUES
(1, 'test', NULL, 'test..', '2022-04-24', '2022-04-29', 'images/Screenshot_138.png', '100', NULL, 'completed', NULL, 2, NULL, 6, NULL),
(2, 'test1', NULL, 'test..', '2022-04-24', '2022-04-29', 'images/Screenshot_138.png', '100', NULL, 'completed', NULL, 2, NULL, 16, NULL),
(3, 'tESTING', NULL, 'TESTING', '2022-04-28', '2022-05-07', 'images/urls.py', '', NULL, 'assigned', 1, 2, NULL, 6, NULL),
(4, 'test', NULL, 'd', '2022-04-29', '2022-05-07', 'images/Screenshot_173.png', '', NULL, 'assigned', 1, 2, NULL, 6, NULL),
(5, 'ttttt', NULL, 'tttt', '2022-04-29', '2022-05-07', 'images/Screenshot_174.png', '', NULL, 'assigned', 1, 2, NULL, 6, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_project_module_assign`
--

CREATE TABLE `base_app_project_module_assign` (
  `id` bigint(20) NOT NULL,
  `description` longtext NOT NULL,
  `module` varchar(255) DEFAULT NULL,
  `project_name_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_project_module_assign`
--

INSERT INTO `base_app_project_module_assign` (`id`, `description`, `module`, `project_name_id`) VALUES
(1, 'test', 'python', 1),
(2, 'test1', 'react', 2),
(3, 'bbbbbb', 'test', 1),
(4, 'nnnnn', 'ttttt', 1),
(5, 'TESTING', 'GGGG', 3),
(6, 'kmln', 'bbbb', 3);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_project_table`
--

CREATE TABLE `base_app_project_table` (
  `id` bigint(20) NOT NULL,
  `description` longtext NOT NULL,
  `module_name_id` varchar(255) DEFAULT NULL,
  `project_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_project_table`
--

INSERT INTO `base_app_project_table` (`id`, `description`, `module_name_id`, `project_id`) VALUES
(1, 'testing', '4', 1),
(2, 'testing', '4', 1),
(3, 'gggg', '3', 1),
(4, 'TESTING', '5', 3),
(5, 'bl', '6', 3);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_project_taskassign`
--

CREATE TABLE `base_app_project_taskassign` (
  `id` bigint(20) NOT NULL,
  `description` longtext NOT NULL,
  `task` varchar(200) DEFAULT NULL,
  `subtask` varchar(200) DEFAULT NULL,
  `startdate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  `files` varchar(100) DEFAULT NULL,
  `extension` int(11) DEFAULT NULL,
  `reason` longtext DEFAULT NULL,
  `extension_status` varchar(200) DEFAULT NULL,
  `extension_date` date DEFAULT NULL,
  `tl_description` varchar(200) DEFAULT NULL,
  `submitted_date` date DEFAULT NULL,
  `employee_files` varchar(100) DEFAULT NULL,
  `employee_description` longtext DEFAULT NULL,
  `designation` varchar(200) DEFAULT NULL,
  `department` varchar(200) DEFAULT NULL,
  `progress` int(11) DEFAULT NULL,
  `projectstatus` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `delay` varchar(200) DEFAULT NULL,
  `developer_id` bigint(20) DEFAULT NULL,
  `project_id` bigint(20) DEFAULT NULL,
  `tester_id` bigint(20) DEFAULT NULL,
  `tl_id` bigint(20) DEFAULT NULL,
  `git_link` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_project_taskassign`
--

INSERT INTO `base_app_project_taskassign` (`id`, `description`, `task`, `subtask`, `startdate`, `enddate`, `files`, `extension`, `reason`, `extension_status`, `extension_date`, `tl_description`, `submitted_date`, `employee_files`, `employee_description`, `designation`, `department`, `progress`, `projectstatus`, `status`, `delay`, `developer_id`, `project_id`, `tester_id`, `tl_id`, `git_link`) VALUES
(1, 'Test', 'test', NULL, '2022-04-07', '2022-04-05', 'images/Screenshot_138_bUJnNqf.png', 0, NULL, NULL, NULL, NULL, '2022-05-04', '', 'test', NULL, NULL, 50, 'in progress', '', '14', 10, 1, 14, 10, 'https://github.com/Mariasusanabraham/coreappbackend.git');

-- --------------------------------------------------------

--
-- Table structure for table `base_app_promissory`
--

CREATE TABLE `base_app_promissory` (
  `id` bigint(20) NOT NULL,
  `inital_amount` varchar(100) DEFAULT NULL,
  `inital_paid_on` varchar(100) DEFAULT NULL,
  `inital_paid_amount` varchar(100) DEFAULT NULL,
  `inital_paid_date` varchar(100) DEFAULT NULL,
  `inital_balance_amount` varchar(100) DEFAULT NULL,
  `inital_due_date` varchar(100) DEFAULT NULL,
  `inital_total_payment` varchar(100) DEFAULT NULL,
  `second_amount` varchar(100) DEFAULT NULL,
  `second_due_on` varchar(100) DEFAULT NULL,
  `second_paid_amount` varchar(100) DEFAULT NULL,
  `second_paid_date` varchar(100) DEFAULT NULL,
  `second_balance_amount` varchar(100) DEFAULT NULL,
  `second_due_date` varchar(100) DEFAULT NULL,
  `second_total_payment` varchar(100) DEFAULT NULL,
  `final_amount` varchar(100) DEFAULT NULL,
  `final_due_on` varchar(100) DEFAULT NULL,
  `final_paid_amount` varchar(100) DEFAULT NULL,
  `final_paid_date` varchar(100) DEFAULT NULL,
  `final_balance_amount` varchar(100) DEFAULT NULL,
  `final_due_date` varchar(100) DEFAULT NULL,
  `final_total_payment` varchar(100) DEFAULT NULL,
  `complete_status` varchar(100) DEFAULT NULL,
  `user_id_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_app_qualification`
--

CREATE TABLE `base_app_qualification` (
  `id` bigint(20) NOT NULL,
  `plustwo` varchar(240) DEFAULT NULL,
  `schoolaggregate` varchar(240) DEFAULT NULL,
  `schoolcertificate` varchar(100) DEFAULT NULL,
  `ugdegree` varchar(240) DEFAULT NULL,
  `ugstream` varchar(240) DEFAULT NULL,
  `ugpassoutyr` varchar(240) DEFAULT NULL,
  `ugaggregrate` varchar(240) DEFAULT NULL,
  `backlogs` varchar(240) DEFAULT NULL,
  `ugcertificate` varchar(100) DEFAULT NULL,
  `pg` varchar(240) DEFAULT NULL,
  `status` varchar(100) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_app_reported_issue`
--

CREATE TABLE `base_app_reported_issue` (
  `id` bigint(20) NOT NULL,
  `issue` longtext NOT NULL,
  `reported_date` date DEFAULT NULL,
  `reply` longtext NOT NULL,
  `status` varchar(200) NOT NULL,
  `issuestatus` varchar(200) NOT NULL,
  `designation_id` varchar(200) NOT NULL,
  `reported_to_id` bigint(20) DEFAULT NULL,
  `reporter_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_reported_issue`
--

INSERT INTO `base_app_reported_issue` (`id`, `issue`, `reported_date`, `reply`, `status`, `issuestatus`, `designation_id`, `reported_to_id`, `reporter_id`) VALUES
(1, '                            nn', '2022-04-23', '', '', '0', '11', 7, 11),
(2, '                            test', '2022-04-23', '', '', '0', '11', 7, 12);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_tasks`
--

CREATE TABLE `base_app_tasks` (
  `id` bigint(20) NOT NULL,
  `tasks` varchar(240) NOT NULL,
  `startdate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  `files` varchar(100) DEFAULT NULL,
  `description` longtext NOT NULL,
  `status` varchar(200) NOT NULL,
  `department_id` bigint(20) DEFAULT NULL,
  `designation_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_app_tester_status`
--

CREATE TABLE `base_app_tester_status` (
  `id` bigint(20) NOT NULL,
  `date` date DEFAULT NULL,
  `workdone` longtext DEFAULT NULL,
  `files` varchar(100) DEFAULT NULL,
  `progress` int(11) NOT NULL,
  `status` varchar(200) DEFAULT NULL,
  `project_id` bigint(20) DEFAULT NULL,
  `subtask_id` bigint(20) DEFAULT NULL,
  `task_id` bigint(20) DEFAULT NULL,
  `tester_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_app_test_status`
--

CREATE TABLE `base_app_test_status` (
  `id` bigint(20) NOT NULL,
  `date` date DEFAULT NULL,
  `workdone` longtext DEFAULT NULL,
  `json` varchar(100) DEFAULT NULL,
  `json_testerscreenshot` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`json_testerscreenshot`)),
  `project_id` bigint(20) DEFAULT NULL,
  `subtask_id` bigint(20) DEFAULT NULL,
  `taskname_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `git_commit` longtext DEFAULT NULL,
  `git_link` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_test_status`
--

INSERT INTO `base_app_test_status` (`id`, `date`, `workdone`, `json`, `json_testerscreenshot`, `project_id`, `subtask_id`, `taskname_id`, `user_id`, `git_commit`, `git_link`) VALUES
(1, '2022-04-27', 'test', '', '[\"/media/Screenshot155png\"]', 1, 1, NULL, 10, 'test', 'https://github.com/Mariasusanabraham/coreappbackend.git'),
(2, '2022-04-27', 'test', '', '[\"/media/Screenshot158png\"]', 1, 2, NULL, 9, 'test1', 'https://github.com/Mariasusanabraham/coreappbackend.git'),
(3, '2022-04-27', 'ttt', '', '[\"/media/Screenshot161png\"]', 1, 2, NULL, 9, 'test33', 'https://github.com/Mariasusanabraham/aptitude_test.git');

-- --------------------------------------------------------

--
-- Table structure for table `base_app_topic`
--

CREATE TABLE `base_app_topic` (
  `id` bigint(20) NOT NULL,
  `topic` varchar(240) NOT NULL,
  `startdate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  `files` varchar(100) DEFAULT NULL,
  `description` longtext NOT NULL,
  `review` longtext NOT NULL,
  `status` varchar(200) NOT NULL,
  `topic_status` varchar(200) NOT NULL,
  `team_id` bigint(20) DEFAULT NULL,
  `trainee_id` bigint(20) DEFAULT NULL,
  `trainer_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_app_trainer_task`
--

CREATE TABLE `base_app_trainer_task` (
  `id` bigint(20) NOT NULL,
  `taskname` varchar(240) NOT NULL,
  `startdate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  `submitteddate` date DEFAULT NULL,
  `files` varchar(100) DEFAULT NULL,
  `description` longtext NOT NULL,
  `user_description` longtext NOT NULL,
  `user_files` varchar(100) DEFAULT NULL,
  `status` varchar(200) NOT NULL,
  `task_status` varchar(200) NOT NULL,
  `team_name_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `delay` int(11) NOT NULL,
  `task_progress` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_trainer_task`
--

INSERT INTO `base_app_trainer_task` (`id`, `taskname`, `startdate`, `enddate`, `submitteddate`, `files`, `description`, `user_description`, `user_files`, `status`, `task_status`, `team_name_id`, `user_id`, `delay`, `task_progress`) VALUES
(1, 'test', '2022-04-01', '2022-04-30', NULL, 'face2.jpg', '', '', 'face2.jpg', '', '0', 5, 5, 0, 0),
(2, 'test1', '2022-04-01', '2022-04-30', '2022-04-29', 'face2.jpg', '', 'test', 'images/trainer.html', '', '1', 5, 3, 0, 0),
(3, 'test2', '2022-04-01', '2022-04-15', '2022-04-22', 'face2.jpg', '', 'testttt', 'face2.jpg', '', '1', 5, 3, 7, 4),
(4, 'test', '2022-04-21', '2022-04-29', NULL, 'images/leya.pdf', 'nnn', 'nnn', 'face2.jpg', '', '1', 4, 3, 0, 40);

-- --------------------------------------------------------

--
-- Table structure for table `base_app_user_registration`
--

CREATE TABLE `base_app_user_registration` (
  `id` bigint(20) NOT NULL,
  `fullname` varchar(100) DEFAULT NULL,
  `fathername` varchar(100) DEFAULT NULL,
  `mothername` varchar(100) DEFAULT NULL,
  `dateofbirth` date DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `presentaddress1` varchar(100) DEFAULT NULL,
  `presentaddress2` varchar(100) DEFAULT NULL,
  `presentaddress3` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `permanentaddress1` varchar(100) DEFAULT NULL,
  `permanentaddress2` varchar(100) DEFAULT NULL,
  `permanentaddress3` varchar(100) DEFAULT NULL,
  `permanentpincode` varchar(100) DEFAULT NULL,
  `permanentdistrict` varchar(100) DEFAULT NULL,
  `permanentstate` varchar(100) DEFAULT NULL,
  `permanentcountry` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `alternativeno` varchar(100) DEFAULT NULL,
  `employee_id` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `idproof` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `attitude` int(11) NOT NULL,
  `creativity` int(11) NOT NULL,
  `workperformance` int(11) NOT NULL,
  `joiningdate` date DEFAULT NULL,
  `startdate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `tl_id` int(11) DEFAULT NULL,
  `projectmanager_id` int(11) DEFAULT NULL,
  `total_pay` int(11) NOT NULL,
  `payment_balance` int(11) NOT NULL,
  `account_no` varchar(100) DEFAULT NULL,
  `ifsc` varchar(100) DEFAULT NULL,
  `bank_name` varchar(100) DEFAULT NULL,
  `bank_branch` varchar(100) DEFAULT NULL,
  `payment_status` varchar(200) DEFAULT NULL,
  `offerqr` varchar(100) DEFAULT NULL,
  `relieveqr` varchar(100) DEFAULT NULL,
  `expqr` varchar(100) DEFAULT NULL,
  `hrmanager` varchar(100) DEFAULT NULL,
  `confirm_salary` varchar(255) NOT NULL,
  `confirm_salary_status` varchar(255) NOT NULL,
  `payment_file_downlod` varchar(100) DEFAULT NULL,
  `total_amount` int(11) NOT NULL,
  `payment_amount_date` date DEFAULT NULL,
  `salary_pending` varchar(100) NOT NULL,
  `salary_status` varchar(10) NOT NULL,
  `trainer_level` varchar(20) DEFAULT NULL,
  `branch_id` bigint(20) DEFAULT NULL,
  `course_id` bigint(20) DEFAULT NULL,
  `department_id` bigint(20) DEFAULT NULL,
  `designation_id` bigint(20) DEFAULT NULL,
  `team_id` bigint(20) DEFAULT NULL,
  `hr_designation` varchar(120) DEFAULT NULL,
  `reg_status` varchar(10) NOT NULL,
  `trainee_delay` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `base_app_user_registration`
--

INSERT INTO `base_app_user_registration` (`id`, `fullname`, `fathername`, `mothername`, `dateofbirth`, `gender`, `presentaddress1`, `presentaddress2`, `presentaddress3`, `pincode`, `district`, `state`, `country`, `permanentaddress1`, `permanentaddress2`, `permanentaddress3`, `permanentpincode`, `permanentdistrict`, `permanentstate`, `permanentcountry`, `mobile`, `alternativeno`, `employee_id`, `email`, `password`, `idproof`, `photo`, `attitude`, `creativity`, `workperformance`, `joiningdate`, `startdate`, `enddate`, `status`, `tl_id`, `projectmanager_id`, `total_pay`, `payment_balance`, `account_no`, `ifsc`, `bank_name`, `bank_branch`, `payment_status`, `offerqr`, `relieveqr`, `expqr`, `hrmanager`, `confirm_salary`, `confirm_salary_status`, `payment_file_downlod`, `total_amount`, `payment_amount_date`, `salary_pending`, `salary_status`, `trainer_level`, `branch_id`, `course_id`, `department_id`, `designation_id`, `team_id`, `hr_designation`, `reg_status`, `trainee_delay`) VALUES
(1, 'Training Manager', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'tm@gmail.com', '123', '', 'images/face2_UhWkYOj.jpg', 0, 0, 0, NULL, '2022-03-01', '2022-05-31', 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 0, NULL, '', '', NULL, 1, 1, 2, 7, 4, NULL, '', 0),
(2, 'Trainerrrrr', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'trainer@gmail.com', '123', '', 'images/julian-wan-WNoLnJo7tS8-unsplash.jpg', 20, 50, 20, NULL, NULL, NULL, 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 0, NULL, '', '', NULL, 1, 1, 2, 8, 4, NULL, '', 0),
(3, 'Trainee', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'trainee@gmail.com', '123', '', 'images/michael-dam-mEZ3PoFGs_k-unsplash.jpg', 10, 10, 10, NULL, '2022-03-01', '2022-05-10', 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 20000, NULL, '', '', NULL, 1, 2, 2, 9, 6, NULL, '', 79),
(4, 'Trainer1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'trainer1@gmail.com', '123', '', 'images/julian-wan-WNoLnJo7tS8-unsplash.jpg', 100, 40, 0, NULL, NULL, NULL, 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 0, NULL, '', '', NULL, 1, 1, 2, 8, 4, NULL, '', 0),
(5, 'Trainee1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'trainee1@gmail.com', '123', '', 'images/michael-dam-mEZ3PoFGs_k-unsplash.jpg', 0, 0, 0, NULL, NULL, NULL, 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 40000, NULL, '', '', NULL, 1, 1, 2, 9, 6, NULL, '', 0),
(6, 'pm', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'pm@gmail.com', '123', '', 'images/michael-dam-mEZ3PoFGs_k-unsplash.jpg', 0, 0, 0, NULL, NULL, NULL, 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 40000, NULL, '', '', NULL, 1, 1, 2, 3, 5, NULL, '', 0),
(7, 'admin', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'admin@gmail.com', '123', '', 'images/michael-dam-mEZ3PoFGs_k-unsplash.jpg', 0, 0, 0, NULL, NULL, NULL, 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 40000, NULL, '', '', NULL, 1, 1, 2, 1, 5, NULL, '', 0),
(8, 'manager', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'manager@gmail.com', '123', '', 'images/michael-dam-mEZ3PoFGs_k-unsplash.jpg', 0, 0, 0, NULL, NULL, NULL, 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 40000, NULL, '', '', NULL, 1, 1, 2, 2, 5, NULL, '', 0),
(9, 'developer', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'dev@gmail.com', '123', '', 'images/michael-dam-mEZ3PoFGs_k-unsplash.jpg', 10, 40, 40, NULL, NULL, NULL, 'active', 10, 6, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '20000', '1', '', 40000, NULL, '', '', NULL, 1, 1, 2, 6, 5, NULL, '', 0),
(10, 'tl', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'tl@gmail.com', '123', '', 'images/michael-dam-mEZ3PoFGs_k-unsplash.jpg', 20, 40, 40, NULL, NULL, NULL, 'active', NULL, 6, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 40000, NULL, '', '', NULL, 1, 1, 2, 4, 5, NULL, '', 0),
(11, 'hr', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'hr@gmail.com', '12', '', 'face2.jpg', 0, 0, 0, NULL, NULL, NULL, 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 40000, NULL, '', '', NULL, 1, 1, 2, 11, NULL, NULL, '', 0),
(12, 'hr1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'hr1@gmail.com', '123', '', 'face2.jpg', 0, 0, 0, NULL, NULL, NULL, 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 40000, NULL, '', '', NULL, 1, 1, 2, 11, NULL, NULL, '', 0),
(13, 'Trainer2', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'trainer2@gmail.com', '123', '', 'images/julian-wan-WNoLnJo7tS8-unsplash.jpg', 20, 40, 40, NULL, NULL, NULL, 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 0, NULL, '', '', NULL, 1, 1, 3, 8, 4, NULL, '', 0),
(14, 'tester', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'ts@gmail.com', '123', '', 'images/julian-wan-WNoLnJo7tS8-unsplash.jpg', 0, 0, 0, NULL, NULL, NULL, 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 0, NULL, '', '', NULL, 1, 1, 2, 5, 4, NULL, '', 0),
(15, 'account', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'accnt@gmail.com', '123', '', 'images/julian-wan-WNoLnJo7tS8-unsplash.jpg', 0, 0, 0, NULL, NULL, NULL, 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 0, NULL, '', '', NULL, 1, 1, 2, 10, 4, NULL, '', 0),
(16, 'pm1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'pm1@gmail.com', '123', '', 'images/michael-dam-mEZ3PoFGs_k-unsplash.jpg', 0, 0, 0, NULL, NULL, NULL, 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 40000, NULL, '', '', NULL, 1, 1, 2, 3, 5, NULL, '', 0),
(17, 'pm2', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'pm2@gmail.com', '123', '', 'images/michael-dam-mEZ3PoFGs_k-unsplash.jpg', 0, 0, 0, NULL, NULL, NULL, 'active', NULL, NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 40000, NULL, '', '', NULL, 1, 1, 2, 3, 5, NULL, '', 0),
(18, 'tl1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'tl1@gmail.com', '123', '', 'images/michael-dam-mEZ3PoFGs_k-unsplash.jpg', 20, 40, 40, NULL, NULL, NULL, 'active', 10, 6, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', 40000, NULL, '', '', NULL, 1, 1, 2, 6, 5, NULL, '', 0);

-- --------------------------------------------------------

--
-- Table structure for table `cal_event`
--

CREATE TABLE `cal_event` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `start_time` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cal_event`
--

INSERT INTO `cal_event` (`id`, `title`, `description`, `start_time`) VALUES
(2, 'test1', 'test', '2022-05-04'),
(3, 'testss', 'testinggg', '2022-05-08');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(8, 'base_app', 'acntexpensest'),
(34, 'base_app', 'acntspayslip'),
(7, 'base_app', 'acnt_monthdays'),
(33, 'base_app', 'attendance'),
(9, 'base_app', 'branch_registration'),
(10, 'base_app', 'conditions'),
(11, 'base_app', 'course'),
(12, 'base_app', 'create_team'),
(13, 'base_app', 'department'),
(14, 'base_app', 'designation'),
(32, 'base_app', 'extracurricular'),
(15, 'base_app', 'internship'),
(31, 'base_app', 'internship_paydata'),
(16, 'base_app', 'internship_type'),
(30, 'base_app', 'leave'),
(29, 'base_app', 'paymentlist'),
(28, 'base_app', 'previousteam'),
(35, 'base_app', 'probation'),
(17, 'base_app', 'project'),
(36, 'base_app', 'project_modules'),
(38, 'base_app', 'project_module_assign'),
(37, 'base_app', 'project_table'),
(18, 'base_app', 'project_taskassign'),
(27, 'base_app', 'promissory'),
(26, 'base_app', 'qualification'),
(25, 'base_app', 'reported_issue'),
(24, 'base_app', 'tasks'),
(22, 'base_app', 'tester_status'),
(23, 'base_app', 'test_status'),
(21, 'base_app', 'topic'),
(20, 'base_app', 'trainer_task'),
(19, 'base_app', 'user_registration'),
(39, 'cal', 'event'),
(40, 'cal', 'example'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-04-20 05:16:08.350331'),
(2, 'auth', '0001_initial', '2022-04-20 05:16:08.809579'),
(3, 'admin', '0001_initial', '2022-04-20 05:16:08.939532'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-04-20 05:16:08.957369'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-04-20 05:16:08.973325'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-04-20 05:16:09.043138'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-04-20 05:16:09.157498'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-04-20 05:16:09.186420'),
(9, 'auth', '0004_alter_user_username_opts', '2022-04-20 05:16:09.210356'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-04-20 05:16:09.269198'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-04-20 05:16:09.274187'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-04-20 05:16:09.287152'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-04-20 05:16:09.311087'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-04-20 05:16:09.333029'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-04-20 05:16:09.363951'),
(16, 'auth', '0011_update_proxy_permissions', '2022-04-20 05:16:09.377909'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-04-20 05:16:09.400849'),
(18, 'base_app', '0001_initial', '2022-04-20 05:16:13.034411'),
(19, 'base_app', '0002_remove_acntspayslip_pending_status_and_more', '2022-04-20 05:16:16.559691'),
(20, 'sessions', '0001_initial', '2022-04-20 05:16:16.599081'),
(21, 'base_app', '0003_create_team_trainer_id', '2022-04-20 05:51:51.053281'),
(22, 'base_app', '0002_create_team_enddate_create_team_startdate', '2022-04-20 10:48:08.211407'),
(23, 'base_app', '0003_trainer_task_delay', '2022-04-21 03:50:24.368539'),
(24, 'base_app', '0004_trainer_task_task_progress', '2022-04-21 05:12:05.237908'),
(25, 'base_app', '0005_probation', '2022-04-21 06:28:35.747289'),
(26, 'base_app', '0006_alter_probation_options', '2022-04-22 04:38:05.434648'),
(27, 'base_app', '0007_probation_stop_reason', '2022-04-22 04:47:42.460508'),
(28, 'base_app', '0008_user_registration_trainee_delay', '2022-04-22 06:44:44.346789'),
(29, 'base_app', '0009_test_status_git_commit_test_status_git_link', '2022-04-27 05:33:10.348241'),
(30, 'base_app', '0010_project_taskassign_git_link', '2022-04-27 05:50:29.910255'),
(31, 'base_app', '0011_project_modules_remove_user_registration_signature_and_more', '2022-04-28 06:30:15.257986'),
(32, 'base_app', '0012_alter_project_module_assign_project_name', '2022-04-28 07:32:50.479532'),
(33, 'base_app', '0013_alter_project_table_project', '2022-04-28 07:33:01.350542'),
(34, 'base_app', '0014_alter_project_module_assign_module', '2022-04-28 08:10:53.121920'),
(35, 'base_app', '0015_alter_project_table_module_name_id', '2022-04-28 08:21:09.007557'),
(36, 'base_app', '0016_delete_project_modules', '2022-05-07 09:04:45.209172'),
(37, 'cal', '0001_initial', '2022-05-07 09:04:45.223452'),
(38, 'cal', '0002_remove_event_end_time', '2022-05-07 09:25:51.853190'),
(39, 'cal', '0003_alter_event_start_time', '2022-05-07 09:26:42.353014'),
(40, 'cal', '0002_event', '2022-05-07 10:02:45.009445'),
(41, 'cal', '0003_delete_example', '2022-05-07 10:25:25.080896'),
(42, 'base_app', '0017_acntspayslip_net_salary', '2022-05-11 10:15:54.805425');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2je6ox9elrs1ngbn12bt6aljp7yrw565', '.eJxVjTEOgCAMRa9i_uwCmKi9g5sXYGgIAx2KTsa7i4vSbv_99vXCWVklFj4KaB676EDYNWbJkoYtSkys6Bc8yHVZRUGLBZ-D9R3YNoAmS5rSG1JBqwW_kq2utuNgyfvgfgCHGU-P:1nhRDp:-cXEihqqzkS-vPmW_9iXGizZMmyTjuzXdTOu6k0Mnts', '2022-05-05 07:27:25.436825'),
('5ijbup2jg1iez3e32vmsoz5qbxuczaf2', '.eJyrVirJyUxRsjI00FEqLsjJLAFxlIyVdJRSUstAbEsdpdLi1KK8xNzUxOS8EohKZBFDoPrE5OT8UqAkqowRULGpjlJBEcgcMx0lx5TceBDTHKGspBisPSU3Mw9Jc0YRSGstAE0JMl0:1npMzo:O5T4pwzVWtKuxYQrsAmKR4IHrFi9CWJlCfuBTlHDnw8', '2022-05-27 04:33:44.758577'),
('74ocwn36pilbcwg8b15zjdb7ti4tj75o', '.eJyrViotTi3KS8xNLclVsjLXQeIaKlkphRQlZuZl5qUr-CbmJaanFikhKzBSsjJE4hflFSlZWaAKwM1A1QqUMVayMkEVARpnhCJSrGRliSqAMC4V1bhioGZjVBGQBbUAHVJNxw:1nh3C7:StLz5XIzKSyeI41Ju40mtByhdKzLsls2a4IyC6XlWCg', '2022-05-04 05:48:03.725602'),
('nsniishqgbmnjf0qnt2l3amg4a4lx1qi', '.eJyrViotTi3KS8xNTUzOK1GyMjTQQRExVLJSSkxOzi8FSqLKGAEVm9YCAODAFjg:1nnyb2:41DaXKhSJJvoE5gMIfnsVITRJvJiWt7QwkkGnq8mmLc', '2022-05-23 08:18:24.269125'),
('oje7yzl4m9wxdvjt35j0x88wbu7x60sa', '.eJyrViotTi3KS8xNLSnKK1aystRBETBUslIKKUrMzEtNVUKVMVKyMkYVMVayMtNRKijKTAEyagGZZx7k:1nlNLJ:N90WsiQERfETar3SyC_FT0V9HqFtGg8tvOyuENJ6p0E', '2022-05-16 04:07:25.578049'),
('phayjgqfcxeorzjp7up2m2rlfftfjpfd', 'eyJwcmlkIjo2LCJ0bGlkIjoxMCwic3BsaXRpZCI6IjUifQ:1nkh59:xaD0p8OOXRc92S395xO5b7AMnmoFBPKbMGDUBwDwMXQ', '2022-05-14 06:59:55.448329'),
('u2vyfbaz3st3hc03yanqmakd9l9qs5qf', 'eyJwcmlkIjo2fQ:1npUhw:8mGd7HRW2kinFsR1hNiU4AEv2dCKLzIBDwVN8knJgvU', '2022-05-27 12:47:48.169593'),
('ucwq6hpyhtpm4i9y4rl3fb3hm8pxpt6z', '.eJxNjbEOAiEQRH_FTE0hFl6Ozg-wszerkIPk2FwWtLn477JcQzcvmZm3Y5Pk4a4GnxKEKYea4aYRLRweQokTL6c7MS1BMBYucNYgylOf7BF9KCNqsd1EHTZ8CfE79tnN514clUWV5HPiwRPl8NS1_54NyramqgDbej58Nc-_P804Q7o:1njbA6:YjIvAvEVPTz-AYPrIX7kDFRHvK2r9pR7TiousaNNp9Q', '2022-05-11 06:28:30.571048');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `base_app_acntexpensest`
--
ALTER TABLE `base_app_acntexpensest`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `base_app_acntspayslip`
--
ALTER TABLE `base_app_acntspayslip`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_acntspaysli_department_id_21ada824_fk_base_app_` (`department_id`),
  ADD KEY `base_app_acntspaysli_designation_id_00bcb706_fk_base_app_` (`designation_id`),
  ADD KEY `base_app_acntspaysli_user_id_id_fce5649e_fk_base_app_` (`user_id_id`);

--
-- Indexes for table `base_app_acnt_monthdays`
--
ALTER TABLE `base_app_acnt_monthdays`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `base_app_attendance`
--
ALTER TABLE `base_app_attendance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_attendance_user_id_430c8040_fk_base_app_` (`user_id`);

--
-- Indexes for table `base_app_branch_registration`
--
ALTER TABLE `base_app_branch_registration`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `base_app_conditions`
--
ALTER TABLE `base_app_conditions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `base_app_course`
--
ALTER TABLE `base_app_course`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `base_app_create_team`
--
ALTER TABLE `base_app_create_team`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `base_app_department`
--
ALTER TABLE `base_app_department`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_department_branch_id_eabcf909_fk_base_app_` (`branch_id`);

--
-- Indexes for table `base_app_designation`
--
ALTER TABLE `base_app_designation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_designation_branch_id_1fc335cd_fk_base_app_` (`branch_id`),
  ADD KEY `base_app_designation_department_id_ea1e17c4_fk_base_app_` (`department_id`);

--
-- Indexes for table `base_app_extracurricular`
--
ALTER TABLE `base_app_extracurricular`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_extracurric_user_id_75f4c404_fk_base_app_` (`user_id`);

--
-- Indexes for table `base_app_internship`
--
ALTER TABLE `base_app_internship`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_internship_internshiptype_id_6b231174_fk_base_app_` (`internshiptype_id`),
  ADD KEY `base_app_internship_branch_id_8aeb0fa1_fk_base_app_` (`branch_id`);

--
-- Indexes for table `base_app_internship_paydata`
--
ALTER TABLE `base_app_internship_paydata`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_internship__internship_user_id_dc53692c_fk_base_app_` (`internship_user_id`);

--
-- Indexes for table `base_app_internship_type`
--
ALTER TABLE `base_app_internship_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `base_app_leave`
--
ALTER TABLE `base_app_leave`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_leave_user_id_864afd43_fk_base_app_user_registration_id` (`user_id`);

--
-- Indexes for table `base_app_paymentlist`
--
ALTER TABLE `base_app_paymentlist`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_paymentlist_course_id_8d28f5e6_fk_base_app_course_id` (`course_id`),
  ADD KEY `base_app_paymentlist_user_id_id_671cce29_fk_base_app_` (`user_id_id`);

--
-- Indexes for table `base_app_previousteam`
--
ALTER TABLE `base_app_previousteam`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_previoustea_teamname_id_3ab1c981_fk_base_app_` (`teamname_id`),
  ADD KEY `base_app_previoustea_user_id_0472f3fa_fk_base_app_` (`user_id`);

--
-- Indexes for table `base_app_probation`
--
ALTER TABLE `base_app_probation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_probation_team_id_bf88d429_fk_base_app_create_team_id` (`team_id`),
  ADD KEY `base_app_probation_trainer_id_c446d47f_fk_base_app_` (`trainer_id`),
  ADD KEY `base_app_probation_user_id_12a4bd49_fk_base_app_` (`user_id`);

--
-- Indexes for table `base_app_project`
--
ALTER TABLE `base_app_project`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_project_projectmanager_id_25eb49b5_fk_base_app_` (`projectmanager_id`),
  ADD KEY `base_app_project_tester_id_681675aa_fk_base_app_` (`tester_id`),
  ADD KEY `base_app_project_branch_id_f9216934_fk_base_app_` (`branch_id`),
  ADD KEY `base_app_project_department_id_ab5a9426_fk_base_app_` (`department_id`),
  ADD KEY `base_app_project_designation_id_b5dff45f_fk_base_app_` (`designation_id`);

--
-- Indexes for table `base_app_project_module_assign`
--
ALTER TABLE `base_app_project_module_assign`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_project_mod_project_name_id_709b008e_fk_base_app_` (`project_name_id`);

--
-- Indexes for table `base_app_project_table`
--
ALTER TABLE `base_app_project_table`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_project_tab_project_id_6c094011_fk_base_app_` (`project_id`);

--
-- Indexes for table `base_app_project_taskassign`
--
ALTER TABLE `base_app_project_taskassign`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_project_tas_developer_id_edc30710_fk_base_app_` (`developer_id`),
  ADD KEY `base_app_project_tas_project_id_11045022_fk_base_app_` (`project_id`),
  ADD KEY `base_app_project_tas_tester_id_7758f59d_fk_base_app_` (`tester_id`),
  ADD KEY `base_app_project_tas_tl_id_7d2cff4b_fk_base_app_` (`tl_id`);

--
-- Indexes for table `base_app_promissory`
--
ALTER TABLE `base_app_promissory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_promissory_user_id_id_ba5996db_fk_base_app_` (`user_id_id`);

--
-- Indexes for table `base_app_qualification`
--
ALTER TABLE `base_app_qualification`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_qualificati_user_id_28baad2d_fk_base_app_` (`user_id`);

--
-- Indexes for table `base_app_reported_issue`
--
ALTER TABLE `base_app_reported_issue`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_reported_is_reported_to_id_071dd663_fk_base_app_` (`reported_to_id`),
  ADD KEY `base_app_reported_is_reporter_id_ecf00692_fk_base_app_` (`reporter_id`);

--
-- Indexes for table `base_app_tasks`
--
ALTER TABLE `base_app_tasks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_tasks_department_id_2002c7b1_fk_base_app_department_id` (`department_id`),
  ADD KEY `base_app_tasks_designation_id_5a0cbfdc_fk_base_app_` (`designation_id`),
  ADD KEY `base_app_tasks_user_id_727f88c7_fk_base_app_user_registration_id` (`user_id`);

--
-- Indexes for table `base_app_tester_status`
--
ALTER TABLE `base_app_tester_status`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_tester_stat_project_id_95868a63_fk_base_app_` (`project_id`),
  ADD KEY `base_app_tester_stat_subtask_id_c145ec1d_fk_base_app_` (`subtask_id`),
  ADD KEY `base_app_tester_stat_task_id_4e683dd3_fk_base_app_` (`task_id`),
  ADD KEY `base_app_tester_stat_tester_id_da5cd3da_fk_base_app_` (`tester_id`),
  ADD KEY `base_app_tester_stat_user_id_c8214431_fk_base_app_` (`user_id`);

--
-- Indexes for table `base_app_test_status`
--
ALTER TABLE `base_app_test_status`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_test_status_project_id_8790b454_fk_base_app_project_id` (`project_id`),
  ADD KEY `base_app_test_status_subtask_id_f2f2d90f_fk_base_app_` (`subtask_id`),
  ADD KEY `base_app_test_status_taskname_id_6f61b503_fk_base_app_` (`taskname_id`),
  ADD KEY `base_app_test_status_user_id_84ffa638_fk_base_app_` (`user_id`);

--
-- Indexes for table `base_app_topic`
--
ALTER TABLE `base_app_topic`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_topic_team_id_a0c5e7a1_fk_base_app_create_team_id` (`team_id`),
  ADD KEY `base_app_topic_trainee_id_1cdbdb38_fk_base_app_` (`trainee_id`),
  ADD KEY `base_app_topic_trainer_id_eb6a13e5_fk_base_app_` (`trainer_id`);

--
-- Indexes for table `base_app_trainer_task`
--
ALTER TABLE `base_app_trainer_task`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_trainer_tas_team_name_id_d201e56b_fk_base_app_` (`team_name_id`),
  ADD KEY `base_app_trainer_tas_user_id_d13a5c2d_fk_base_app_` (`user_id`);

--
-- Indexes for table `base_app_user_registration`
--
ALTER TABLE `base_app_user_registration`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_app_user_regist_branch_id_14a07e3d_fk_base_app_` (`branch_id`),
  ADD KEY `base_app_user_regist_course_id_5a1e7dc3_fk_base_app_` (`course_id`),
  ADD KEY `base_app_user_regist_department_id_f8ffba2f_fk_base_app_` (`department_id`),
  ADD KEY `base_app_user_regist_designation_id_1a35907e_fk_base_app_` (`designation_id`),
  ADD KEY `base_app_user_regist_team_id_82d71bbf_fk_base_app_` (`team_id`);

--
-- Indexes for table `cal_event`
--
ALTER TABLE `cal_event`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=161;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_app_acntexpensest`
--
ALTER TABLE `base_app_acntexpensest`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `base_app_acntspayslip`
--
ALTER TABLE `base_app_acntspayslip`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `base_app_acnt_monthdays`
--
ALTER TABLE `base_app_acnt_monthdays`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `base_app_attendance`
--
ALTER TABLE `base_app_attendance`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `base_app_branch_registration`
--
ALTER TABLE `base_app_branch_registration`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `base_app_conditions`
--
ALTER TABLE `base_app_conditions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `base_app_course`
--
ALTER TABLE `base_app_course`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `base_app_create_team`
--
ALTER TABLE `base_app_create_team`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `base_app_department`
--
ALTER TABLE `base_app_department`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `base_app_designation`
--
ALTER TABLE `base_app_designation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `base_app_extracurricular`
--
ALTER TABLE `base_app_extracurricular`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `base_app_internship`
--
ALTER TABLE `base_app_internship`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `base_app_internship_paydata`
--
ALTER TABLE `base_app_internship_paydata`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `base_app_internship_type`
--
ALTER TABLE `base_app_internship_type`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `base_app_leave`
--
ALTER TABLE `base_app_leave`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `base_app_paymentlist`
--
ALTER TABLE `base_app_paymentlist`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `base_app_previousteam`
--
ALTER TABLE `base_app_previousteam`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `base_app_probation`
--
ALTER TABLE `base_app_probation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `base_app_project`
--
ALTER TABLE `base_app_project`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `base_app_project_module_assign`
--
ALTER TABLE `base_app_project_module_assign`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `base_app_project_table`
--
ALTER TABLE `base_app_project_table`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `base_app_project_taskassign`
--
ALTER TABLE `base_app_project_taskassign`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `base_app_promissory`
--
ALTER TABLE `base_app_promissory`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_app_qualification`
--
ALTER TABLE `base_app_qualification`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_app_reported_issue`
--
ALTER TABLE `base_app_reported_issue`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `base_app_tasks`
--
ALTER TABLE `base_app_tasks`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_app_tester_status`
--
ALTER TABLE `base_app_tester_status`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_app_test_status`
--
ALTER TABLE `base_app_test_status`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `base_app_topic`
--
ALTER TABLE `base_app_topic`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_app_trainer_task`
--
ALTER TABLE `base_app_trainer_task`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `base_app_user_registration`
--
ALTER TABLE `base_app_user_registration`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `cal_event`
--
ALTER TABLE `cal_event`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `base_app_acntspayslip`
--
ALTER TABLE `base_app_acntspayslip`
  ADD CONSTRAINT `base_app_acntspaysli_department_id_21ada824_fk_base_app_` FOREIGN KEY (`department_id`) REFERENCES `base_app_department` (`id`),
  ADD CONSTRAINT `base_app_acntspaysli_designation_id_00bcb706_fk_base_app_` FOREIGN KEY (`designation_id`) REFERENCES `base_app_designation` (`id`),
  ADD CONSTRAINT `base_app_acntspaysli_user_id_id_fce5649e_fk_base_app_` FOREIGN KEY (`user_id_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_attendance`
--
ALTER TABLE `base_app_attendance`
  ADD CONSTRAINT `base_app_attendance_user_id_430c8040_fk_base_app_` FOREIGN KEY (`user_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_department`
--
ALTER TABLE `base_app_department`
  ADD CONSTRAINT `base_app_department_branch_id_eabcf909_fk_base_app_` FOREIGN KEY (`branch_id`) REFERENCES `base_app_branch_registration` (`id`);

--
-- Constraints for table `base_app_designation`
--
ALTER TABLE `base_app_designation`
  ADD CONSTRAINT `base_app_designation_branch_id_1fc335cd_fk_base_app_` FOREIGN KEY (`branch_id`) REFERENCES `base_app_branch_registration` (`id`),
  ADD CONSTRAINT `base_app_designation_department_id_ea1e17c4_fk_base_app_` FOREIGN KEY (`department_id`) REFERENCES `base_app_department` (`id`);

--
-- Constraints for table `base_app_extracurricular`
--
ALTER TABLE `base_app_extracurricular`
  ADD CONSTRAINT `base_app_extracurric_user_id_75f4c404_fk_base_app_` FOREIGN KEY (`user_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_internship`
--
ALTER TABLE `base_app_internship`
  ADD CONSTRAINT `base_app_internship_branch_id_8aeb0fa1_fk_base_app_` FOREIGN KEY (`branch_id`) REFERENCES `base_app_branch_registration` (`id`),
  ADD CONSTRAINT `base_app_internship_internshiptype_id_6b231174_fk_base_app_` FOREIGN KEY (`internshiptype_id`) REFERENCES `base_app_internship_type` (`id`);

--
-- Constraints for table `base_app_internship_paydata`
--
ALTER TABLE `base_app_internship_paydata`
  ADD CONSTRAINT `base_app_internship__internship_user_id_dc53692c_fk_base_app_` FOREIGN KEY (`internship_user_id`) REFERENCES `base_app_internship` (`id`);

--
-- Constraints for table `base_app_leave`
--
ALTER TABLE `base_app_leave`
  ADD CONSTRAINT `base_app_leave_user_id_864afd43_fk_base_app_user_registration_id` FOREIGN KEY (`user_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_paymentlist`
--
ALTER TABLE `base_app_paymentlist`
  ADD CONSTRAINT `base_app_paymentlist_course_id_8d28f5e6_fk_base_app_course_id` FOREIGN KEY (`course_id`) REFERENCES `base_app_course` (`id`),
  ADD CONSTRAINT `base_app_paymentlist_user_id_id_671cce29_fk_base_app_` FOREIGN KEY (`user_id_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_previousteam`
--
ALTER TABLE `base_app_previousteam`
  ADD CONSTRAINT `base_app_previoustea_teamname_id_3ab1c981_fk_base_app_` FOREIGN KEY (`teamname_id`) REFERENCES `base_app_create_team` (`id`),
  ADD CONSTRAINT `base_app_previoustea_user_id_0472f3fa_fk_base_app_` FOREIGN KEY (`user_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_probation`
--
ALTER TABLE `base_app_probation`
  ADD CONSTRAINT `base_app_probation_team_id_bf88d429_fk_base_app_create_team_id` FOREIGN KEY (`team_id`) REFERENCES `base_app_create_team` (`id`),
  ADD CONSTRAINT `base_app_probation_trainer_id_c446d47f_fk_base_app_` FOREIGN KEY (`trainer_id`) REFERENCES `base_app_user_registration` (`id`),
  ADD CONSTRAINT `base_app_probation_user_id_12a4bd49_fk_base_app_` FOREIGN KEY (`user_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_project`
--
ALTER TABLE `base_app_project`
  ADD CONSTRAINT `base_app_project_branch_id_f9216934_fk_base_app_` FOREIGN KEY (`branch_id`) REFERENCES `base_app_branch_registration` (`id`),
  ADD CONSTRAINT `base_app_project_department_id_ab5a9426_fk_base_app_` FOREIGN KEY (`department_id`) REFERENCES `base_app_department` (`id`),
  ADD CONSTRAINT `base_app_project_designation_id_b5dff45f_fk_base_app_` FOREIGN KEY (`designation_id`) REFERENCES `base_app_designation` (`id`),
  ADD CONSTRAINT `base_app_project_projectmanager_id_25eb49b5_fk_base_app_` FOREIGN KEY (`projectmanager_id`) REFERENCES `base_app_user_registration` (`id`),
  ADD CONSTRAINT `base_app_project_tester_id_681675aa_fk_base_app_` FOREIGN KEY (`tester_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_project_module_assign`
--
ALTER TABLE `base_app_project_module_assign`
  ADD CONSTRAINT `base_app_project_mod_project_name_id_709b008e_fk_base_app_` FOREIGN KEY (`project_name_id`) REFERENCES `base_app_project` (`id`);

--
-- Constraints for table `base_app_project_table`
--
ALTER TABLE `base_app_project_table`
  ADD CONSTRAINT `base_app_project_tab_project_id_6c094011_fk_base_app_` FOREIGN KEY (`project_id`) REFERENCES `base_app_project` (`id`);

--
-- Constraints for table `base_app_project_taskassign`
--
ALTER TABLE `base_app_project_taskassign`
  ADD CONSTRAINT `base_app_project_tas_developer_id_edc30710_fk_base_app_` FOREIGN KEY (`developer_id`) REFERENCES `base_app_user_registration` (`id`),
  ADD CONSTRAINT `base_app_project_tas_project_id_11045022_fk_base_app_` FOREIGN KEY (`project_id`) REFERENCES `base_app_project` (`id`),
  ADD CONSTRAINT `base_app_project_tas_tester_id_7758f59d_fk_base_app_` FOREIGN KEY (`tester_id`) REFERENCES `base_app_user_registration` (`id`),
  ADD CONSTRAINT `base_app_project_tas_tl_id_7d2cff4b_fk_base_app_` FOREIGN KEY (`tl_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_promissory`
--
ALTER TABLE `base_app_promissory`
  ADD CONSTRAINT `base_app_promissory_user_id_id_ba5996db_fk_base_app_` FOREIGN KEY (`user_id_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_qualification`
--
ALTER TABLE `base_app_qualification`
  ADD CONSTRAINT `base_app_qualificati_user_id_28baad2d_fk_base_app_` FOREIGN KEY (`user_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_reported_issue`
--
ALTER TABLE `base_app_reported_issue`
  ADD CONSTRAINT `base_app_reported_is_reported_to_id_071dd663_fk_base_app_` FOREIGN KEY (`reported_to_id`) REFERENCES `base_app_user_registration` (`id`),
  ADD CONSTRAINT `base_app_reported_is_reporter_id_ecf00692_fk_base_app_` FOREIGN KEY (`reporter_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_tasks`
--
ALTER TABLE `base_app_tasks`
  ADD CONSTRAINT `base_app_tasks_department_id_2002c7b1_fk_base_app_department_id` FOREIGN KEY (`department_id`) REFERENCES `base_app_department` (`id`),
  ADD CONSTRAINT `base_app_tasks_designation_id_5a0cbfdc_fk_base_app_` FOREIGN KEY (`designation_id`) REFERENCES `base_app_designation` (`id`),
  ADD CONSTRAINT `base_app_tasks_user_id_727f88c7_fk_base_app_user_registration_id` FOREIGN KEY (`user_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_tester_status`
--
ALTER TABLE `base_app_tester_status`
  ADD CONSTRAINT `base_app_tester_stat_project_id_95868a63_fk_base_app_` FOREIGN KEY (`project_id`) REFERENCES `base_app_project` (`id`),
  ADD CONSTRAINT `base_app_tester_stat_subtask_id_c145ec1d_fk_base_app_` FOREIGN KEY (`subtask_id`) REFERENCES `base_app_project_taskassign` (`id`),
  ADD CONSTRAINT `base_app_tester_stat_task_id_4e683dd3_fk_base_app_` FOREIGN KEY (`task_id`) REFERENCES `base_app_project_taskassign` (`id`),
  ADD CONSTRAINT `base_app_tester_stat_tester_id_da5cd3da_fk_base_app_` FOREIGN KEY (`tester_id`) REFERENCES `base_app_user_registration` (`id`),
  ADD CONSTRAINT `base_app_tester_stat_user_id_c8214431_fk_base_app_` FOREIGN KEY (`user_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_test_status`
--
ALTER TABLE `base_app_test_status`
  ADD CONSTRAINT `base_app_test_status_project_id_8790b454_fk_base_app_project_id` FOREIGN KEY (`project_id`) REFERENCES `base_app_project` (`id`),
  ADD CONSTRAINT `base_app_test_status_subtask_id_f2f2d90f_fk_base_app_` FOREIGN KEY (`subtask_id`) REFERENCES `base_app_project_taskassign` (`id`),
  ADD CONSTRAINT `base_app_test_status_taskname_id_6f61b503_fk_base_app_` FOREIGN KEY (`taskname_id`) REFERENCES `base_app_user_registration` (`id`),
  ADD CONSTRAINT `base_app_test_status_user_id_84ffa638_fk_base_app_` FOREIGN KEY (`user_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_topic`
--
ALTER TABLE `base_app_topic`
  ADD CONSTRAINT `base_app_topic_team_id_a0c5e7a1_fk_base_app_create_team_id` FOREIGN KEY (`team_id`) REFERENCES `base_app_create_team` (`id`),
  ADD CONSTRAINT `base_app_topic_trainee_id_1cdbdb38_fk_base_app_` FOREIGN KEY (`trainee_id`) REFERENCES `base_app_user_registration` (`id`),
  ADD CONSTRAINT `base_app_topic_trainer_id_eb6a13e5_fk_base_app_` FOREIGN KEY (`trainer_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_trainer_task`
--
ALTER TABLE `base_app_trainer_task`
  ADD CONSTRAINT `base_app_trainer_tas_team_name_id_d201e56b_fk_base_app_` FOREIGN KEY (`team_name_id`) REFERENCES `base_app_create_team` (`id`),
  ADD CONSTRAINT `base_app_trainer_tas_user_id_d13a5c2d_fk_base_app_` FOREIGN KEY (`user_id`) REFERENCES `base_app_user_registration` (`id`);

--
-- Constraints for table `base_app_user_registration`
--
ALTER TABLE `base_app_user_registration`
  ADD CONSTRAINT `base_app_user_regist_branch_id_14a07e3d_fk_base_app_` FOREIGN KEY (`branch_id`) REFERENCES `base_app_branch_registration` (`id`),
  ADD CONSTRAINT `base_app_user_regist_course_id_5a1e7dc3_fk_base_app_` FOREIGN KEY (`course_id`) REFERENCES `base_app_course` (`id`),
  ADD CONSTRAINT `base_app_user_regist_department_id_f8ffba2f_fk_base_app_` FOREIGN KEY (`department_id`) REFERENCES `base_app_department` (`id`),
  ADD CONSTRAINT `base_app_user_regist_designation_id_1a35907e_fk_base_app_` FOREIGN KEY (`designation_id`) REFERENCES `base_app_designation` (`id`),
  ADD CONSTRAINT `base_app_user_regist_team_id_82d71bbf_fk_base_app_` FOREIGN KEY (`team_id`) REFERENCES `base_app_create_team` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
