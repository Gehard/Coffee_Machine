def get_bonus(salary, percentage=35):
    bonus = (percentage / 100) * salary
    return int(bonus)
