import GrossSalary
import SalaryDeductions
import NetSalary

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Frame, StringVar

import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\avile\Desktop\BEMBEM\VSCode\Python\SalaryComputation\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def toggle_details():
    if details_frame.winfo_viewable():
        details_frame.place_forget()
    else:
        details_frame.place(x=0, y=0)

def update_Gross_Salary(*args):
    Gross_Salary = GrossSalary.compute_Gross_Salary(
        rate_of_pay_var.get(),
        work_hr_var.get(),
        ot_hrs_var.get(),
        absence_var.get(),
        workingday_var.get()
    )
    Gross_Salary_var.set(Gross_Salary)
    canvas.itemconfig(Gross_Salary_text, text=Gross_Salary_var.get())

def update_Loan_Deduction(*args):
    loan_deduction = SalaryDeductions.Loan_Deduction(loan_var.get())
    loan_var2.set(loan_deduction)
    details_canva.itemconfig(loan_text, text=loan_var2.get())

def update_PagIbig_Deduction(*args):
    if not checkbox_varPagibig.get():
        PagIbig_Deduction = 0
    else:
        PagIbig_Deduction = SalaryDeductions.PagIbig_Deduction(
            Gross_Salary_var.get()
        )
        
    PagIbig_Deduction_var.set(PagIbig_Deduction)
    details_canva.itemconfig(PagIbig_Deduction_text, text=PagIbig_Deduction_var.get())

def update_Tax_Deduction(*args):
    Tax_Deduction = SalaryDeductions.IncomeTax_Deduction(
        Gross_Salary_var.get(),
        SSS_Deduction_var.get(),
        PhilHealth_Deduction_var.get(),
        PagIbig_Deduction_var.get(),
    )
    Tax_Deduction_var.set(Tax_Deduction)
    details_canva.itemconfig(Tax_Deduction_text, text=Tax_Deduction_var.get())

def update_SSS_Deduction(*args):
    if not checkbox_varGsis.get():
        SSS_Deduction = 0
    else:
        SSS_Deduction = SalaryDeductions.SSS_Deduction(
            Gross_Salary_var.get()
        )
    
    SSS_Deduction_var.set(SSS_Deduction)
    details_canva.itemconfig(SSS_Deduction_text, text=SSS_Deduction_var.get())

def update_PhilHealth_Deduction(*args):
    if not checkbox_varPhilhealth.get():
        PhilHealth_Deduction = 0
    else:
        PhilHealth_Deduction = SalaryDeductions.PhilHealth_Deduction(
            Gross_Salary_var.get()
        )
        
    PhilHealth_Deduction_var.set(PhilHealth_Deduction)
    details_canva.itemconfig(PhilHealth_Deduction_text, text=PhilHealth_Deduction_var.get())

def update_Total_Deduction(*args):
    Total_Deduction = SalaryDeductions.Total_Deduction(
        loan_var.get(),
        PagIbig_Deduction_var.get(),
        Tax_Deduction_var.get(),
        SSS_Deduction_var.get(),
        PhilHealth_Deduction_var.get()
    )
    Total_Deduction_var.set(Total_Deduction)
    details_canva.itemconfig(Total_Deduction_text, text=Total_Deduction_var.get())
    canvas.itemconfig(Deduction_text, text=Total_Deduction_var.get())

def update_Net_Salary(*args):
    Net_Salary = NetSalary.compute_Net_Salary(
        Gross_Salary_var.get(),
        Total_Deduction_var.get()
    )
    Net_Salary_var.set(Net_Salary)
    canvas.itemconfig(Net_Salary_text, text=Net_Salary_var.get())

window = Tk()

window.geometry("556x377")
window.configure(bg = "#F4EEEE")

Gross_Salary_var = StringVar()
Gross_Salary_var.trace_add("write", update_SSS_Deduction)
Gross_Salary_var.trace_add("write", update_PhilHealth_Deduction)
Gross_Salary_var.trace_add("write", update_PagIbig_Deduction)
Gross_Salary_var.trace_add("write", update_Tax_Deduction)
Gross_Salary_var.trace_add("write", update_Net_Salary)

loan_var = StringVar()
loan_var.trace_add("write", update_Loan_Deduction)
loan_var.trace_add("write", update_Total_Deduction)
loan_var2 = StringVar() #Solution to bug lol

PagIbig_Deduction_var = StringVar()
PagIbig_Deduction_var.trace_add("write", update_Tax_Deduction)
PagIbig_Deduction_var.trace_add("write", update_Total_Deduction)

Tax_Deduction_var = StringVar()
Tax_Deduction_var.trace_add("write", update_Total_Deduction)

SSS_Deduction_var = StringVar()
SSS_Deduction_var.trace_add("write", update_Tax_Deduction)
SSS_Deduction_var.trace_add("write", update_Total_Deduction)

PhilHealth_Deduction_var = StringVar()
PhilHealth_Deduction_var.trace_add("write", update_Tax_Deduction)
PhilHealth_Deduction_var.trace_add("write", update_Total_Deduction)

Total_Deduction_var = StringVar()
Total_Deduction_var.trace_add("write", update_Net_Salary)

Net_Salary_var = StringVar()

name_var = StringVar()

workingday_var = StringVar()
workingday_var.trace_add("write", update_Gross_Salary)

rate_of_pay_var = StringVar()
rate_of_pay_var.trace_add("write", update_Gross_Salary)

work_hr_var = StringVar()
work_hr_var.trace_add("write", update_Gross_Salary)

ot_hrs_var = StringVar()
ot_hrs_var.trace_add("write", update_Gross_Salary)

absence_var = StringVar()
absence_var.trace_add("write", update_Gross_Salary)

checkbox_varGsis = tk.BooleanVar()
checkbox_varGsis.trace_add("write", update_SSS_Deduction)

checkbox_varPagibig = tk.BooleanVar()
checkbox_varPagibig.trace_add("write", update_PagIbig_Deduction)

checkbox_varPhilhealth = tk.BooleanVar()
checkbox_varPhilhealth.trace_add("write", update_PhilHealth_Deduction)


canvas = Canvas(
    window,
    bg = "#F4EEEE",
    height = 377,
    width = 556,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)


#-------GROSS SALARY-----
image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    107.0,
    65.0,
    image=image_image_4
)
canvas.create_text(
    46.0,
    34.0,
    anchor="nw",
    text="Gross Salary",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
Gross_Salary_text = canvas.create_text(
    69.0,
    52.0,
    anchor="nw",
    text="---",      # <<< GROSS SALARY VALUE (just a place holder)
    fill="#000000",
    font=("Outfit Bold", 24 * -1)
)
canvas.create_text(
    47.0,
    52.0,
    anchor="nw",
    text="₱",
    fill="#000000",
    font=("Outfit Bold", 24 * -1)
)
#-------END OF GROSS SALARY-----


#-------DEDUCTIONS------------
image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    278.0,
    65.0,
    image=image_image_3
)

canvas.create_text(
    218.0,
    34.0,
    anchor="nw",
    text="Deductions",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
canvas.create_text(
    219.0,
    52.0,
    anchor="nw",
    text="₱",
    fill="#FF5757",
    font=("Outfit Bold", 24 * -1)
)
Deduction_text = canvas.create_text(
    241.0,
    52.0,
    anchor="nw",
    text="---",     # <<< DEDUCTION VALUE (placeholder)
    fill="#FF5757",
    font=("Outfit Bold", 24 * -1)
)


#------SEE DETAILS INSIDE DEDUCTIONS------------
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
detailbtn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=toggle_details,
    relief="flat"
)
detailbtn.place(
    x=218.0,
    y=85.0,
    width=120.0,
    height=41.0
)

details_frame = Frame(
    window,
    bg = "#F4EEEE",
    height = 139,
    width = 556,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
details_frame.place(x=0, y=0)

image_image_1 = PhotoImage(
    file=relative_to_assets("bgframe.png"))
image_1 = canvas.create_image(
    278.0,
    72.0,
    image=image_image_1
)

details_frame.place_forget()

#------------- CANVA INSIDE SEE DETAIL FRAME (See Detail Button)--------------

details_canva = Canvas(
    details_frame,
    bg = "#F4EEEE",
    height = 139,
    width = 556,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
details_canva.place(x = 0, y = 0)

image_image_1 = PhotoImage(
    file=relative_to_assets("bgframe.png"))
image_1 = details_canva.create_image(
    278.0,
    72.0,
    image=image_image_1
)

#--------Text like "SSS","Loan" after you click "see details"------
details_canva.create_text(
    64.0,
    21.0,
    anchor="nw",
    text="Loan",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
details_canva.create_text(
    41.0,
    43.0,
    anchor="nw",
    text="₱",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)
loan_text = details_canva.create_text(
    55.0,
    43.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)

details_canva.create_text(
    252.0,
    21.0,
    anchor="nw",
    text="PAG-IBIG",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
details_canva.create_text(
    224.0,
    43.0,
    anchor="nw",
    text="₱",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)
PagIbig_Deduction_text = details_canva.create_text(
    238.0,
    43.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)

details_canva.create_text(
    450.0,
    21.0,
    anchor="nw",
    text="Tax",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
details_canva.create_text(
    404.0,
    43.0,
    anchor="nw",
    text="₱",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)
Tax_Deduction_text = details_canva.create_text(
    418.0,
    43.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)

details_canva.create_rectangle(
    40.0,
    70.99998899175588,
    516.0,
    72.00003051757812,
    fill="#CFCFCF",
    outline=""
)

details_canva.create_text(
    56.0,
    77.0,
    anchor="nw",
    text="SSS/GSIS",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
details_canva.create_text(
    41.0,
    96.0,
    anchor="nw",
    text="₱",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)
SSS_Deduction_text = details_canva.create_text(
    56.0,
    96.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)

details_canva.create_text(
    252.0,
    77.0,
    anchor="nw",
    text="PhilHealth",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
details_canva.create_text(
    224.0,
    96.0,
    anchor="nw",
    text="₱",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)
PhilHealth_Deduction_text = details_canva.create_text(
    239.0,
    96.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Outfit Bold", 16 * -1)
)

details_canva.create_text(
    448.0,
    77.0,
    anchor="nw",
    text="Total",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
details_canva.create_text(
    404.0,
    96.0,
    anchor="nw",
    text="₱",
    fill="#FF5757",
    font=("Outfit Bold", 16 * -1)
)
Total_Deduction_text = details_canva.create_text(
    418.0,
    96.0,
    anchor="nw",
    text="---",
    fill="#FF5757",
    font=("Outfit Bold", 16 * -1)
)

#----x button after you click "see details"-----------
xbuttonimg= PhotoImage(
    file=relative_to_assets("xbutton.png"))
xbutton = Button(
    details_canva,
    image=xbuttonimg,
    borderwidth=0,
    highlightthickness=0,
    command=toggle_details,
    relief="flat"
)
xbutton.place(
    x=516.0,
    y=21.0,
    width=16.0,
    height=16.0
)
#-------------------END OF DEDUCTIONS ----------------


#-------------------NET SALARY------------------------
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    448.0,
    65.0,
    image=image_image_2
)

canvas.create_text(
    389.0,
    34.0,
    anchor="nw",
    text="Net Salary",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
canvas.create_text(
    390.0,
    52.0,
    anchor="nw",
    text="₱",
    fill="#000000",
    font=("Outfit Bold", 24 * -1)
)
Net_Salary_text = canvas.create_text(
    412.0,
    52.0,
    anchor="nw", 
    text="---",     # <<< NET SALARY VALUE (placeholder)
    fill="#000000",
    font=("Outfit Bold", 24 * -1)
)
#---------END OF NET SALARY---------------------------


#-------Upper part------------
canvas.create_text(
    46.0,
    140.0,
    anchor="nw",
    text="Name",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
name = Entry(
    window,
    textvariable = name_var,
    bd=0,
    bg="#F4EEEE",
    fg="#000716",
    highlightthickness=0,
    font=("Outfit Bold", 19 * -1)
)
name.place(
    x=59.0,
    y=162.0,
    width=250.0,
    height=22.0
)

canvas.create_text(
    432.0,
    140.0,
    anchor="nw",
    text="Working Days",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
workingday = Entry(
    window,
    textvariable=workingday_var,
    bd=0,
    bg="#F4EEEE",
    fg="#000716",
    highlightthickness=0,
    font=("Outfit Bold", 19 * -1)
)
workingday.place(
    x=445.0,
    y=162.0,
    width=25.0,
    height=22.0
)
canvas.create_text(
    478.0,
    162.0,
    anchor="nw",
    text="/month",
    fill="#545454",
    font=("Outfit Bold", 16 * -1)
)

canvas.create_rectangle(
    40.0,
    190.00000425054495,
    516.0,
    191.0000457763672,
    fill="#CFCFCF",
    outline=""
)
#------------------------------


#------Lower part-------------
canvas.create_text(
    49.0,
    218.0,
    anchor="nw",
    text="Rate of Pay",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
canvas.create_text(
    45.0,
    243.0,
    anchor="nw",
    text="₱",
    fill="#545454",
    font=("Outfit Bold", 16 * -1)
)
rate_of_pay = Entry(
    window,
    textvariable=rate_of_pay_var,
    bd=0,
    bg="#F4EEEE",
    fg="#000716",
    highlightthickness=0,
    font=("Outfit Bold", 19 * -1),
    justify="center"
)
rate_of_pay.place(
    x=58.0,
    y=243.0,
    width=50.0,
    height=18.0
)
canvas.create_text(
    110.0,
    243.0,
    anchor="nw",
    text="/hr",
    fill="#545454",
    font=("Outfit Bold", 16 * -1)
)

canvas.create_text(
    175.0,
    218.0,
    anchor="nw",
    text="Work Hours",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
work_hr = Entry(
    window,
    textvariable=work_hr_var,
    bd=0,
    bg="#F4EEEE",
    fg="#000716",
    highlightthickness=0,
    font=("Outfit Bold", 19 * -1),
    justify="center"
)
work_hr.place(
    x=179.0,
    y=243.0,
    width=37.0,
    height=18.0
)
canvas.create_text(
    220.0,
    243.0,
    anchor="nw",
    text="hr/day",
    fill="#545454",
    font=("Outfit Bold", 16 * -1)
)

canvas.create_text(
    304.0,
    218.0,
    anchor="nw",
    text="Total OT Hours",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
ot_hrs = Entry(
    window,
    textvariable=ot_hrs_var,
    bd=0,
    bg="#F4EEEE",
    fg="#000716",
    highlightthickness=0,
    font=("Outfit Bold", 19 * -1),
    justify="center"
)
ot_hrs.place(
    x=312.0,
    y=243.0,
    width=37.0,
    height=18.0
)
canvas.create_text(
    353.0,
    243.0,
    anchor="nw",
    text="hr(s)",
    fill="#545454",
    font=("Outfit Bold", 16 * -1)
)

canvas.create_text(
    431.0,
    218.0,
    anchor="nw",
    text="Days of Absence",
    fill="#545454",
    font=("Outfit Bold", 10 * -1)
)
absence = Entry(
    window,
    textvariable=absence_var,
    bd=0,
    bg="#F4EEEE",
    fg="#000716",
    highlightthickness=0,
    font=("Outfit Bold", 19 * -1),
    justify="center"
)
absence.place(
    x=436.0,
    y=243.0,
    width=37.0,
    height=18.0
)
canvas.create_text(
    478.0,
    243.0,
    anchor="nw",
    text="day(s)",
    fill="#545454",
    font=("Outfit Bold", 16 * -1)
)

canvas.create_rectangle(
    40.0,
    269.99998899175586,
    516.0,
    271.0000305175781,
    fill="#CFCFCF",
    outline=""
)
#----------------------------

#--------YELLOW RECTANGLE AT THE BOTTOM
botimage = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    279.0,
    335.0,
    image=botimage
)

canvas.create_text(
    70.0,
    306.0,
    anchor="nw",
    text="Loan per Month",
    fill="#000000",
    font=("Outfit Bold", 10 * -1)
)
loan = Entry(
    window,
    textvariable=loan_var,
    bd=0,
    bg="#FFDE59",
    fg="#FF5757",
    highlightthickness=0,
    font=("Outfit Bold", 16 * -1),
    justify='left'
)
loan.place(
    x=62.0,
    y=328.0,
    width=110.0,
    height=16.0
)
canvas.create_text(
    47.0,
    327.0,
    anchor="nw",
    text="₱",
    fill="#FF5757",
    font=("Outfit Bold", 16 * -1)
)

canvas.create_text(
    205.0,
    306.0,
    anchor="nw",
    text="SSS/GSIS",
    fill="#000000",
    font=("Outfit Bold", 10 * -1)
)
checkboxGsis = tk.Checkbutton(window,variable=checkbox_varGsis)
checkboxGsis.place(
    x=220.0, 
    y=330.0,
    width=15.0, 
    height=15.0
)

canvas.create_text(
    329.0,
    306.0,
    anchor="nw",
    text="PAG-IBIG",
    fill="#000000",
    font=("Outfit Bold", 10 * -1)
)
checkboxPagibig = tk.Checkbutton(window,variable=checkbox_varPagibig)
checkboxPagibig.place(
    x=342.0,
    y=330.0,
    width=15.0,
    height=15.0,
)

canvas.create_text(
    447.0,
    306.0,
    anchor="nw",
    text="PhilHealth",
    fill="#000000",
    font=("Outfit Bold", 10 * -1)
)
checkboxPhilhealth = tk.Checkbutton(window,variable=checkbox_varPhilhealth)
checkboxPhilhealth.place(
    x=460.0,
    y=330.0,
    width=15.0,
    height=15.0,
)

canvas.create_rectangle(
    40.0,
    352.9999889917559,
    516.0,
    354.0000305175781,
    fill="#FFFFFF",
    outline=""
)
#--------------------------------

window.resizable(False, False)
window.mainloop()

