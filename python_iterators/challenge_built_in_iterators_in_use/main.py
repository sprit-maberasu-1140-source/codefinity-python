def format_scores(names, scores):
    return [f"{idx}. {name} scored {score}" for idx, (name, score) in enumerate(zip(names, scores), start=1)]

result = format_scores(["Alice", "Bob", "Charlie"], [85, 92, 78])
print(result)