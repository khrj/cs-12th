CREATE TABLE marks (
	stid INTEGER PRIMARY KEY,
	aadhaarno CHAR(14),
	physics INTEGER,
	chemistry INTEGER,
	maths INTEGER
);

ALTER TABLE marks
ADD CONSTRAINT fk_aadhaar
FOREIGN KEY (aadhaarno)
REFERENCES student(aadhaarno);

INSERT INTO student 
	(stname, aadhaarno, hobby, dob)
VALUES
	("Rashmi", "4733 6592 2270", "dance", "2010-05-07"),
	("Tanu", "4640 0039 0437", "music", "2006-07-04"),
	("Hritik", "9897 3757 8824", "dance", "2007-01-13"),
	("Rakesh", "3092 3016 5011", "sport", "2004-03-09"),
	("Minali", "8155 3614 5390", "sport", "2014-03-10"),
	("Amrit", "9023 1977 2793", "music", "2004-09-12"),
	("Rati", "5214 0664 7499", "dance", "2018-03-22"),
	("Kalyan", "3469 7948 7075", "dance", "2014-12-20");

INSERT INTO marks 
	(stid, aadhaarno, physics, chemistry, maths)
VALUES 
	('1', '3092 3016 5011', null, '78', '90'),
	('2', '3469 7948 7075', '68', '79', '81'),
	('3', '4640 0039 0437', '80', null, '90'),
	('4', '4733 6592 2270', '48', '89', '75'),
	('5', '5214 0664 7499', '69', null, '68'),
	('6', '8155 3614 5390', '86', '93', '74'),
	('7', '9023 1977 2793', '92', '95', '80'),
	('8', '9897 3757 8824', '98', '94', '78');

UPDATE marks SET physics = marks.physics * (1/10) + marks.physics;
UPDATE marks SET physics = 100 WHERE marks.physics > 100;

UPDATE student SET stname = "Minalee" WHERE stname = "Minali";
UPDATE student SET stname = "Amreet" WHERE stname = "Amrit";

INSERT INTO student 
	(stname, aadhaarno, hobby, dob)
VALUES
	("Anaya", "7243 0294 8689", "dance", "2010-02-11"),
	("Subhash", "9335 1910 3036", "music", "2017-05-19"),
	("Talika", "8119 0574 4980", "sport", "2004-03-22");

INSERT INTO marks 
	(stid, aadhaarno, physics, chemistry, maths)
VALUES 
	('9', '7243 0294 8689', null, '78', '90'),
	('10', '9335 1910 3036', '68', '79', '81'),
	('11', '8119 0574 4980', '80', null, '90');

DELETE FROM marks WHERE aadhaarno = "8119 0574 4980";
DELETE FROM student WHERE aadhaarno = "8119 0574 4980";

UPDATE marks SET maths = "95" WHERE aadhaarno = "9335 1910 3036";

UPDATE student 
SET marks_percent = (
	SELECT (physics + chemistry + maths)/3 
	FROM marks
	WHERE aadhaarno = student.aadhaarno
); 
