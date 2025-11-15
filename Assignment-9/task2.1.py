from dataclasses import dataclass, field
from typing import Union

#Represent a student at SR University.
@dataclass
class SRUStudent:
    name: str
    roll_no: Union[int, str]
    hostel_status: bool
    fee_due: float = field(default=0.0)

    #Update the outstanding fee amount.
    def fee_update(self, amount: float) -> None:
        self.fee_due = max(self.fee_due + amount, 0.0)
    
    #Return a formatted multi-line string with the student's details.
    def display_details(self) -> str:
        hostel_text = "Hosteller" if self.hostel_status else "Day Scholar"
        return (
            f"Name          : {self.name}\n"
            f"Roll Number   : {self.roll_no}\n"
            f"Hostel Status : {hostel_text}\n"
            f"Fee Due       : ₹{self.fee_due:,.2f}"
        )


if __name__ == "__main__":
    # Example usage
    student = SRUStudent(name="Ananya Singh", roll_no="22CS101", hostel_status=True, fee_due=15000.0)
    print("Before update:")
    print(student.display_details())

    student.fee_update(-5000.0)
    print("\nAfter update:")
    print(student.display_details())

