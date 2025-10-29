import pandas as pd

def analyze_csv(file_path):
    try:
        # Read the CSV file using pandas
        df = pd.read_csv(file_path)
        
        # Calculate statistics for each numerical column
        for column in df.select_dtypes(include=['int64', 'float64']):
            print(f"\nAnalysis for {column}:")
            print(f"Mean: {df[column].mean():.2f}")
            print(f"Minimum: {df[column].min()}")
            print(f"Maximum: {df[column].max()}")
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Specify the path to your CSV file
    csv_file = "sample_data.csv"
    analyze_csv(csv_file)
