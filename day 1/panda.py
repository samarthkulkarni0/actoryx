import pandas as pd
def main():
    try:
        df = pd.read_csv('students.csv')
        print("First 10 records of the student information:")
        print(df.head(10))
    except FileNotFoundError:
        print("The specified file was not found.")
    except pd.errors.EmptyDataError:
        print("The specified file is empty.")
    except pd.errors.ParserError:
        print("Error parsing the CSV file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()