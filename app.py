import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Scam-O-Meter")
root.geometry("900x550")
root.config(bg="black")

score = 0
sec = 600

def update_score(points, label, color):
    global score
    score += points
    if score > 92: score = 92
    label.config(bg=color, fg="white" if color=="red" else "black")
    score_text.config(text=f"SCORE: {score}/100")
    if score >= 70:
        final_text.config(text="⛔ 92% SCAM - BHAG JAO!")
    root.bell()

def check_timer(): update_score(30, b1, "red")
def check_fee(): 
    update_score(25, b2, "orange")
    messagebox.showinfo("Hidden Fee", "Rs.499 extra charge pakda gaya!")
def check_review(): update_score(25, b3, "red")
def check_guilt(): update_score(12, b4, "orange")

# TIMER
def run_timer():
    global sec
    sec -= 1
    if sec < 0: sec = 600
    m, s = divmod(sec, 60)
    timer.config(text=f"Offer ends in: {m:02d}:{s:02d}")
    root.after(1000, run_timer)

# LEFT SIDE
left = tk.Frame(root, bg="white", padx=20, pady=20)
left.pack(side="left", fill="both", expand=True)

tk.Label(left, text="🔥 SNEAKR.PK - 90% OFF", bg="white", font=("Arial",14,"bold")).pack()
tk.Label(left, text="Air Jordan - Rs.4,999", bg="white", font=("Arial",14)).pack(pady=5)
timer = tk.Label(left, text="Offer ends in: 10:00", bg="white", fg="red", font=("Arial",12,"bold"))
timer.pack()

tk.Label(left, text="⭐ Ayesha K. - Best ever!\n⭐ Ali R. - Best ever!\n⭐ Ayesha K. - Best ever!", bg="white", justify="left").pack(pady=10)
tk.Checkbutton(left, text="Add Rs.499 Insurance", bg="white").pack()
tk.Button(left, text="BUY NOW", bg="green", fg="white", width=20, command=check_fee).pack(pady=10)

run_timer()

# RIGHT SIDE
right = tk.Frame(root, bg="#111", padx=20, pady=20)
right.pack(side="right", fill="both", expand=True)

tk.Label(right, text="🛡️ SCAM-O-METER", bg="#111", fg="white", font=("Arial",14,"bold")).pack()
score_text = tk.Label(right, text="SCORE: 0/100", bg="#111", fg="white", font=("Arial",18,"bold"))
score_text.pack(pady=10)

b1 = tk.Label(right, text="🔴 Fake Timer", bg="#333", fg="white", pady=10); b1.pack(fill="x", pady=5)
b2 = tk.Label(right, text="🟡 Hidden Fee", bg="#333", fg="white", pady=10); b2.pack(fill="x", pady=5)
b3 = tk.Label(right, text="🔴 Fake Reviews", bg="#333", fg="white", pady=10); b3.pack(fill="x", pady=5)
b4 = tk.Label(right, text="🟡 Guilt Popup", bg="#333", fg="white", pady=10); b4.pack(fill="x", pady=5)

final_text = tk.Label(right, text="", bg="#111", fg="red", font=("Arial",12,"bold")); final_text.pack(pady=15)

tk.Button(right, text="Press T - Timer", command=check_timer).pack(fill="x")
tk.Button(right, text="Press H - Hidden Fee", command=check_fee).pack(fill="x")
tk.Button(right, text="Press R - Reviews", command=check_review).pack(fill="x")
tk.Button(right, text="Press G - Guilt", command=check_guilt).pack(fill="x")

root.bind('t', lambda e: check_timer())
root.bind('h', lambda e: check_fee())
root.bind('r', lambda e: check_review())
root.bind('g', lambda e: check_guilt())

root.mainloop()
