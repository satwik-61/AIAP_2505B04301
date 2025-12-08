-- Library Management System - UPDATE and DELETE Queries

-- ========================================
-- UPDATING BOOK AVAILABILITY
-- ========================================

-- Method 1: Decrease available copies when a book is borrowed
-- This should be executed when a new loan is created
UPDATE Books
SET AvailableCopies = AvailableCopies - 1
WHERE BookID = 1 AND AvailableCopies > 0;

-- ========================================
-- Method 2: Increase available copies when a book is returned
-- This should be executed when a loan is marked as returned
UPDATE Books
SET AvailableCopies = AvailableCopies + 1
WHERE BookID = 1 AND AvailableCopies < TotalCopies;

-- ========================================
-- Method 3: Update availability using a transaction with proper error handling
-- Ensures atomicity and consistency
-- ========================================

BEGIN TRANSACTION;

-- Check if book has available copies before borrowing
IF (SELECT AvailableCopies FROM Books WHERE BookID = 1) > 0
BEGIN
    -- Decrease available copies
    UPDATE Books
    SET AvailableCopies = AvailableCopies - 1
    WHERE BookID = 1;
    
    -- Insert the loan record
    INSERT INTO Loans (BookID, MemberID, LoanDate, DueDate, LoanStatus)
    VALUES (1, 1, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 14 DAY), 'Active');
    
    PRINT 'Book borrowed successfully';
END
ELSE
BEGIN
    ROLLBACK;
    PRINT 'Error: Book is not available';
END

COMMIT;

-- ========================================
-- Method 4: Update book status to reflect all copies unavailable
-- Set AvailableCopies to 0 when no copies are left
-- ========================================

UPDATE Books
SET AvailableCopies = 0
WHERE BookID = 2 AND AvailableCopies <= 0;

-- ========================================
-- DELETING MEMBER RECORDS SAFELY
-- ========================================

-- Method 1: Check before deleting - View all loans for a member
-- Always execute this first to understand member's history
SELECT 
    m.MemberID,
    CONCAT(m.FirstName, ' ', m.LastName) AS MemberName,
    COUNT(l.LoanID) AS TotalLoans,
    SUM(CASE WHEN l.LoanStatus = 'Active' THEN 1 ELSE 0 END) AS ActiveLoans,
    SUM(CASE WHEN l.LoanStatus = 'Overdue' THEN 1 ELSE 0 END) AS OverdueLoans,
    m.Fine AS OutstandingFine
FROM Members m
LEFT JOIN Loans l ON m.MemberID = l.MemberID
WHERE m.MemberID = 3
GROUP BY m.MemberID;

-- ========================================
-- Method 2: Safe deletion with validation
-- Only delete if member has no active loans and no outstanding fines
-- ========================================

DELETE FROM Members
WHERE MemberID = 3 
  AND MemberID NOT IN (
    SELECT DISTINCT MemberID 
    FROM Loans 
    WHERE LoanStatus IN ('Active', 'Overdue')
  )
  AND Fine = 0.00;

-- ========================================
-- Method 3: Soft delete approach (Recommended for audit trails)
-- Mark member as inactive instead of deleting
-- Preserves historical data and loan records
-- ========================================

UPDATE Members
SET IsActive = FALSE
WHERE MemberID = 3;

-- Query to view inactive members
SELECT 
    MemberID,
    CONCAT(FirstName, ' ', LastName) AS MemberName,
    Email,
    IsActive,
    DateRegistered,
    MembershipExpiryDate
FROM Members
WHERE IsActive = FALSE;

-- ========================================
-- Method 4: Cascade delete with transaction (Use with caution)
-- Delete member and all associated loan records
-- Warning: This permanently removes loan history
-- ========================================

BEGIN TRANSACTION;

-- Check if member exists and has no outstanding fines
IF EXISTS (SELECT 1 FROM Members WHERE MemberID = 3 AND Fine = 0.00)
BEGIN
    -- Delete all loans associated with the member
    DELETE FROM Loans WHERE MemberID = 3;
    
    -- Delete the member record
    DELETE FROM Members WHERE MemberID = 3;
    
    PRINT 'Member record deleted successfully';
    COMMIT;
END
ELSE
BEGIN
    PRINT 'Error: Member has outstanding fines or does not exist';
    ROLLBACK;
END

-- ========================================
-- Method 5: Archive member data before deletion
-- Create backup before permanent deletion
-- ========================================

-- Create backup table (run once to set up)
CREATE TABLE IF NOT EXISTS Members_Archive AS
SELECT * FROM Members WHERE 1=0;

-- Archive member data before deletion
INSERT INTO Members_Archive
SELECT * FROM Members WHERE MemberID = 3;

-- Then delete the member
DELETE FROM Members WHERE MemberID = 3;

-- ========================================
-- Method 6: View active members with borrowing status
-- Useful for identifying members to keep or remove
-- ========================================

SELECT 
    m.MemberID,
    CONCAT(m.FirstName, ' ', m.LastName) AS MemberName,
    m.Email,
    m.MembershipType,
    m.IsActive,
    COUNT(l.LoanID) AS BorrowingCount,
    MAX(l.LoanDate) AS LastBorrowDate,
    m.Fine,
    DATEDIFF(m.MembershipExpiryDate, CURDATE()) AS DaysUntilExpiry
FROM Members m
LEFT JOIN Loans l ON m.MemberID = l.MemberID
GROUP BY m.MemberID
ORDER BY m.IsActive DESC, m.MembershipExpiryDate ASC;

-- ========================================
-- Method 7: Comprehensive deletion workflow
-- This is the safest approach for production systems
-- ========================================

-- Step 1: Verify member has no active loans
SELECT COUNT(*) AS ActiveLoans
FROM Loans
WHERE MemberID = 3 AND LoanStatus = 'Active';

-- Step 2: Verify member has no outstanding fines
SELECT Fine FROM Members WHERE MemberID = 3;

-- Step 3: Archive member data
INSERT INTO Members_Archive
SELECT * FROM Members WHERE MemberID = 3;

-- Step 4: Archive member's loan history
INSERT INTO Loans_Archive
SELECT * FROM Loans WHERE MemberID = 3;

-- Step 5: Delete loans first (if needed)
DELETE FROM Loans WHERE MemberID = 3;

-- Step 6: Delete member record
DELETE FROM Members WHERE MemberID = 3;
