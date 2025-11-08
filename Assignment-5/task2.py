import json
import os
from datetime import datetime
# File to store loan applications
LOANS_FILE = "loans.json"

def load_loans():
    """Load loan applications from JSON file"""
    if os.path.exists(LOANS_FILE):
        try:
            with open(LOANS_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_loans(loans):
    """Save loan applications to JSON file"""
    with open(LOANS_FILE, 'w') as f:
        json.dump(loans, f, indent=2)

def calculate_loan_eligibility(applicant_data):
    """Calculate loan eligibility based on applicant data"""
    name = applicant_data.get('name', '')
    gender = applicant_data.get('gender', '').lower()
    age = applicant_data.get('age', 0)
    income = applicant_data.get('income', 0)
    credit_score = applicant_data.get('credit_score', 0)
    loan_amount = applicant_data.get('loan_amount', 0)
    employment_status = applicant_data.get('employment_status', '').lower()
    loan_purpose = applicant_data.get('loan_purpose', '').lower()
    
    # Initialize result
    result = {
        'approved': False,
        'reason': '',
        'approved_amount': 0,
        'interest_rate': 0,
        'loan_tenure': 0
    }
    
    # Basic validations
    if age < 18:
        result['reason'] = "Applicant must be at least 18 years old."
        return result
    
    if age > 70:
        result['reason'] = "Applicant age exceeds maximum limit (70 years)."
        return result
    
    if income <= 0:
        result['reason'] = "Invalid income amount."
        return result
    
    if loan_amount <= 0:
        result['reason'] = "Invalid loan amount."
        return result
    
    if credit_score < 300 or credit_score > 850:
        result['reason'] = "Invalid credit score (must be between 300-850)."
        return result
    
    # Loan eligibility criteria
    
    # 1. Credit Score Check
    if credit_score < 600:
        result['reason'] = f"Credit score too low ({credit_score}). Minimum required: 600."
        return result
    # 2. Employment Status Check
    if employment_status not in ['employed', 'self-employed', 'business owner']:
        result['reason'] = "Must be employed, self-employed, or a business owner."
        return result

    # 3. Income to Loan Ratio (Loan amount should not exceed 5x annual income)
    if loan_amount > (income * 5):
        max_loan = income * 5
        result['reason'] = f"Loan amount exceeds maximum limit (5x annual income). Maximum eligible: ${max_loan:,.2f}"
        return result
    
    # 4. Minimum Income Requirements
    min_income_required = 20000
    if income < min_income_required:
        result['reason'] = f"Income below minimum requirement (${min_income_required:,} per year)."
        return result
    
    # Approval logic based on credit score and other factors
    approved = True
    approved_amount = loan_amount
    interest_rate = 0
    loan_tenure = 0
    
    # Determine interest rate based on credit score
    if credit_score >= 750:
        interest_rate = 6.5  # Excellent credit
        loan_tenure = 10  # years
    elif credit_score >= 700:
        interest_rate = 7.5  # Good credit
        loan_tenure = 8
    elif credit_score >= 650:
        interest_rate = 9.0  # Fair credit
        loan_tenure = 5
    else:  # 600-649
        interest_rate = 11.5  # Poor but acceptable credit
        loan_tenure = 3
    
    # Adjust based on loan purpose
    if loan_purpose in ['education', 'medical']:
        interest_rate -= 0.5  # Lower interest for essential purposes
        if interest_rate < 5.0:
            interest_rate = 5.0
    elif loan_purpose in ['business', 'investment']:
        interest_rate += 0.5  # Higher interest for business/investment
    
    # Gender-based considerations (equal treatment, but different risk assessment if needed)
    # Note: In many jurisdictions, gender cannot be a factor, but we can track it for statistics
    # Here we treat all genders equally in approval decisions
    
    # Age-based tenure adjustment
    if age > 60:
        # Reduce maximum tenure for older applicants
        max_tenure_by_age = 70 - age
        if loan_tenure > max_tenure_by_age:
            loan_tenure = max_tenure_by_age
    
    # Final amount adjustment based on debt-to-income ratio
    # Assume 30% of income can go to loan payments
    monthly_income = income / 12
    max_monthly_payment = monthly_income * 0.30
    
    # Calculate if the loan payment is affordable
    # Simplified calculation: Principal + Interest over tenure
    annual_payment = (approved_amount * (interest_rate / 100)) + (approved_amount / loan_tenure)
    monthly_payment = annual_payment / 12
    
    if monthly_payment > max_monthly_payment:
        # Reduce loan amount to make it affordable
        # Solve for affordable loan amount
        # monthly_payment = (loan_amount * (interest_rate/100) / 12) + (loan_amount / (loan_tenure * 12))
        # monthly_payment = loan_amount * ((interest_rate/100)/12 + 1/(loan_tenure*12))
        # loan_amount = monthly_payment / ((interest_rate/100)/12 + 1/(loan_tenure*12))
        monthly_interest_factor = (interest_rate / 100) / 12
        monthly_principal_factor = 1 / (loan_tenure * 12)
        affordable_amount = max_monthly_payment / (monthly_interest_factor + monthly_principal_factor)
        if affordable_amount < loan_amount * 0.5:
            result['approved'] = False
            result['reason'] = f"Loan amount not affordable based on income. Maximum affordable amount: ${affordable_amount:,.2f}"
            return result
        else:
            approved_amount = affordable_amount
            result['reason'] = f"Loan amount adjusted to affordable limit: ${approved_amount:,.2f}"
    
    # Set final results
    result['approved'] = approved
    if result['reason'] == '':
        result['reason'] = "Loan approved based on eligibility criteria."
    result['approved_amount'] = round(approved_amount, 2)
    result['interest_rate'] = round(interest_rate, 2)
    result['loan_tenure'] = loan_tenure
    result['monthly_payment'] = round(monthly_payment, 2)
    
    return result

def apply_for_loan():
    """Apply for a loan"""
    print("\n=== Loan Application ===")
    
    # Get applicant information
    name = input("Enter full name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    
    print("\nGender options:")
    print("1. Male")
    print("2. Female")
    print("3. Other")
    gender_choice = input("Select gender (1-3): ").strip()
    gender_map = {'1': 'Male', '2': 'Female', '3': 'Other'}
    gender = gender_map.get(gender_choice, 'Other')
    try:
        age = int(input("Enter age: ").strip())
    except ValueError:
        print("Invalid age!")
        return   
    try:
        income = float(input("Enter annual income ($): ").strip())
    except ValueError:
        print("Invalid income amount!")
        return   
    try:
        credit_score = int(input("Enter credit score (300-850): ").strip())
    except ValueError:
        print("Invalid credit score!")
        return   
    print("\nEmployment Status:")
    print("1. Employed")
    print("2. Self-Employed")
    print("3. Business Owner")
    emp_choice = input("Select employment status (1-3): ").strip()    
    emp_map = {'1': 'Employed', '2': 'Self-Employed', '3': 'Business Owner'}
    employment_status = emp_map.get(emp_choice, 'Employed')  
    print("\nLoan Purpose:")
    print("1. Home Purchase")
    print("2. Education")
    print("3. Medical")
    print("4. Business")
    print("5. Personal")
    print("6. Investment")
    purpose_choice = input("Select loan purpose (1-6): ").strip()   
    purpose_map = {
        '1': 'Home Purchase',
        '2': 'Education',
        '3': 'Medical',
        '4': 'Business',
        '5': 'Personal',
        '6': 'Investment'
    }
    loan_purpose = purpose_map.get(purpose_choice, 'Personal')
    
    try:
        loan_amount = float(input("Enter requested loan amount ($): ").strip())
    except ValueError:
        print("Invalid loan amount!")
        return  
    # Create applicant data
    applicant_data = {
        'name': name,
        'gender': gender,
        'age': age,
        'income': income,
        'credit_score': credit_score,
        'employment_status': employment_status,
        'loan_purpose': loan_purpose,
        'loan_amount': loan_amount,
        'application_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }    
    # Calculate eligibility
    print("\nProcessing application...")
    result = calculate_loan_eligibility(applicant_data)   
    # Store application
    application = {
        **applicant_data,
        'approved': result['approved'],
        'approved_amount': result['approved_amount'],
        'interest_rate': result['interest_rate'],
        'loan_tenure': result['loan_tenure'],
        'monthly_payment': result.get('monthly_payment', 0),
        'reason': result['reason'],
        'application_id': f"LOAN-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    }    
    loans = load_loans()
    loans.append(application)
    save_loans(loans)   
    # Display results
    print("\n" + "="*50)
    print("    LOAN APPLICATION RESULT")
    print("="*50)
    print(f"Application ID: {application['application_id']}")
    print(f"Applicant Name: {name}")
    print(f"Gender: {gender}")
    print(f"Status: {'APPROVED' if result['approved'] else 'REJECTED'}")
    print(f"Reason: {result['reason']}")   
    if result['approved']:
        print(f"\nApproved Loan Amount: ${result['approved_amount']:,.2f}")
        print(f"Interest Rate: {result['interest_rate']}%")
        print(f"Loan Tenure: {result['loan_tenure']} years")
        print(f"Monthly Payment: ${result.get('monthly_payment', 0):,.2f}")
    print("="*50)
def view_all_loans():
    """View all loan applications"""
    print("\n=== All Loan Applications ===")
    loans = load_loans()   
    if not loans:
        print("No loan applications found.")
        return 
    print(f"\nTotal Applications: {len(loans)}")
    print("\n" + "-"*80)
    print(f"{'ID':<15} {'Name':<20} {'Gender':<8} {'Amount':<12} {'Status':<10} {'Date':<20}")
    print("-"*80)  
    for loan in loans:
        status = "APPROVED" if loan.get('approved', False) else "REJECTED"
        amount = loan.get('approved_amount', loan.get('loan_amount', 0))
        app_date = loan.get('application_date', 'N/A')
        if len(app_date) > 19:
            app_date = app_date[:19]        
        print(f"{loan.get('application_id', 'N/A'):<15} "
              f"{loan.get('name', 'N/A'):<20} "
              f"{loan.get('gender', 'N/A'):<8} "
              f"${amount:>10,.2f} "
              f"{status:<10} "
              f"{app_date:<20}")
def view_loan_details():
    """View details of a specific loan application"""
    print("\n=== Loan Application Details ===")
    application_id = input("Enter Application ID: ").strip()   
    loans = load_loans()
    loan = None   
    for l in loans:
        if l.get('application_id') == application_id:
            loan = l
            break   
    if not loan:
        print("Application not found!")
        return   
    print("\n" + "="*50)
    print("    LOAN APPLICATION DETAILS")
    print("="*50)
    print(f"Application ID: {loan.get('application_id', 'N/A')}")
    print(f"Name: {loan.get('name', 'N/A')}")
    print(f"Gender: {loan.get('gender', 'N/A')}")
    print(f"Age: {loan.get('age', 'N/A')}")
    print(f"Annual Income: ${loan.get('income', 0):,.2f}")
    print(f"Credit Score: {loan.get('credit_score', 'N/A')}")
    print(f"Employment Status: {loan.get('employment_status', 'N/A')}")
    print(f"Loan Purpose: {loan.get('loan_purpose', 'N/A')}")
    print(f"Requested Amount: ${loan.get('loan_amount', 0):,.2f}")
    print(f"Status: {'APPROVED' if loan.get('approved', False) else 'REJECTED'}")    
    if loan.get('approved', False):
        print(f"Approved Amount: ${loan.get('approved_amount', 0):,.2f}")
        print(f"Interest Rate: {loan.get('interest_rate', 0)}%")
        print(f"Loan Tenure: {loan.get('loan_tenure', 0)} years")
        print(f"Monthly Payment: ${loan.get('monthly_payment', 0):,.2f}")    
    print(f"Reason: {loan.get('reason', 'N/A')}")
    print(f"Application Date: {loan.get('application_date', 'N/A')}")
    print("="*50)
def view_statistics():
    """View loan statistics"""
    print("\n=== Loan Statistics ===")
    loans = load_loans()    
    if not loans:
        print("No loan applications found.")
        return    
    total_applications = len(loans)
    approved_count = sum(1 for loan in loans if loan.get('approved', False))
    rejected_count = total_applications - approved_count    
    approved_amount = sum(loan.get('approved_amount', 0) for loan in loans if loan.get('approved', False))
    total_requested = sum(loan.get('loan_amount', 0) for loan in loans)    
    # Gender statistics
    gender_stats = {}
    for loan in loans:
        gender = loan.get('gender', 'Unknown')
        if gender not in gender_stats:
            gender_stats[gender] = {'total': 0, 'approved': 0, 'rejected': 0}
        gender_stats[gender]['total'] += 1
        if loan.get('approved', False):
            gender_stats[gender]['approved'] += 1
        else:
            gender_stats[gender]['rejected'] += 1   
    print(f"\nTotal Applications: {total_applications}")
    print(f"Approved: {approved_count} ({approved_count/total_applications*100:.1f}%)")
    print(f"Rejected: {rejected_count} ({rejected_count/total_applications*100:.1f}%)")
    print(f"\nTotal Requested Amount: ${total_requested:,.2f}")
    print(f"Total Approved Amount: ${approved_amount:,.2f}")    
    print("\n--- Gender Statistics ---")
    for gender, stats in gender_stats.items():
        approval_rate = (stats['approved'] / stats['total'] * 100) if stats['total'] > 0 else 0
        print(f"\n{gender}:")
        print(f"  Total Applications: {stats['total']}")
        print(f"  Approved: {stats['approved']} ({stats['approved']/stats['total']*100:.1f}%)")
        print(f"  Rejected: {stats['rejected']} ({stats['rejected']/stats['total']*100:.1f}%)")
def search_loans_by_name():
    """Search loans by applicant name"""
    print("\n=== Search Loans by Name ===")
    search_name = input("Enter name to search: ").strip().lower()    
    loans = load_loans()
    matching_loans = [loan for loan in loans if search_name in loan.get('name', '').lower()]    
    if not matching_loans:
        print(f"No applications found for '{search_name}'.")
        return   
    print(f"\nFound {len(matching_loans)} application(s):")
    print("\n" + "-"*80)
    print(f"{'ID':<15} {'Name':<20} {'Gender':<8} {'Amount':<12} {'Status':<10} {'Date':<20}")
    print("-"*80)    
    for loan in matching_loans:
        status = "APPROVED" if loan.get('approved', False) else "REJECTED"
        amount = loan.get('approved_amount', loan.get('loan_amount', 0))
        app_date = loan.get('application_date', 'N/A')
        if len(app_date) > 19:
            app_date = app_date[:19]        
        print(f"{loan.get('application_id', 'N/A'):<15} "
              f"{loan.get('name', 'N/A'):<20} "
              f"{loan.get('gender', 'N/A'):<8} "
              f"${amount:>10,.2f} "
              f"{status:<10} "
              f"{app_date:<20}")
def main_menu():
    """Display main menu and handle user choices"""
    while True:
        print("\n" + "="*40)
        print("    LOAN APPROVAL SYSTEM")
        print("="*40)
        print("1. Apply for Loan")
        print("2. View All Loans")
        print("3. View Loan Details")
        print("4. Search Loans by Name")
        print("5. View Statistics")
        print("6. Exit")
        print("="*40)        
        choice = input("\nEnter your choice (1-6): ").strip()        
        if choice == '1':
            apply_for_loan()
        elif choice == '2':
            view_all_loans()
        elif choice == '3':
            view_loan_details()
        elif choice == '4':
            search_loans_by_name()
        elif choice == '5':
            view_statistics()
        elif choice == '6':
            print("\nThank you for using the Loan Approval System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")
if __name__ == "__main__":
    print("Welcome to the Loan Approval System!")
    main_menu()