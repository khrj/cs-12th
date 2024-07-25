-- Since "create the table" is no longer in the question, you won't have to
-- write this when you write your practicals. It's probably a good idea to test
-- your code before you write it, and the rest of the file won't work without
-- this

CREATE TABLE Bank(
    AcctNo INTEGER,
    CCode INTEGER,
    BName VARCHAR(100),
    Amount INTEGER,
    Transactions INTEGER,
    PRIMARY KEY(AcctNo)
);

INSERT INTO Bank VALUES
    (1, 4, "Bank of Baroda", 15000, 10),
    (2, 3, "SBI", 25000, 9),
    (3, 5, "Oriental bank", 17000, 5),
    (4, 1, "Oriental bank", 38000, 11),
    (5, 2, "Oriental bank", 47000, 15),
    (6, 6, "Bank of Baroda", 56000, 12);

-- Writing part starts here

-- (i)
SELECT * FROM Bank ORDER BY Amount;

-- (ii)
SELECT * FROM Bank WHERE Transactions BETWEEN 8 AND 11;

-- (iii)
SELECT BName, COUNT(*) FROM Bank GROUP BY BName;

-- (iv)
UPDATE Bank SET Amount = Amount + 100 WHERE BName = "SBI";