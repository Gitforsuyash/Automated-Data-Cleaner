from src.cleaner import clean_dataset
from src.utils import load_data, save_data

def main():
    df = load_data('data/sample_dirty_data.csv')
    cleaned_df = clean_dataset(df)
    save_data(cleaned_df)
    print("✅ Cleaning complete. Saved to cleaned_data.csv")

if __name__ == '__main__':
    main()
