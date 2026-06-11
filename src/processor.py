def process_batch(values):
    total = sum(values)
    count = len(values)

    average = total / count

    return {
        "count": count,
        "average": average
    }
