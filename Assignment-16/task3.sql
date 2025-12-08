-- Query to list all books borrowed by a specific member

-- Method 1: Using Member ID (Replace 1 with the desired MemberID)
SELECT 
    l.LoanID,
    b.BookID,
    b.Title,
    b.Author,
    b.Category,
    l.LoanDate,
    l.DueDate,
    l.ReturnDate,
    l.LoanStatus,
    DATEDIFF(CURDATE(), l.DueDate) AS DaysOverdue,
    l.LateFine,
    l.Notes
FROM Loans l
JOIN Books b ON l.BookID = b.BookID
WHERE l.MemberID = 1
ORDER BY l.LoanDate DESC;

-- ========================================
-- Method 2: Using Member Name (More user-friendly)
-- Replace 'John' and 'Smith' with the desired member's first and last name
-- ========================================

SELECT 
    l.LoanID,
    b.BookID,
    b.Title,
    b.Author,
    b.Category,
    l.LoanDate,
    l.DueDate,
    l.ReturnDate,
    l.LoanStatus,
    DATEDIFF(CURDATE(), l.DueDate) AS DaysOverdue,
    l.LateFine,
    l.Notes
FROM Loans l
JOIN Books b ON l.BookID = b.BookID
JOIN Members m ON l.MemberID = m.MemberID
WHERE m.FirstName = 'John' AND m.LastName = 'Smith'
ORDER BY l.LoanDate DESC;

-- ========================================
-- Method 3: List only ACTIVE loans for a specific member
-- ========================================

SELECT 
    l.LoanID,
    b.BookID,
    b.Title,
    b.Author,
    b.Category,
    l.LoanDate,
    l.DueDate,
    DATEDIFF(CURDATE(), l.DueDate) AS DaysOverdue,
    CASE 
        WHEN DATEDIFF(CURDATE(), l.DueDate) > 0 THEN 'OVERDUE'
        ELSE 'ON TIME'
    END AS DueStatus,
    l.LateFine
FROM Loans l
JOIN Books b ON l.BookID = b.BookID
WHERE l.MemberID = 1 AND l.LoanStatus = 'Active'
ORDER BY l.DueDate ASC;

-- ========================================
-- Method 4: List all loans with member details for a specific member
-- ========================================

SELECT 
    m.MemberID,
    CONCAT(m.FirstName, ' ', m.LastName) AS MemberName,
    m.Email,
    m.PhoneNumber,
    m.MembershipType,
    COUNT(l.LoanID) AS TotalBorrowedBooks,
    SUM(CASE WHEN l.LoanStatus = 'Active' THEN 1 ELSE 0 END) AS CurrentlyBorrowedBooks,
    SUM(CASE WHEN l.LoanStatus = 'Returned' THEN 1 ELSE 0 END) AS ReturnedBooks,
    MAX(m.Fine) AS OutstandingFine
FROM Members m
LEFT JOIN Loans l ON m.MemberID = l.MemberID
WHERE m.MemberID = 1
GROUP BY m.MemberID;

-- ========================================
-- Method 5: Detailed view with book details for a specific member
-- ========================================

SELECT 
    l.LoanID,
    b.Title,
    b.Author,
    b.ISBN,
    b.Category,
    l.LoanDate,
    l.DueDate,
    l.ReturnDate,
    l.LoanStatus,
    CASE 
        WHEN l.LoanStatus = 'Returned' THEN 'Completed'
        WHEN DATEDIFF(CURDATE(), l.DueDate) > 0 THEN 'OVERDUE'
        ELSE 'Active - ' || DATEDIFF(l.DueDate, CURDATE()) || ' days remaining'
    END AS Status,
    l.LateFine,
    l.Notes
FROM Loans l
JOIN Books b ON l.BookID = b.BookID
WHERE l.MemberID = 1
ORDER BY l.LoanStatus DESC, l.DueDate ASC;
