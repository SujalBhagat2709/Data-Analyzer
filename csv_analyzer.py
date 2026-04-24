import csv
from stats import calculate_stats

def analyze_csv(file_path, column_index=0):
    
    values = []
    
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        
        for row in reader:
            try:
                values.append(float(row[column_index]))
            except:
                continue
    
    return calculate_stats(values)


if __name__ == "__main__":
    
    result = analyze_csv("data.csv", 0)
    
    print(result)