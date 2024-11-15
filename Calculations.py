def get_probability_curve(dice_count:int, sides:int):
    n = dice_count
    s = sides
    dp = [0] * (n * s + 1)
    for i in range(1, s + 1):
        dp[i] = 1
    
    for dice in range(2, n + 1):
        next_dp = [0] * (n * s + 1)
        for total in range(dice, dice * s + 1):
            for face in range(1, s + 1):
                if total - face > 0:
                    next_dp[total] += dp[total - face]
        dp = next_dp
    
    total_outcomes = s ** n
    probabilities:dict[int, float] = {total: freq / total_outcomes for total, freq in enumerate(dp) if freq > 0}
    return probabilities