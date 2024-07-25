SELECT * FROM student;
SELECT * FROM marks;

SELECT stname, hobby FROM student;
SELECT stname FROM student WHERE marks_percent < 35;

SELECT stname, marks_percent FROM student 
WHERE marks_percent = (SELECT max(marks_percent) FROM student);
SELECT stname, marks_percent FROM student
WHERE marks_percent = (SELECT min(marks_percent) FROM student);

SELECT stname FROM student WHERE hobby IS NULL;

SELECT DISTINCT hobby FROM student;

SELECT hobby, count(hobby) FROM student GROUP BY hobby;

SELECT stname, marks_percent FROM student ORDER BY marks_percent DESC;

SELECT stname, aadhaarno FROM student WHERE stname = "Hritik";

SELECT stname 
FROM student
JOIN marks ON marks.aadhaarno = student.aadhaarno
WHERE marks.physics = (SELECT max(physics) FROM marks);

SELECT stname 
FROM student
JOIN marks ON marks.aadhaarno = student.aadhaarno
WHERE marks.chemistry = (SELECT max(chemistry) FROM marks);

SELECT stname 
FROM student
JOIN marks ON marks.aadhaarno = student.aadhaarno
WHERE marks.maths = (SELECT max(maths) FROM marks);

SELECT AVG(maths), AVG(physics), AVG(chemistry) FROM marks;

SELECT stname, marks.stid, dob
FROM student
JOIN marks ON marks.aadhaarno = student.aadhaarno
ORDER BY dob ASC;

SELECT * FROM student
CROSS JOIN marks;

SELECT * FROM student 
WHERE marks_percent BETWEEN 50 AND 70;

SELECT stname FROM student
WHERE hobby = "dance" OR hobby = "music";

SELECT * FROM student
JOIN marks ON student.aadhaarno = marks.aadhaarno;

SELECT stname FROM student 
WHERE stname LIKE "m%" OR stname LIKE "s%";

SELECT stname FROM student
WHERE stname LIKE "_a%";

