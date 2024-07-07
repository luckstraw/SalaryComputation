def toggle_details():
    if details_frame.winfo_viewable():
        details_frame.place_forget()
    else:
        details_frame.place(x=0, y=0)