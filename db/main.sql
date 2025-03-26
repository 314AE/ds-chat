/*
 Navicat Premium Dump SQL

 Source Server         : demo_one
 Source Server Type    : SQLite
 Source Server Version : 3045000 (3.45.0)
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3045000 (3.45.0)
 File Encoding         : 65001

 Date: 05/03/2025 02:36:02
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for ai_chat_info
-- ----------------------------
DROP TABLE IF EXISTS "ai_chat_info";
CREATE TABLE "ai_chat_info" (
  "id" integer NOT NULL,
  "problem_info" TEXT,
  "res_info" TEXT,
  "create_time" t,
  PRIMARY KEY ("id")
);

-- ----------------------------
-- Table structure for res_record
-- ----------------------------
DROP TABLE IF EXISTS "res_record";
CREATE TABLE "res_record" (
  "id" INTEGER NOT NULL,
  "status_code" TEXT,
  "headers" TEXT,
  "res_text" TEXT,
  "create_time" text,
  PRIMARY KEY ("id")
);

PRAGMA foreign_keys = true;
