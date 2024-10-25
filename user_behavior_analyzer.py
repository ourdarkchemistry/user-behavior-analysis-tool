import pandas as pd
import sys
import matplotlib.pyplot as plt

def load_user_data(file):
    try:
        return pd.read_csv(file)
    except Exception as e:
        print(f"Error loading user data file: {e}")
        return None

def analyze_user_behavior(df):
    # Подсчет активности пользователей
    user_activity = df['user_id'].value_counts()
    
    # Вывод результатов
    print("User activity count:")
    print(user_activity)
    
    # Визуализация активности
    plt.figure(figsize=(10, 5))
    user_activity.plot(kind='bar', color='green')
    plt.xlabel('User ID')
    plt.ylabel('Activity Count')
    plt.title('User Activity Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    if len(sys.argv) < 3 or sys.argv[1] != '--file':
        print("Usage: python user_behavior_analyzer.py --file <path_to_user_activity_file>")
        return

    file = sys.argv[2]
    df = load_user_data(file)

    if df is not None:
        print("Analyzing user behavior...")
        analyze_user_behavior(df)

if __name__ == "__main__":
    main()
