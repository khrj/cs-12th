CREATE DATABASE cspract;
USE cspract;

CREATE TABLE student (
	stid INTEGER,
	stname VARCHAR(25),
	aadhaarno CHAR(14) UNIQUE NOT NULL,
	marks_percent INTEGER,
	hobby ENUM("dance", "music", "sport"),
	cellno VARCHAR(13)
);

ALTER TABLE student
ADD CONSTRAINT pk_aadhaar PRIMARY KEY (aadhaarno),
ADD COLUMN dob DATE,
DROP COLUMN cellno,
DROP COLUMN stid;





