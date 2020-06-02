CREATE DATABASE [CMS4]
USE [CMS4]

CREATE TABLE [User]
(
	Username VARCHAR(50) PRIMARY KEY,
	[Name] VARCHAR(50),
	Email VARCHAR(50),
	[Password] VARCHAR(200)
);


CREATE TABLE [UserType]
(
	[Type] VARCHAR(50) PRIMARY KEY
);


CREATE TABLE Deadline
(
	DeadlineID INT IDENTITY(1,1) PRIMARY KEY,
	ProposalDeadline DATE,
	AbstractDeadline DATE
);

CREATE TABLE [Event]
(
	EventID INT IDENTITY(1,1) PRIMARY KEY,
	[Name] VARCHAR(50),
	Interval VARCHAR(50),
	DeadlineID INT UNIQUE FOREIGN KEY REFERENCES Deadline(DeadlineID)
);

CREATE TABLE Participates
(
	Username VARCHAR(50) FOREIGN KEY REFERENCES [User](Username),
	EventID INT FOREIGN KEY REFERENCES Event(EventID),
	[Type] VARCHAR(50) FOREIGN KEY REFERENCES UserType([Type]),
	PRIMARY KEY(Username,EventID,[Type])
);


CREATE TABLE Abstract
(
	AbstractID INT IDENTITY(1,1) PRIMARY KEY ,
	Title VARCHAR(50),
	[Name] VARCHAR(50), 
	Purpose VARCHAR(100),
	Methods VARCHAR(100)
);



CREATE TABLE Paper
(
	PaperID INT IDENTITY(1,1) PRIMARY KEY,
	PaperInfo Varchar(500),
	
);


CREATE TABLE Proposal
(
	ProposalID INT IDENTITY(1,1) PRIMARY KEY,
	AbstractID INT UNIQUE FOREIGN KEY REFERENCES Abstract(AbstractID),
	PaperID INT UNIQUE FOREIGN KEY REFERENCES Paper(PaperID),
	EventId INT  FOREIGN KEY REFERENCES [Event](EventID),
	

	[Name] VARCHAR(50),
	Keyword VARCHAR(50),
	Topic VARCHAR(50),
	Metainfo VARCHAR(50),
	[Status] BIT

);

CREATE TABLE Author
(
	Username VARCHAR(50) FOREIGN KEY REFERENCES [User](Username),
	ProposalID INT FOREIGN KEY REFERENCES Proposal(ProposalID),
	PRIMARY KEY(Username, ProposalID)
);

CREATE TABLE [PCAnalyze]
(
	[Type] VARCHAR(50) PRIMARY KEY
);

/*  each PC member: brief analyze of abstracts or papers in order to say:

		- pleased to review 

		- could evaluate

		- refuse to evaluate*/
CREATE TABLE PCmember
(
	Username VARCHAR(50) FOREIGN KEY REFERENCES [User](Username),
	ProposalID INT FOREIGN KEY REFERENCES Proposal(ProposalID),
	Analyze  VARCHAR(50) FOREIGN KEY REFERENCES PCAnalyze([Type]),
	PRIMARY KEY(Username,ProposalID)
);



CREATE TABLE [PaperResult]
(
	[Type] VARCHAR(50) PRIMARY KEY
);

CREATE TABLE Reviewer
(
	Username VARCHAR(50) FOREIGN KEY REFERENCES [User](Username),
	ProposalID INT FOREIGN KEY REFERENCES Proposal(ProposalID),
	Result VARCHAR(50) FOREIGN KEY REFERENCES PaperResult([Type]),
	Recommendation VARCHAR(200),
	PRIMARY KEY(Username,ProposalID)

);

CREATE TABLE Section
(
	SectionID INT IDENTITY(1,1) PRIMARY KEY,
	EventID INT FOREIGN KEY REFERENCES Event(EventID),
	[Name] VARCHAR(50)
);

/*
Here speakers upload their presentations
*/

CREATE TABLE PresentationContent
(
	ContentID INT IDENTITY(1,1) PRIMARY KEY,
	SectionID INT FOREIGN KEY REFERENCES Section(SectionID),
	Username VARCHAR(50) FOREIGN KEY REFERENCES [User](Username),
	Content VARCHAR(500)
)

CREATE TABLE SectionParticipates
(
	Username VARCHAR(50) FOREIGN KEY REFERENCES [User](Username),
	SectionID INT FOREIGN KEY REFERENCES Section(SectionID),
	[Type] VARCHAR(50) FOREIGN KEY REFERENCES UserType([Type]),
	PRIMARY KEY(Username,SectionID,[Type])
);

INSERT INTO UserType([Type])
VALUES
    ('PCmember'),
    ('chair'),
	('co_chair'),
	('author'),
	('speaker'),
	('listener'),
	('sesion_chair'),
	('reviewer')

INSERT INTO [PCAnalyze]([Type])
VALUES
    ('pleased_eval'),
    ('could_eval'),
	('refuse_eval')

INSERT INTO [PaperResult]([Type])
VALUES
    ('strong_accept'),
    ('accept'),
	('borderline'),
	('weak_reject'),
	('reject'),
	('strong_reject')







