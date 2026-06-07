def get_status(gwa):
    if 1.00 <= gwa <= 1.25:
        return "PRESIDENT'S LIST"
    elif 1.26 <= gwa <= 1.75:
        return "DEAN'S LIST"
    else:
        return "GOOD JOB"