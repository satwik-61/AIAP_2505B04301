-- Library Management System Schema

-- 1. BOOKS TABLE
-- Stores information about all books in the library
CREATE TABLE Books (
    BookID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    ISBN VARCHAR(13) UNIQUE NOT NULL,
    PublicationYear INT,
    Publisher VARCHAR(255),
    Category VARCHAR(100),
    TotalCopies INT NOT NULL DEFAULT 1,
    AvailableCopies INT NOT NULL DEFAULT 1,
    Location VARCHAR(100),
    DateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_copies CHECK (AvailableCopies <= TotalCopies AND AvailableCopies >= 0)
);

-- 2. MEMBERS TABLE
-- Stores information about library members
CREATE TABLE Members (
    MemberID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    PhoneNumber VARCHAR(20),
    Address VARCHAR(500),
    City VARCHAR(100),
    PostalCode VARCHAR(20),
    MembershipType ENUM('Standard', 'Premium', 'Student', 'Senior') DEFAULT 'Standard',
    MembershipStartDate DATE NOT NULL,
    MembershipExpiryDate DATE,
    IsActive BOOLEAN DEFAULT TRUE,
    MaxBooksAllowed INT DEFAULT 5,
    Fine DECIMAL(10, 2) DEFAULT 0.00,
    DateRegistered TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_expiry CHECK (MembershipExpiryDate IS NULL OR MembershipExpiryDate >= MembershipStartDate)
);

-- 3. LOANS TABLE
-- Stores information about book loans
CREATE TABLE Loans (
    LoanID INT PRIMARY KEY AUTO_INCREMENT,
    BookID INT NOT NULL,
    MemberID INT NOT NULL,
    LoanDate DATE NOT NULL,
    DueDate DATE NOT NULL,
    ReturnDate DATE,
    LoanStatus ENUM('Active', 'Returned', 'Overdue') DEFAULT 'Active',
    LateFine DECIMAL(10, 2) DEFAULT 0.00,
    Notes VARCHAR(500),
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT check_dates CHECK (DueDate > LoanDate AND (ReturnDate IS NULL OR ReturnDate >= LoanDate))
);

-- INDEXES for better query performance
CREATE INDEX idx_books_category ON Books(Category);
CREATE INDEX idx_books_author ON Books(Author);
CREATE INDEX idx_members_email ON Members(Email);
CREATE INDEX idx_members_status ON Members(IsActive);
CREATE INDEX idx_loans_bookid ON Loans(BookID);
CREATE INDEX idx_loans_memberid ON Loans(MemberID);
CREATE INDEX idx_loans_status ON Loans(LoanStatus);
CREATE INDEX idx_loans_duedate ON Loans(DueDate);

-- VIEWS for common queries

-- View to see books currently available
CREATE VIEW AvailableBooks AS
SELECT 
    BookID,
    Title,
    Author,
    Category,
    AvailableCopies,
    TotalCopies,
    Location
FROM Books
WHERE AvailableCopies > 0;

-- View to see active loans with book and member details
CREATE VIEW ActiveLoans AS
SELECT 
    l.LoanID,
    b.Title,
    b.Author,
    m.FirstName,
    m.LastName,
    m.Email,
    l.LoanDate,
    l.DueDate,
    DATEDIFF(CURDATE(), l.DueDate) AS DaysOverdue,
    l.LoanStatus
FROM Loans l
JOIN Books b ON l.BookID = b.BookID
JOIN Members m ON l.MemberID = m.MemberID
WHERE l.LoanStatus IN ('Active', 'Overdue');

-- View to see member activity
CREATE VIEW MemberActivity AS
SELECT 
    m.MemberID,
    CONCAT(m.FirstName, ' ', m.LastName) AS MemberName,
    m.Email,
    COUNT(l.LoanID) AS TotalBorrowedBooks,
    SUM(CASE WHEN l.LoanStatus = 'Active' THEN 1 ELSE 0 END) AS CurrentlyBorrowedBooks,
    MAX(l.LoanDate) AS LastBorrowDate,
    m.Fine AS OutstandingFine
FROM Members m
LEFT JOIN Loans l ON m.MemberID = l.MemberID
WHERE m.IsActive = TRUE
GROUP BY m.MemberID;

