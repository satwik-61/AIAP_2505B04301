import json
import os
from datetime import datetime
from statistics import mean, median, stdev
# File to store applicant data
APPLICANTS_FILE = "applicants.json"
def load_applicants():
    """Load applicant data from JSON file"""
    if os.path.exists(APPLICANTS_FILE):
        try:
            with open(APPLICANTS_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []
def save_applicants(applicants):
    """Save applicant data to JSON file"""
    with open(APPLICANTS_FILE, 'w') as f:
        json.dump(applicants, f, indent=2)
def calculate_score(applicant_data):
    """
    Calculate applicant score based on various features.    
    Scoring criteria (total: 100 points):
    - Years of Experience: 0-30 points (1 point per year, max 30)
    - Education Level: 0-25 points
      * High School: 10 points
      * Bachelor's: 15 points
      * Master's: 20 points
      * PhD: 25 points
    - Skills Match: 0-25 points (5 points per matching skill, max 5 skills)
    - Interview Score: 0-20 points (out of 20) 
    Note: Gender is NOT used in scoring - this ensures fairness   """
    # Initialize score
    total_score = 0  
    # 1. Experience Score (0-30 points)
    # 1 point per year of experience, capped at 30 years
    years_experience = applicant_data.get('years_experience', 0)
    experience_score = min(years_experience, 30)
    total_score += experience_score   
    # 2. Education Score (0-25 points)
    # Higher education levels receive higher scores
    education = applicant_data.get('education', '').lower()
    education_scores = {
        'high school': 10,
        "bachelor's": 15,
        "bachelor": 15,
        "master's": 20,
        'master': 20,
        'phd': 25,
        'ph.d': 25,
        'doctorate': 25
    }
    education_score = 0
    for key, value in education_scores.items():
        if key in education:
            education_score = value
            break
    total_score += education_score    
    # 3. Skills Match Score (0-25 points)
    # 5 points per matching skill, maximum 5 skills (25 points total)
    required_skills = applicant_data.get('required_skills', [])
    applicant_skills = applicant_data.get('skills', [])
    
    # Count matching skills
    matching_skills = 0
    for skill in required_skills:
        if skill.lower() in [s.lower() for s in applicant_skills]:
            matching_skills += 1   
    # 5 points per matching skill, max 5 skills
    skills_score = min(matching_skills * 5, 25)
    total_score += skills_score   
    # 4. Interview Score (0-20 points)
    # Interview performance score out of 20
    interview_score = applicant_data.get('interview_score', 0)
    # Ensure interview score is between 0 and 20
    interview_score = max(0, min(interview_score, 20))
    total_score += interview_score  
    # Round to 2 decimal places
    return round(total_score, 2)
def add_applicant():
    """Add a new job applicant"""
    print("\n=== Add Job Applicant ===")    
    # Get applicant information
    name = input("Enter applicant name: ").strip()
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
        years_experience = float(input("Enter years of experience: ").strip())
    except ValueError:
        print("Invalid years of experience!")
        return   
    print("\nEducation Level:")
    print("1. High School")
    print("2. Bachelor's")
    print("3. Master's")
    print("4. PhD")
    edu_choice = input("Select education level (1-4): ").strip()
    edu_map = {'1': "High School", '2': "Bachelor's", '3': "Master's", '4': "PhD"}
    education = edu_map.get(edu_choice, "High School")   
    # Get skills
    print("\nEnter skills (comma-separated, e.g., Python, Java, SQL): ")
    skills_input = input().strip()
    skills = [s.strip() for s in skills_input.split(',') if s.strip()]  
    # Get required skills for the job
    print("\nEnter required skills for the job (comma-separated): ")
    required_skills_input = input().strip()
    required_skills = [s.strip() for s in required_skills_input.split(',') if s.strip()]   
    try:
        interview_score = float(input("Enter interview score (0-20): ").strip())
    except ValueError:
        print("Invalid interview score!")
        return 
    # Create applicant data
    applicant_data = {
        'name': name,
        'gender': gender,
        'years_experience': years_experience,
        'education': education,
        'skills': skills,
        'required_skills': required_skills,
        'interview_score': interview_score,
        'application_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }    
    # Calculate score (gender is NOT used in calculation)
    score = calculate_score(applicant_data)
    applicant_data['score'] = score  
    # Store applicant
    applicants = load_applicants()
    applicants.append(applicant_data)
    save_applicants(applicants) 
    # Display results
    print("\n" + "="*50)
    print("    APPLICANT ADDED SUCCESSFULLY")
    print("="*50)
    print(f"Name: {name}")
    print(f"Gender: {gender}")
    print(f"Total Score: {score}/100")
    print(f"\nScore Breakdown:")
    print(f"  Experience: {min(years_experience, 30)}/30")
    edu_score = 10 if "High School" in education else (15 if "Bachelor" in education else (20 if "Master" in education else 25))
    print(f"  Education: {edu_score}/25")
    matching = sum(1 for s in required_skills if s.lower() in [sk.lower() for sk in skills])
    print(f"  Skills Match: {min(matching * 5, 25)}/25")
    print(f"  Interview: {min(max(interview_score, 0), 20)}/20")
    print("="*50)
def view_all_applicants():
    """View all applicants with their scores"""
    print("\n=== All Applicants ===")
    applicants = load_applicants()   
    if not applicants:
        print("No applicants found.")
        return  
    # Sort by score (descending)
    applicants_sorted = sorted(applicants, key=lambda x: x.get('score', 0), reverse=True)    
    print(f"\nTotal Applicants: {len(applicants_sorted)}")
    print("\n" + "-"*90)
    print(f"{'Name':<20} {'Gender':<8} {'Score':<8} {'Experience':<12} {'Education':<15} {'Interview':<10}")
    print("-"*90) 
    for applicant in applicants_sorted:
        name = applicant.get('name', 'N/A')[:18]
        gender = applicant.get('gender', 'N/A')
        score = applicant.get('score', 0)
        exp = applicant.get('years_experience', 0)
        edu = applicant.get('education', 'N/A')[:13]
        interview = applicant.get('interview_score', 0)      
        print(f"{name:<20} {gender:<8} {score:>7.2f} {exp:>11.1f} {edu:<15} {interview:>9.1f}")
def analyze_gender_bias():
    """Analyze if there is any gender bias in the scoring system"""
    print("\n=== Gender Bias Analysis ===")
    applicants = load_applicants()  
    if not applicants:
        print("No applicants found.")
        return 
    # Separate applicants by gender
    male_applicants = [a for a in applicants if a.get('gender', '').lower() == 'male']
    female_applicants = [a for a in applicants if a.get('gender', '').lower() == 'female']
    other_applicants = [a for a in applicants if a.get('gender', '').lower() == 'other']  
    # Calculate statistics for each gender
    def get_stats(gender_group, gender_name):
        if not gender_group:
            return None       
        scores = [a.get('score', 0) for a in gender_group]
        experiences = [a.get('years_experience', 0) for a in gender_group]
        educations = [a.get('education', '') for a in gender_group]
        interview_scores = [a.get('interview_score', 0) for a in gender_group]        
        return {
            'name': gender_name,
            'count': len(gender_group),
            'avg_score': mean(scores),
            'median_score': median(scores),
            'min_score': min(scores),
            'max_score': max(scores),
            'std_score': stdev(scores) if len(scores) > 1 else 0.0,
            'avg_experience': mean(experiences),
            'avg_interview': mean(interview_scores),
            'education_dist': {}
        }    
    male_stats = get_stats(male_applicants, "Male")
    female_stats = get_stats(female_applicants, "Female")
    other_stats = get_stats(other_applicants, "Other")    
    # Display statistics
    print("\n" + "="*70)
    print("    GENDER-BASED STATISTICS")
    print("="*70)   
    all_stats = [s for s in [male_stats, female_stats, other_stats] if s is not None]  
    for stats in all_stats:
        print(f"\n{stats['name']} Applicants:")
        print(f"  Count: {stats['count']}")
        print(f"  Average Score: {stats['avg_score']:.2f}/100")
        print(f"  Median Score: {stats['median_score']:.2f}/100")
        print(f"  Score Range: {stats['min_score']:.2f} - {stats['max_score']:.2f}")
        print(f"  Standard Deviation: {stats['std_score']:.2f}")
        print(f"  Average Experience: {stats['avg_experience']:.2f} years")
        print(f"  Average Interview Score: {stats['avg_interview']:.2f}/20")   
    # Bias Analysis
    print("\n" + "="*70)
    print("    BIAS ANALYSIS")
    print("="*70)   
    if male_stats and female_stats:
        score_difference = abs(male_stats['avg_score'] - female_stats['avg_score'])
        experience_difference = abs(male_stats['avg_experience'] - female_stats['avg_experience'])     
        print(f"\nScore Comparison (Male vs Female):")
        print(f"  Male Average Score: {male_stats['avg_score']:.2f}")
        print(f"  Female Average Score: {female_stats['avg_score']:.2f}")
        print(f"  Difference: {score_difference:.2f} points")     
        print(f"\nExperience Comparison:")
        print(f"  Male Average Experience: {male_stats['avg_experience']:.2f} years")
        print(f"  Female Average Experience: {female_stats['avg_experience']:.2f} years")
        print(f"  Difference: {experience_difference:.2f} years")    
        # Statistical significance test (simplified)
        # If difference is significant and not explained by legitimate factors
        print(f"\nBias Detection:")  
        bias_found = False
        bias_reasons = []      
        # Check 1: Significant score difference not explained by experience
        if score_difference > 5:  # More than 5 points difference
            experience_impact = abs(experience_difference) * 1  # 1 point per year
            if score_difference > experience_impact + 3:  # Difference beyond experience
                bias_found = True
                bias_reasons.append(f"Significant score difference ({score_difference:.2f} points) not fully explained by experience difference")        
        # Check 2: Similar qualifications but different scores
        if abs(experience_difference) < 2 and score_difference > 3:
            bias_found = True
            bias_reasons.append("Similar experience levels but different average scores")
        
        # Check 3: Interview score differences
        interview_diff = abs(male_stats['avg_interview'] - female_stats['avg_interview'])
        if interview_diff > 2:
            bias_reasons.append(f"Significant interview score difference ({interview_diff:.2f} points)")       
        if bias_found:
            print("  ⚠️  POTENTIAL BIAS DETECTED!")
            for reason in bias_reasons:
                print(f"    - {reason}")
            print("\n  Recommendation: Review scoring criteria and ensure gender-neutral evaluation.")
        else:
            print("  ✓ No significant bias detected based on statistical analysis.")
            if score_difference > 0:
                print(f"  Note: Score difference ({score_difference:.2f} points) appears to be explained by experience/qualifications.")       
        # Additional analysis: Score distribution
        print(f"\nDistribution Analysis:")
        if male_stats['median_score'] > female_stats['median_score'] + 3:
            print("  - Male applicants have higher median scores")
        elif female_stats['median_score'] > male_stats['median_score'] + 3:
            print("  - Female applicants have higher median scores")
        else:
            print("  - Similar median scores between genders")   
    elif male_stats:
        print("\nOnly Male applicants found. Cannot perform bias analysis.")
    elif female_stats:
        print("\nOnly Female applicants found. Cannot perform bias analysis.")
    else:
        print("\nInsufficient data for bias analysis.")   
    print("\n" + "="*70)
    print("NOTE: Gender is NOT used in score calculation.")
    print("Any score differences should be due to experience, education, skills, or interview performance.")
    print("="*70)
def view_detailed_analysis():
    """View detailed breakdown of scores by gender"""
    print("\n=== Detailed Gender Analysis ===")
    applicants = load_applicants()   
    if not applicants:
        print("No applicants found.")
        return   
    # Group by gender
    male_applicants = [a for a in applicants if a.get('gender', '').lower() == 'male']
    female_applicants = [a for a in applicants if a.get('gender', '').lower() == 'female']  
    print("\nScore Component Analysis:")
    print("-"*60) 
    def analyze_components(gender_group, gender_name):
        if not gender_group:
            return  
        print(f"\n{gender_name} Applicants:")
        experiences = [a.get('years_experience', 0) for a in gender_group]
        interview_scores = [a.get('interview_score', 0) for a in gender_group]
        total_scores = [a.get('score', 0) for a in gender_group]
        # Education distribution
        educations = {}
        for a in gender_group:
            edu = a.get('education', 'Unknown')
            educations[edu] = educations.get(edu, 0) + 1 # add 1 to the count of the education          
        print(f"  Average Experience: {mean(experiences):.2f} years")
        print(f"  Average Interview Score: {mean(interview_scores):.2f}/20")
        print(f"  Average Total Score: {mean(total_scores):.2f}/100")
        print(f"  Education Distribution:")
        for edu, count in educations.items():
            print(f"    {edu}: {count}")    
    if male_applicants:
        analyze_components(male_applicants, "Male")
    if female_applicants:
        analyze_components(female_applicants, "Female")
def main_menu():
    """Display main menu and handle user choices"""
    while True:
        print("\n" + "="*40)
        print("    JOB APPLICANT SCORING SYSTEM")
        print("="*40)
        print("1. Add Applicant")
        print("2. View All Applicants")
        print("3. Analyze Gender Bias")
        print("4. Detailed Gender Analysis")
        print("5. Exit")
        print("="*40)       
        choice = input("\nEnter your choice (1-5): ").strip()        
        if choice == '1':
            add_applicant()
        elif choice == '2':
            view_all_applicants()
        elif choice == '3':
            analyze_gender_bias()
        elif choice == '4':
            view_detailed_analysis()
        elif choice == '5':
            print("\nThank you for using the Job Applicant Scoring System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
if __name__ == "__main__":
    print("Welcome to the Job Applicant Scoring System!")
    print("This system evaluates applicants based on:")
    print("  - Experience (0-30 points)")
    print("  - Education (0-25 points)")
    print("  - Skills Match (0-25 points)")
    print("  - Interview Score (0-20 points)")
    print("\nNote: Gender is NOT used in scoring to ensure fairness.")
    main_menu()