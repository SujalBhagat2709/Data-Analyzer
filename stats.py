def calculate_stats(numbers):
    
    total = sum(numbers)
    count = len(numbers)
    mean = total / count if count > 0 else 0
    
    return {
        "sum": total,
        "count": count,
        "mean": mean
    }


if __name__ == "__main__":
    
    data = [10, 20, 30, 40]
    
    result = calculate_stats(data)
    
    print(result)