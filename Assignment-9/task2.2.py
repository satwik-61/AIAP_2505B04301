from dataclasses import dataclass, field  # Import helpers to create data classes and default fields.
from typing import Union  # Import Union so roll numbers can be either int or str.

@dataclass  # Tell Python to auto-generate init and repr based on the fields below.
class SRUStudent:
    """Represent a student at SR University with fee tracking."""  # Give a concise class description.

    name: str  # Store the student's full name as text.
    roll_no: Union[int, str]  # Store roll number, allowing numeric or alphanumeric formats.
    hostel_status: bool  # Track whether the student stays in the hostel (True) or not (False).
    fee_due: float = field(default=0.0)  # Track outstanding fee amount, defaulting to zero.

    def fee_update(self, amount: float) -> None:  # Method to adjust the fee balance by the given amount.
        """
        Update the outstanding fee amount, ensuring it never becomes negative.  # Document method behavior.
        """  # End of docstring description.
        self.fee_due = max(self.fee_due + amount, 0.0)  # Add amount and clamp at zero to prevent negative dues.

    def display_details(self) -> str:  # Method to format key student details for display.
        """Return formatted student details including hostel status and fee data."""  # Document return info.
        hostel_text = "Hosteller" if self.hostel_status else "Day Scholar"  # Choose readable hostel label.
        return (  # Build and return the multi-line string.
            f"Name          : {self.name}\n"  # Include the student's name.
            f"Roll Number   : {self.roll_no}\n"  # Include the roll number.
            f"Hostel Status : {hostel_text}\n"  # Include hostel status in words.
            f"Fee Due       : ₹{self.fee_due:,.2f}"  # Include fee due formatted with currency symbol.
        )

if __name__ == "__main__":  # Allow demo execution when running this file directly.
    student = SRUStudent(name="Ananya Singh", roll_no="22CS101", hostel_status=True, fee_due=15000.0)  # Create demo student.
    print("Before update:")  # Label upcoming details as pre-update.
    print(student.display_details())  # Show original student data.

    student.fee_update(-5000.0)  # Reduce fee due by applying a payment adjustment.
    print("\nAfter update:")  # Separate sections and label them post-update.
    print(student.display_details())  # Show updated student data after fee adjustment.

