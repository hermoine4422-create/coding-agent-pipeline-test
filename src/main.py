from processor import process_batch

def main():
    batches = [
        [10, 20, 30],
        [],
        [5, 15, 25]
    ]

    for batch in batches:
        result = process_batch(batch)
        print(result)

if __name__ == "__main__":
    main()
