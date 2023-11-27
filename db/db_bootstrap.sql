-- This file is to bootstrap a database for the CS3200 project. 

-- Create a new database.  You can change the name later.  You'll
-- need this name in the FLASK API file(s),  the AppSmith 
-- data source creation.
create database taskwiz_db;

-- Via the Docker Compose file, a special user called webapp will 
-- be created in MySQL. We are going to grant that user 
-- all privilages to the new database we just created. 
-- TODO: If you changed the name of the database above, you need 
-- to change it here too.
grant all privileges on taskwiz_db.* to 'webapp'@'%';
flush privileges;

-- Move into the database we just created.
-- TODO: If you changed the name of the database above, you need to
-- change it here too. 
use taskwiz_db;

-- Put your DDL

-- User table
CREATE TABLE User (
  UserID int NOT NULL AUTO_INCREMENT,
  Username varchar(255) NOT NULL,
  PRIMARY KEY (UserID)
);

-- Folder table
CREATE TABLE Folder (
  FolderID int NOT NULL AUTO_INCREMENT,
  FolderName varchar(255),
  UserID int NOT NULL,
  PRIMARY KEY (FolderID),
  CONSTRAINT creator_fk FOREIGN KEY (UserID) REFERENCES User(UserID)
);

-- Job Application table
CREATE TABLE JobApplication (
  ApplicationID int NOT NULL AUTO_INCREMENT,
  JobTitle varchar(255),
  CompanyName varchar(255),
  Content text,
  UserID int NOT NULL,
  FolderID int NOT NULL,
  PRIMARY KEY (JobApplicationID),
  CONSTRAINT creator_fk FOREIGN KEY (UserID) REFERENCES User(UserID),
  CONSTRAINT filelocation_fk FOREIGN KEY (FolderID) REFERENCES Folder(FolderID)
);

-- Basic Document table
CREATE TABLE Document (
  DocumentID int NOT NULL AUTO_INCREMENT,
  DocumentName varchar(255),
  Content text,
  UserID int NOT NULL,
  FolderID int NOT NULL,
  PRIMARY KEY (DocumentID),
  CONSTRAINT creator_fk FOREIGN KEY (UserID) REFERENCES User(UserID),
  CONSTRAINT filelocation_fk FOREIGN KEY (FolderID) REFERENCES Folder(FolderID)
);

-- Message table
CREATE TABLE Message (
  MessageID int NOT NULL AUTO_INCREMENT,
  SenderID int NOT NULL,
  RecipientID int NOT NULL,
  MessageBody text,
  DateSent datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (MessageID),
  CONSTRAINT sender_fk FOREIGN KEY (SenderID) REFERENCES User(UserID),
  CONSTRAINT recipient_fk FOREIGN KEY (RecipientID) REFERENCES User(UserID)
);

-- UserGroup table
CREATE TABLE UserGroup (
  GroupID int NOT NULL AUTO_INCREMENT,
  GroupName varchar(255),
  PRIMARY KEY (GroupID)
);

-- GroupsAndUsers table
-- Slightly convoluted naming to reduce issues with using reserved words ('group') as table names
CREATE TABLE GroupsAndUsers (
  UserID int NOT NULL,
  GroupID int NOT NULL,
  PRIMARY KEY (UserID, GroupID),
  FOREIGN KEY (UserID) REFERENCES User(UserID),
  FOREIGN KEY (GroupID) REFERENCES UserGroup(GroupID)
);

-- Planner table
CREATE TABLE Planner (
  PlannerID int NOT NULL AUTO_INCREMENT,
  PlannerName varchar(255),
  UserID int NOT NULL,
  PRIMARY KEY (PlannerID),
  CONSTRAINT creator_fk FOREIGN KEY (UserID) REFERENCES User(UserID),
);

-- Calendar table
CREATE TABLE Calendar (
  CalendarID int NOT NULL AUTO_INCREMENT,
  CalendarName varchar(255),
  UserID int NOT NULL,
  PRIMARY KEY (CalendarID),
  CONSTRAINT creator_fk FOREIGN KEY (UserID) REFERENCES User(UserID),
);

-- Task table
CREATE TABLE Task (
  TaskID int NOT NULL AUTO_INCREMENT,
  Title varchar(255),
  TaskDescription text,
  DueDate datetime NOT NULL,
  Completed boolean NOT NULL DEFAULT FALSE,
  UserID int NOT NULL,
  PlannerID int,
  CalendarID int,
  PRIMARY KEY (TaskID),
  CONSTRAINT creator_fk FOREIGN KEY (UserID) REFERENCES User(UserID),
  CONSTRAINT planner_fk FOREIGN KEY (PlannerID) REFERENCES Planner(PlannerID),
  CONSTRAINT calendar_fk FOREIGN KEY (CalendarID) REFERENCES Calendar(CalendarID)
);

-- Event table
CREATE TABLE Event (
  EventID int NOT NULL AUTO_INCREMENT,
  Title varchar(255),
  Details text,
  EventDate datetime NOT NULL,
  UserID int NOT NULL,
  PlannerID int,
  CalendarID int,
  PRIMARY KEY (EventID),
  CONSTRAINT creator_fk FOREIGN KEY (UserID) REFERENCES User(UserID),
  CONSTRAINT planner_fk FOREIGN KEY (PlannerID) REFERENCES Planner(PlannerID),
  CONSTRAINT calendar_fk FOREIGN KEY (CalendarID) REFERENCES Calendar(CalendarID)
);

-- Class table
CREATE TABLE Class (
  ClassID int NOT NULL AUTO_INCREMENT,
  Title varchar(255),
  PRIMARY KEY (ClassID)
);

-- ClassAndUser table
CREATE TABLE ClassAndUser (
  UserID int NOT NULL,
  ClassID int NOT NULL,
  PRIMARY KEY (UserID, ClassID),
  CONSTRAINT student_fk FOREIGN KEY (UserID) REFERENCES User(UserID),
  CONSTRAINT class_fk FOREIGN KEY (ClassID) REFERENCES Class(ClassID)
);

-- Budget Tracker table
CREATE TABLE BudgetTracker (
  BudgetTrackerID int NOT NULL AUTO_INCREMENT,
  BudgetTrackerName varchar(255),
  UserID int NOT NULL,
  PRIMARY KEY (BudgetTrackerID),
  CONSTRAINT creator_fk FOREIGN KEY (UserID) REFERENCES User(UserID),
);

-- BudgetItem table
CREATE TABLE BudgetItem (
  BudgetItemID int NOT NULL AUTO_INCREMENT,
  ItemName varchar(255),
  ItemDescription text,
  ItemAmount decimal(10,2) NOT NULL,
  BudgetTrackerID int NOT NULL,
  PRIMARY KEY (BudgetItemID),
  CONSTRAINT tracker_fk FOREIGN KEY (BudgetTrackerID) REFERENCES BudgetTracker(BudgetTrackerID),
);


-- Add sample data. 
INSERT INTO fav_colors
  (name, color)
VALUES
  ('dev', 'blue'),
  ('pro', 'yellow'),
  ('junior', 'red');
