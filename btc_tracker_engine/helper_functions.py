def rate_diff_percentage(previous_rate, current_rate, percentage=False):
    diff_percentage = (current_rate - previous_rate) / previous_rate
    if percentage:
        return diff_percentage * 100
    return diff_percentage