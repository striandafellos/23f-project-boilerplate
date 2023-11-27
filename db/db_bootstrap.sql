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
CREATE TABLE IF NOT EXISTS User (
  UserID int NOT NULL AUTO_INCREMENT,
  Username varchar(255) NOT NULL,
  PRIMARY KEY (UserID)
);

-- Folder table
CREATE TABLE IF NOT EXISTS Folder (
  FolderID int NOT NULL AUTO_INCREMENT,
  FolderName varchar(255),
  UserID int NOT NULL,
  PRIMARY KEY (FolderID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
    ON DELETE CASCADE
);

-- Job Application table
CREATE TABLE IF NOT EXISTS JobApplication (
  ApplicationID int NOT NULL AUTO_INCREMENT,
  JobTitle varchar(255),
  CompanyName varchar(255),
  Content text,
  UserID int NOT NULL,
  FolderID int NOT NULL,
  PRIMARY KEY (ApplicationID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
    ON DELETE CASCADE,
  FOREIGN KEY (FolderID) REFERENCES Folder(FolderID)
    ON DELETE CASCADE
);

-- Basic Document table
CREATE TABLE IF NOT EXISTS Document (
  DocumentID int NOT NULL AUTO_INCREMENT,
  DocumentName varchar(255),
  Content text,
  UserID int NOT NULL,
  FolderID int NOT NULL,
  PRIMARY KEY (DocumentID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
    ON DELETE CASCADE,
  FOREIGN KEY (FolderID) REFERENCES Folder(FolderID)
    ON DELETE CASCADE
);

-- Message table
CREATE TABLE IF NOT EXISTS Message (
  MessageID int NOT NULL AUTO_INCREMENT,
  SenderID int NOT NULL,
  RecipientID int NOT NULL,
  MessageBody text NOT NULL,
  DateSent datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (MessageID),
  FOREIGN KEY (SenderID) REFERENCES User(UserID),
  FOREIGN KEY (RecipientID) REFERENCES User(UserID)
);

-- UserGroup table
CREATE TABLE IF NOT EXISTS UserGroup (
  GroupID int NOT NULL AUTO_INCREMENT,
  GroupName varchar(255),
  PRIMARY KEY (GroupID)
);

-- GroupsAndUsers table
-- Slightly convoluted naming to reduce issues with using reserved words ('group') as table names
CREATE TABLE IF NOT EXISTS GroupsAndUsers (
  UserID int NOT NULL,
  GroupID int NOT NULL,
  PRIMARY KEY (UserID, GroupID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
    ON DELETE CASCADE,
  FOREIGN KEY (GroupID) REFERENCES UserGroup(GroupID)
    ON DELETE CASCADE
);

-- Planner table
CREATE TABLE IF NOT EXISTS Planner (
  PlannerID int NOT NULL AUTO_INCREMENT,
  PlannerName varchar(255),
  UserID int NOT NULL,
  PRIMARY KEY (PlannerID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
    ON DELETE CASCADE
);

-- Calendar table
CREATE TABLE IF NOT EXISTS Calendar (
  CalendarID int NOT NULL AUTO_INCREMENT,
  CalendarName varchar(255),
  UserID int NOT NULL,
  PRIMARY KEY (CalendarID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
    ON DELETE CASCADE
);

-- Task table
CREATE TABLE IF NOT EXISTS Task (
  TaskID int NOT NULL AUTO_INCREMENT,
  Title varchar(255),
  TaskDescription text,
  DueDate datetime NOT NULL,
  Completed boolean NOT NULL DEFAULT FALSE,
  UserID int NOT NULL,
  PlannerID int,
  CalendarID int,
  PRIMARY KEY (TaskID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
    ON DELETE CASCADE,
  FOREIGN KEY (PlannerID) REFERENCES Planner(PlannerID)
    ON DELETE CASCADE,
  FOREIGN KEY (CalendarID) REFERENCES Calendar(CalendarID)
    ON DELETE CASCADE
);

-- Event table
CREATE TABLE IF NOT EXISTS Event (
  EventID int NOT NULL AUTO_INCREMENT,
  Title varchar(255),
  Details text,
  EventDate datetime NOT NULL,
  UserID int NOT NULL,
  PlannerID int,
  CalendarID int,
  PRIMARY KEY (EventID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
    ON DELETE CASCADE,
  FOREIGN KEY (PlannerID) REFERENCES Planner(PlannerID)
    ON DELETE CASCADE,
  FOREIGN KEY (CalendarID) REFERENCES Calendar(CalendarID)
    ON DELETE CASCADE
);

-- Class table
CREATE TABLE IF NOT EXISTS Class (
  ClassID int NOT NULL AUTO_INCREMENT,
  Title varchar(255),
  PRIMARY KEY (ClassID)
);

-- ClassAndUser table
CREATE TABLE IF NOT EXISTS ClassAndUser (
  UserID int NOT NULL,
  ClassID int NOT NULL,
  PRIMARY KEY (UserID, ClassID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
    ON DELETE CASCADE,
  FOREIGN KEY (ClassID) REFERENCES Class(ClassID)
    ON DELETE CASCADE
);

-- Budget Tracker table
CREATE TABLE IF NOT EXISTS BudgetTracker (
  BudgetTrackerID int NOT NULL AUTO_INCREMENT,
  BudgetTrackerName varchar(255),
  UserID int NOT NULL,
  PRIMARY KEY (BudgetTrackerID),
  FOREIGN KEY (UserID) REFERENCES User(UserID)
    ON DELETE CASCADE
);

-- BudgetItem table
CREATE TABLE IF NOT EXISTS BudgetItem (
  BudgetItemID int NOT NULL AUTO_INCREMENT,
  ItemName varchar(255),
  ItemDescription text,
  ItemAmount decimal(10,2) NOT NULL,
  BudgetTrackerID int NOT NULL,
  PRIMARY KEY (BudgetItemID),
  FOREIGN KEY (BudgetTrackerID) REFERENCES BudgetTracker(BudgetTrackerID)
    ON DELETE CASCADE
);


-- Add sample data. 

-- User sample data
INSERT INTO User
  (Username)
VALUES
  ('testuser1'),
  ('testuser2'),
  ('testuser3');

-- Folder sample data
INSERT INTO Folder
  (FolderName, UserID)
VALUES
  ('Folder 1', 1),
  ('Folder 2', 1),
  ('Folder 3', 2),
  ('Folder 4', 2),
  ('Folder 5', 3),
  ('Folder 6', 3);

-- Job Application sample data
INSERT INTO JobApplication
  (JobTitle, CompanyName, Content, UserID, FolderID)
VALUES
  ('Job 1', 'Company 1', 'Content related to job 1', 1, 1),
  (NULL, 'Company 2', 'More information', 2, 3),
  (NULL, NULL, NULL, 3, 6);

-- Document sample data
INSERT INTO Document
  (DocumentName, Content, UserID, FolderID)
VALUES
  ('Document 1', 'Content related to document 1', 1, 1),
  ('Document 2', 'Document 2 content', 1, 1),
  (NULL, 'words words words', 3, 5),
  (NULL, NULL, 2, 3);

-- Message sample data
INSERT INTO Message
  (SenderID, RecipientID, MessageBody)
VALUES
  (1, 2, 'Message 1'),
  (2, 1, 'Message 2'),
  (3, 1, 'Message 3'),
  (1, 3, 'Message 4'),
  (2, 3, 'Message 5'),
  (3, 2, 'Message 6');

-- UserGroup sample data
INSERT INTO UserGroup
  (GroupName)
VALUES
  ('Group 1'),
  ('Group 2'),
  ('Group 3');

-- GroupsAndUsers sample data
INSERT INTO GroupsAndUsers
  (UserID, GroupID)
VALUES
  (1, 1),
  (1, 2),
  (1, 3),
  (3, 2),
  (3, 3);

-- Planner sample data
INSERT INTO Planner
  (PlannerName, UserID)
VALUES
  ('Planner 1', 1),
  ('Planner 2', 1),
  ('Planner 3', 2),
  (NULL, 3);

-- Calendar sample data
INSERT INTO Calendar
  (CalendarName, UserID)
VALUES
  ('Calendar 1', 2),
  ('Calendar 2', 3),
  ('Calendar 3', 2),
  (NULL, 1);

-- Task sample data
INSERT INTO Task
  (Title, TaskDescription, DueDate, Completed, UserID, PlannerID, CalendarID)
VALUES
  ('Task 1', 'Task 1 description', '2023-11-28 00:00:00', 0, 2, 3, NULL),
  ('Task 2', 'Task 2 description', '2023-12-25 13:13:13', 1, 1, NULL, 4),
  (NULL, NULL, '2023-12-11 01:32:54', 0, 1, NULL, NULL);

-- Event sample data
INSERT INTO Event
  (Title, Details, EventDate, UserID, PlannerID, CalendarID)
VALUES
  ('Event 1', 'Event 1 details', '2023-11-29 19:00:00', 1, 1, NULL),
  ('Event 2', 'Event 2 details', '2027-03-12 08:33:12', 2, NULL, 1),
  (NULL, NULL, CURRENT_TIMESTAMP, 3, NULL, NULL);

-- Class sample data
INSERT INTO Class
  (Title)
VALUES
  ('Class 1'),
  ('Class 2'),
  ('Class 3'),
  ('Class 4');

-- ClassAndUser sample data
INSERT INTO ClassAndUser
  (UserID, ClassID)
VALUES
  (1, 1),
  (1, 2),
  (1, 3),
  (1, 4),
  (2, 1),
  (2, 3),
  (3, 2),
  (3, 3),
  (3, 4);

-- BudgetTracker sample data
INSERT INTO BudgetTracker
  (BudgetTrackerName, UserID)
VALUES
  ('Budget Tracker 1', 1),
  ('Budget Tracker 2', 2),
  ('Budget Tracker 3', 3),
  (NULL, 3);

-- BudgetItem sample data
INSERT INTO BudgetItem
  (ItemName, ItemDescription, ItemAmount, BudgetTrackerID)
VALUES
  ('Item 1', 'Description for item 1', 25.99, 1),
  ('Item 2', 'Uh oh this one is negative it better not break the system', -47.88, 2),
  (NULL, NULL, 100.00, 1);