function printStudents(students) {
    console.log("Student Names:");
    students.forEach((student, index) => {
        console.log(`${index + 1}. ${student}`);
    });
}

// Test with sample student names
const studentList = ["Alice", "Bob", "Charlie", "Diana", "Eve"];
printStudents(studentList);
