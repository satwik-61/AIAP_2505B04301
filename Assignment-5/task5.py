import json
import os
from statistics import mean
# File to store data
DATA_FILE = "scores.json"
def load_data():
    """Load data from file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []
def save_data(data):
    """Save data to file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)
def calculate_score(person_data):
    """
    Calculate score based on features (gender-neutral).
    
    Scoring (total: 100 points):
    - Feature 1: 0-40 points
    - Feature 2: 0-30 points
    - Feature 3: 0-30 points
    
    Note: Gender is NOT used in scoring calculation.
    """
    # Gender is NOT used in any calculations - only features are considered
    score = 0 
    # Feature 1 score (0-40 points)
    feature1 = person_data.get('feature1', 0)
    score += min(max(feature1, 0), 40) 
    # Feature 2 score (0-30 points)
    feature2 = person_data.get('feature2', 0)
    score += min(max(feature2, 0), 30)
    # Feature 3 score (0-30 points)
    feature3 = person_data.get('feature3', 0)
    score += min(max(feature3, 0), 30)
    return round(score, 2)
def add_person():
    """Add a new person with scores"""
    print("\n=== Add Person ===")
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    # Get gender (stored for analysis only, NOT used in scoring)
    print("Gender: 1-Male, 2-Female, 3-Other")
    gender_map = {'1': 'Male', '2': 'Female', '3': 'Other'}
    gender = gender_map.get(input("Select (1-3): ").strip(), 'Other')
    # Get feature scores
    try:
        feature1 = float(input("Feature 1 score (0-40): "))
        feature2 = float(input("Feature 2 score (0-30): "))
        feature3 = float(input("Feature 3 score (0-30): "))
    except ValueError:
        print("Invalid input!")
        return
    # Create person data (gender stored but NOT used in scoring)
    person = {
        'name': name,
        'gender': gender,  # Stored for bias analysis only
        'feature1': feature1,
        'feature2': feature2,
        'feature3': feature3
    }
    # Calculate total score (gender-neutral)
    person['total_score'] = calculate_score(person)
    # Save data
    data = load_data()
    data.append(person)
    save_data(data)
    print(f"\n✓ Person added! Total Score: {person['total_score']}/100")
    print(f"  Score breakdown: Feature1={min(max(feature1,0),40)}, "
          f"Feature2={min(max(feature2,0),30)}, Feature3={min(max(feature3,0),30)}")
def view_all():
    """View all people and their scores"""
    data = load_data()
    if not data:
        print("No data found.")
        return
    data.sort(key=lambda x: x.get('total_score', 0), reverse=True)
    print("\n" + "-"*60)
    print(f"{'Name':<20} {'Gender':<8} {'Score':<8} {'F1':<6} {'F2':<6} {'F3':<6}")
    print("-"*60)
    for person in data:
        print(f"{person.get('name', 'N/A'):<20} {person.get('gender', 'N/A'):<8} "
              f"{person.get('total_score', 0):>7.2f} {person.get('feature1',0):>5.1f} "
              f"{person.get('feature2',0):>5.1f} {person.get('feature3',0):>5.1f}")
def analyze_bias():
    """Analyze gender bias in scoring"""
    data = load_data()
    if not data:
        print("No data found.")
        return
    # Separate by gender
    males = [p for p in data if p.get('gender', '').lower() == 'male']
    females = [p for p in data if p.get('gender', '').lower() == 'female']
    print("\n=== Gender Bias Analysis ===")
    print("Note: Gender is NOT used in score calculation.\n")
    # Calculate statistics
    def get_stats(group, name):
        if not group:
            return None
        scores = [p.get('total_score', 0) for p in group]
        return {
            'name': name,
            'count': len(group),
            'avg_score': mean(scores),
            'min_score': min(scores),
            'max_score': max(scores)
        }
    male_stats = get_stats(males, "Male")
    female_stats = get_stats(females, "Female")
    # Display statistics
    if male_stats:
        print(f"{male_stats['name']} (Count: {male_stats['count']}):")
        print(f"  Average Score: {male_stats['avg_score']:.2f}/100")
        print(f"  Range: {male_stats['min_score']:.2f} - {male_stats['max_score']:.2f}\n")
    if female_stats:
        print(f"{female_stats['name']} (Count: {female_stats['count']}):")
        print(f"  Average Score: {female_stats['avg_score']:.2f}/100")
        print(f"  Range: {female_stats['min_score']:.2f} - {female_stats['max_score']:.2f}\n")
    # Bias detection
    if male_stats and female_stats:
        score_diff = abs(male_stats['avg_score'] - female_stats['avg_score'])
        print(f"Score Difference: {score_diff:.2f} points")
        # Check for potential bias
        if score_diff > 5:
            print("  ⚠️  SIGNIFICANT DIFFERENCE DETECTED!")
            print("     Review if difference is due to legitimate factors.")
        elif score_diff > 2:
            print("  ⚠️  Moderate difference detected.")
        else:
            print("  ✓ No significant bias detected.")
    else:
        print("Cannot analyze - need both male and female data.")
def main():
    """Main menu"""
    while True:
        print("\n" + "="*40)
        print("  GENDER-NEUTRAL SCORING SYSTEM")
        print("="*40)
        print("1. Add Person")
        print("2. View All")
        print("3. Analyze Gender Bias")
        print("4. Exit")
        print("="*40)
        choice = input("\nEnter choice (1-4): ").strip()
        if choice == '1':
            add_person()
        elif choice == '2':
            view_all()
        elif choice == '3':
            analyze_bias()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    print("Welcome to Gender-Neutral Scoring System!")
    print("Scoring is based on features only - Gender is NOT used.")
    main()