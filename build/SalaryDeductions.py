def Loan_Deduction(Loan):
    try:
        Loan = float(Loan)
        return Loan
    except ValueError:
        return "---"

def SSS_Deduction(GrossSalary):
    try: 
        GrossSalary = float(GrossSalary)

        contribution_table = {
            (0, 4249): 570 - 390,
            (4250, 4749): 640 - 437.5,
            (4750, 5249): 710 - 485,
            (5250, 5749): 780 - 532.5,
            (5750, 6249): 850 - 580,
            (6250, 6749): 920 - 627.5,
            (6750, 7249): 990 - 675,
            (7250, 7749): 1060 - 722.5,
            (7750, 8249): 1130 - 770,
            (8250, 8749): 1200 - 817.5,
            (8750, 9249): 1270 - 865,
            (9250, 9749): 1340 - 912.5,
            (9750, 10249): 1410 - 960,
            (10250, 10749): 1480 - 1007.5,
            (10750, 11249): 1550 - 1055,
            (11250, 11749): 1620 - 1102.5,
            (11750, 12249): 1690 - 1150,
            (12250, 12749): 1760 - 1197.5,
            (12750, 13249): 1830 - 1245,
            (13250, 13749): 1900 - 1292.5,
            (13750, 14249): 1970 - 1340,
            (14250, 14749): 2040 - 1387.5,
            (14750, 15249): 2130 - 1455,
            (15250, 15749): 2200 - 1502.5,
            (15750, 16249): 2270 - 1550,
            (16250, 16749): 2340 - 1597.5,
            (16750, 17249): 2410 - 1645,
            (17250, 17749): 2480 - 1692.5,
            (17750, 18249): 2550 - 1720,
            (18250, 18749): 2620 - 1787.5,
            (18750, 19249): 2690 - 1835,
            (19250, 19749): 2760 - 1882.5,
            (19750, 20249): 2830 - 1930,
            (20250, 20749): 2900 - 1977.5,
            (20750, 21249): 2970 - 2025,
            (21250, 21749): 3040 - 2072.5,
            (21750, 22249): 3110 - 2120,
            (22250, 22749): 3180 - 2167.5,
            (22750, 23249): 3250 - 2215,
            (23250, 23749): 3320 - 2262.5,
            (23750, 24249): 3390 - 2310,
            (24250, 24749): 3460 - 2257.5,
            (24750, 25249): 3530 - 2405,
            (25250, 25749): 3600 - 2452.5,
            (25750, 26249): 3670 - 2500,
            (26250, 26749): 3740 - 2547.5,
            (26750, 27249): 3810 - 2595,
            (27250, 27749): 3880 - 2642.5,
            (27750, 28249): 3950 - 2690,
            (28250, 28749): 4020 - 2737.5,
            (28750, 29249): 4090 - 2785,
            (29250, 29749): 4160 - 2832.5,
            (29750, float("inf")): 4230 - 2880
        }

        for salary_range, contribution in contribution_table.items():
            lower, upper = salary_range
            if lower <= GrossSalary <= upper:
                return contribution
            
    except ValueError:
        return "---"

def PhilHealth_Deduction(GrossSalary):
    try:
        GrossSalary = float(GrossSalary)

        if 0 <= GrossSalary <= 10000:
            return 250
        elif 10000 < GrossSalary < 100000:
            return (GrossSalary*0.05)/2
        elif 10000 <= GrossSalary:
            return 2500
        
    except ValueError:
        return "---"

def PagIbig_Deduction(GrossSalary):
    try: 
        GrossSalary = float(GrossSalary)

        if 0 <= GrossSalary <= 1500:
            return "{:.2f}".format(GrossSalary*0.01)
        elif 1501 <= GrossSalary <= 5000:
            return "{:.2f}".format(GrossSalary*0.02)
        elif GrossSalary > 5000:
            return 100
    except ValueError:
        return "---"
    
def IncomeTax_Deduction(GrossSalary, SSS_Deduction, PhilHealth_Deduction, PagIbigDeduction):

    try:
        GrossSalary = float(GrossSalary)
        SSS_Deduction = float(SSS_Deduction)
        PhilHealth_Deduction = float(PhilHealth_Deduction)
        PagIbigDeduction = float(PagIbigDeduction)

        taxableIncome = (GrossSalary - (SSS_Deduction + PhilHealth_Deduction + PagIbigDeduction) )* 12

        if taxableIncome < 250000:
            return 0
        elif 250000 <= taxableIncome < 400000:
            return "{:.2f}".format(((taxableIncome - 250000)*0.15)/12)
        elif 400000 <= taxableIncome < 800000:
            return "{:.2f}".format((22500 + (taxableIncome - 400000)*0.2)/12)
        elif 800000 <= taxableIncome < 2000000:
            return "{:.2f}".format((102500 + (taxableIncome - 800000)*0.25)/12)
        elif 2000000 <= taxableIncome < 8000000:
            return "{:.2f}".format((402500 + (taxableIncome - 2000000)*0.3)/12)
        elif taxableIncome >= 8000000:
            return "{:.2f}".format((2202500 + (taxableIncome - 8000000)*0.35)/12)
        
    except ValueError:
        return "---"

def Total_Deduction(Loan, PagIbig, IncomeTax, SSS, Philhealth):
    try:
        Loan = float(Loan)
        PagIbig = float(PagIbig)
        IncomeTax = float(IncomeTax)
        SSS = float(SSS)
        Philhealth = float(Philhealth)

        return "{:.2f}".format((Loan + PagIbig + IncomeTax + SSS + Philhealth))

    except ValueError:
        return "---"



