def compute_Net_Salary(Gross_Salary, Total_Deduction):
    try:
        Gross_Salary = float(Gross_Salary)
        Total_Deduction = float(Total_Deduction)

        return "{:.2f}".format(Gross_Salary - Total_Deduction)
    
    except ValueError:
        return "---"