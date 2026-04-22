from extract import extract
from transform import transform

def main():
    df = extract()
    df = transform(df)
    print(df.shape)
    print(df.head())

if __name__ == "__main__":
    main()    