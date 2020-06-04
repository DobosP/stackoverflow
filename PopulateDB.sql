USE [CMS4]
INSERT INTO [User] (Username, [Name], Email, [Password])
VALUES ('Dobo', 'Paul','email@email.com','password'),
	('DeliaO', 'Ostafi','email@email.com','password');

DBCC CHECKIDENT ('[Deadline]', RESEED, 0);
GO
INSERT INTO [Deadline] ([ProposalDeadline], [AbstractDeadline])
VALUES ('2020-01-06', '2020-01-06'),
	('2020-08-06', '2020-10-06');

DBCC CHECKIDENT ('[Event]', RESEED, 0);
GO
INSERT INTO [Event] ([Name], [Interval], [DeadlineID])
VALUES ('Cool Event', '2020-2021',1),
	('Not so cool event', '2020-2021',2);

INSERT INTO Participates(Username, EventID,[Type])
VALUES ('Dobo', 1,'chair'),
	('DeliaO',2, 'chair');
