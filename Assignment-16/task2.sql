-- Library Management System - Sample Data
-- INSERT INTO queries for Books, Members, and Loans tables

-- ========================================
-- INSERT INTO BOOKS TABLE (3 sample records)
-- ========================================

INSERT INTO Books (Title, Author, ISBN, PublicationYear, Publisher, Category, TotalCopies, AvailableCopies, Location)
VALUES 
('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 1925, 'Scribner', 'Fiction', 5, 3, 'Shelf A1'),
('To Kill a Mockingbird', 'Harper Lee', '9780061120084', 1960, 'J. B. Lippincott', 'Fiction', 4, 2, 'Shelf A2'),
('1984', 'George Orwell', '9780451524935', 1949, 'Signet Classic', 'Dystopian', 6, 5, 'Shelf B1');

-- ========================================
-- INSERT INTO MEMBERS TABLE (3 sample records)
-- ========================================

INSERT INTO Members (FirstName, LastName, Email, PhoneNumber, Address, City, PostalCode, MembershipType, MembershipStartDate, MembershipExpiryDate, IsActive, MaxBooksAllowed, Fine)
VALUES
('John', 'Smith', 'john.smith@email.com', '555-0101', '123 Oak Street', 'New York', '10001', 'Standard', '2024-01-15', '2025-01-15', TRUE, 5, 0.00),
('Sarah', 'Johnson', 'sarah.johnson@email.com', '555-0102', '456 Maple Avenue', 'Los Angeles', '90001', 'Premium', '2023-06-20', '2026-06-20', TRUE, 10, 5.50),
('Michael', 'Brown', 'michael.brown@email.com', '555-0103', '789 Pine Road', 'Chicago', '60601', 'Student', '2024-09-01', '2025-09-01', TRUE, 3, 0.00);

-- ========================================
-- INSERT INTO LOANS TABLE (3 sample records)
-- ========================================

INSERT INTO Loans (BookID, MemberID, LoanDate, DueDate, ReturnDate, LoanStatus, LateFine, Notes)
VALUES
(1, 1, '2024-11-20', '2024-12-04', NULL, 'Active', 0.00, 'Regular loan'),
(2, 2, '2024-11-10', '2024-12-10', '2024-12-05', 'Returned', 0.00, 'Returned on time'),
(3, 3, '2024-11-25', '2024-12-09', NULL, 'Active', 0.00, 'Regular loan');
