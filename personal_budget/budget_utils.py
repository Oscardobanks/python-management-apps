def group_by_category(transactions):
    grouped = {}
    for t in transactions:
        grouped.setdefault(t.category, []).append(t)
    return grouped


def calculate_totals(transactions):
    totals = {}
    for t in transactions:
        totals[t.category] = totals.get(t.category, 0) + t.amount
    return totals
