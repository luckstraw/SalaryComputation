def compute_Gross_Salary(rate_pr_hr, hr_pr_day, OT_hr, absence, day_pr_mnth):
    try:
        rate_pr_hr = float(rate_pr_hr)
        hr_pr_day = float(hr_pr_day)
        OT_hr = float(OT_hr)
        absence = float(absence)
        day_pr_mnth = float(day_pr_mnth)

        total_hrs_pr_month = ((day_pr_mnth - absence)*hr_pr_day) + OT_hr
        
        return "{:.2f}".format(total_hrs_pr_month*rate_pr_hr)
    
    except ValueError:
        return "---"