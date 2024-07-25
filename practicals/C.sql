-- Since "create the table" is no longer in the question, you won't have to
-- write this when you write your practicals. It's probably a good idea to test
-- your code before you write it, and the rest of the file won't work without
-- this

CREATE TABLE Product(
    PCode VARCHAR(10),
    ProductName VARCHAR(100),
    UPrice INTEGER,
    Rating INTEGER,
    BID VARCHAR(10),
    PRIMARY KEY(PCode)
);

CREATE TABLE Brand(
    BID VARCHAR(10),
    BrandName VARCHAR(100),
    PRIMARY KEY(BID)
);

INSERT INTO Product VALUES
    ("P01", "Shampoo", 120, 6, "M03"),
    ("P02", "Toothpaste", 54, 8, "M02"),
    ("P03", "Soap", 25, 7, "M03"),
    ("P04", "Toothpaste", 65, 4, "M04"),
    ("P05", "Soap", 38, 5, "M05"),
    ("P06", "Shampoo", 245, 6, "M05");

INSERT INTO Brand VALUES
    ("M02", "Dant Kanti"),
    ("M03", "Medimix"),
    ("M04", "Pepsodent"),
    ("M05", "Dove");

-- Writing part starts here

-- (i)
SELECT ProductName, BrandName FROM Product
JOIN Brand ON Brand.BID = Product.BID;

-- (ii)
DESC Product;

-- (iii)
SELECT BrandName, AVG(Rating) FROM Product
JOIN Brand ON Brand.BID = Product.BID
WHERE BrandName IN ("Medimix", "Dove")
GROUP BY BrandName;

-- (iv)
SELECT ProductName, BrandName, Rating FROM Product
JOIN Brand ON Brand.BID = Product.BID
ORDER BY Rating DESC;