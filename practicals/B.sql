-- Since "create the table" is no longer in the question, you won't have to
-- write this when you write your practicals. It's probably a good idea to test
-- your code before you write it, and the rest of the file won't work without
-- this

CREATE TABLE Stock(
    ItemNo INTEGER,
    IName VARCHAR(100),
    DCode INTEGER,
    Qty INTEGER,
    UPrice INTEGER,
    StockDate DATE,
    PRIMARY KEY(ItemNo)
);

INSERT INTO Stock VALUES
    (5005, "Ball pen 0.5", 102, 100, 16, "2010-03-30"),
    (5003, "Ball pen 0.25", 102, 150, 20, "2010-01-01"),
    (5002, "Gel pen premium", 102, 125, 14, "2010-02-14"),
    (5006, "Gel pen classic", 102, 200, 22, "2009-01-01"),
    (5001, "Eraser small", 102, 210, 5, "2009-03-19"),
    (5004, "Eraser big", 102, 60, 10, "2009-12-12");

-- Writing part starts here

-- (i)
SELECT * FROM Stock ORDER BY StockDate;

-- (ii)
SELECT * FROM Stock WHERE DCode = 102 OR Qty > 100;

-- (iii)
SELECT DCode, MAX(UPrice) FROM Stock GROUP BY DCode;

-- (iv)
SELECT DCode, SUM(Qty) FROM Stock GROUP BY DCode;