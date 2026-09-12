import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Scam-O-Meter")
root.geometry("1400x800")
root.config(bg="#1a1a1a")

score = 0
sec = 600
detected_scams = []

def update_score(points, label, color, scam_name):
    global score
    score += points
    if score > 100: score = 100
    label.config(bg=color, fg="white")
    score_text.config(text=f"SCORE: {score}/100")
    detected_scams.append(scam_name)
    
    if score >= 90:
        final_text.config(text="⛔ MAJOR SCAM DETECTED!", fg="#ff0000")
    elif score >= 70:
        final_text.config(text="⚠️ HIGH SCAM RISK!", fg="#ff6600")
    elif score >= 50:
        final_text.config(text="⚠️ MEDIUM SCAM RISK", fg="#ffaa00")
    
    root.bell()
    update_detected_list()

def check_visa(): 
    update_score(25, b1, "red", "Free Work Visa Promise")
    messagebox.showinfo("SCAM ALERT", "❌ FAKE VISA PROMISE\nNo one offers free work visas!\nThey charge thousands!")

def check_visa_reviews(): 
    update_score(20, b1b, "orange", "Fake Visa Reviews")
    messagebox.showinfo("SCAM ALERT", "❌ FAKE REVIEWS DETECTED\nThese are copy-paste testimonials!")

def check_lottery(): 
    update_score(25, b2, "red", "Free Lottery Winnings")
    messagebox.showinfo("SCAM ALERT", "❌ FAKE LOTTERY\nYou didn't enter any lottery!\nThis is 100% fraud!")

def check_lottery_reviews(): 
    update_score(20, b2b, "orange", "Fake Lottery Reviews")
    messagebox.showinfo("SCAM ALERT", "❌ FAKE REVIEWS DETECTED\nNo real winners here!")

def check_inheritance(): 
    update_score(25, b3, "red", "Fake Inheritance Claims")
    messagebox.showinfo("SCAM ALERT", "❌ FAKE INHERITANCE\nYou have no unknown relatives!\nThis is a money laundering scheme!")

def check_inheritance_reviews(): 
    update_score(20, b3b, "orange", "Fake Inheritance Reviews")
    messagebox.showinfo("SCAM ALERT", "❌ FAKE REVIEWS DETECTED\nThese people don't exist!")

def check_loan(): 
    update_score(25, b4, "red", "Guaranteed Easy Loan")
    messagebox.showinfo("SCAM ALERT", "❌ FAKE LOAN GUARANTEE\nNo one guarantees loans without credit check!\nThey'll steal your data!")

def check_loan_reviews(): 
    update_score(20, b4b, "orange", "Fake Loan Reviews")
    messagebox.showinfo("SCAM ALERT", "❌ FAKE REVIEWS DETECTED\nBots posing as customers!")

def detect_scam():
    if len(detected_scams) == 0:
        result = "No scams detected yet. Try clicking on the scam indicators!"
        color = "#00ff00"
        emoji = "✅"
    elif len(detected_scams) >= 8:
        result = f"MASSIVE SCAM DETECTED!\n{len(detected_scams)}/8 Scam Indicators Found!\n❌ DO NOT PROCEED"
        color = "#ff0000"
        emoji = "⛔"
    elif len(detected_scams) >= 5:
        result = f"HIGH SCAM RISK!\n{len(detected_scams)}/8 Indicators Found\n⚠️ STAY AWAY!"
        color = "#ff6600"
        emoji = "⚠️"
    else:
        result = f"Medium Risk Detected\n{len(detected_scams)}/8 Indicators Found\n⚠️ BE CAREFUL"
        color = "#ffaa00"
        emoji = "⚠️"
    
    result_label.config(text=f"{emoji}\n{result}", bg="#222", fg=color, font=("Arial", 16, "bold"))
    messagebox.showwarning("SCAM ANALYSIS RESULT", f"{emoji} {result}")

def update_detected_list():
    detected_text = "SCAMS DETECTED:\n" + "\n".join([f"• {scam}" for scam in detected_scams]) if detected_scams else "SCAMS DETECTED:\nNone yet..."
    detected_label.config(text=detected_text)

def reset_scam():
    global score, detected_scams, sec
    score = 0
    detected_scams = []
    sec = 600
    score_text.config(text="SCORE: 0/100")
    final_text.config(text="")
    result_label.config(text="Click DETECT SCAM to analyze")
    detected_label.config(text="SCAMS DETECTED:\nNone yet...")
    update_detected_list()

# TIMER
def run_timer():
    global sec
    sec -= 1
    if sec < 0: sec = 600
    m, s = divmod(sec, 60)
    timer.config(text=f"⏱️ Offer ends in: {m:02d}:{s:02d}")
    root.after(1000, run_timer)

# ===== LEFT SIDE - FAKE PRODUCT/OFFER =====
left = tk.Frame(root, bg="#ffffff", padx=25, pady=25)
left.pack(side="left", fill="both", expand=True)

# Header
header = tk.Label(left, text="💼 WORK ABROAD AGENCY", bg="#ffffff", font=("Arial", 20, "bold"), fg="#000080")
header.pack()

subtitle = tk.Label(left, text="FREE WORK VISA TO CANADA", bg="#ffffff", font=("Arial", 16, "bold"), fg="#cc0000")
subtitle.pack(pady=5)

price = tk.Label(left, text="Limited Time Offer - Only Rs. 0!", bg="#ffffff", font=("Arial", 14, "bold"), fg="#00aa00")
price.pack(pady=3)

timer = tk.Label(left, text="⏱️ Offer ends in: 10:00", bg="#ffffff", fg="#cc0000", font=("Arial", 13, "bold"))
timer.pack(pady=10)

# Separator
tk.Label(left, text="─" * 40, bg="#ffffff", fg="#cccccc").pack()

# Reviews Section
review_title = tk.Label(left, text="⭐ CLIENT TESTIMONIALS", bg="#ffffff", font=("Arial", 12, "bold"), fg="#000000")
review_title.pack(pady=10)

reviews_text = """⭐⭐⭐⭐⭐ Ayesha K. - "Best ever! Got visa immediately!"
⭐⭐⭐⭐⭐ Ali R. - "Life changing! Now in Canada!"
⭐⭐⭐⭐⭐ Maria S. - "Amazing service! Highly recommend!"
⭐⭐⭐⭐⭐ Hassan M. - "Best decision ever made!"
⭐⭐⭐⭐⭐ Fatima A. - "Got job offer same day!"
"""

reviews = tk.Label(left, text=reviews_text, bg="#f0f0f0", font=("Arial", 11), justify="left", padx=10, pady=8)
reviews.pack(fill="x", pady=5)

# Separator
tk.Label(left, text="─" * 40, bg="#ffffff", fg="#cccccc").pack(pady=5)

# Checkbox
tk.Checkbutton(left, text="✓ I agree to pay Rs.50,000 processing fee", bg="#ffffff", font=("Arial", 11)).pack(pady=5)

# Call to Action Button
cta_button = tk.Button(left, text="🎯 APPLY NOW FOR FREE VISA", bg="#00aa00", fg="white", 
                       width=30, font=("Arial", 14, "bold"), command=check_visa)
cta_button.pack(pady=15)

run_timer()

# ===== RIGHT SIDE - SCAM DETECTOR =====
right = tk.Frame(root, bg="#1a1a1a", padx=25, pady=25)
right.pack(side="right", fill="both", expand=True)

# Title
title = tk.Label(right, text="🛡️ SCAM-O-METER 3000", bg="#1a1a1a", fg="#00ff00", font=("Arial", 22, "bold"))
title.pack()

# Score Display
score_text = tk.Label(right, text="SCORE: 0/100", bg="#1a1a1a", fg="#00ff00", font=("Arial", 32, "bold"))
score_text.pack(pady=15)

# Scam Indicators
indicators_frame = tk.Frame(right, bg="#1a1a1a")
indicators_frame.pack(fill="x", pady=10)

tk.Label(indicators_frame, text="SCAM INDICATORS:", bg="#1a1a1a", fg="#ffff00", font=("Arial", 13, "bold")).pack(anchor="w")

scams_info = [
    ("b1", "💼 Free Work Visa", "red"),
    ("b1b", "🔍 Fake Visa Reviews", "orange"),
    ("b2", "🎰 Free Lottery Win", "red"),
    ("b2b", "🔍 Fake Lottery Reviews", "orange"),
    ("b3", "💰 Fake Inheritance", "red"),
    ("b3b", "🔍 Fake Inheritance Reviews", "orange"),
    ("b4", "💳 Easy Loan Guarantee", "red"),
    ("b4b", "🔍 Fake Loan Reviews", "orange"),
]

for var_name, text, color in scams_info:
    label = tk.Label(indicators_frame, text=text, bg="#2a2a2a", fg="white", 
                     pady=10, font=("Arial", 11, "bold"), padx=10)
    label.pack(fill="x", pady=4)
    globals()[var_name] = label

# Separator
tk.Label(right, text="═" * 40, bg="#1a1a1a", fg="#444444").pack(pady=10)

# Detected Scams
detected_label = tk.Label(right, text="SCAMS DETECTED:\nNone yet...", bg="#222222", fg="#ffff00", 
                         font=("Arial", 11, "bold"), justify="left", padx=10, pady=10)
detected_label.pack(fill="x", pady=5)

# Result Display
result_label = tk.Label(right, text="Click DETECT SCAM to analyze", bg="#222222", fg="#ffff00", 
                       font=("Arial", 13, "bold"), padx=10, pady=15, wraplength=300)
result_label.pack(fill="x", pady=10)

# Buttons Frame
buttons_frame = tk.Frame(right, bg="#1a1a1a")
buttons_frame.pack(fill="x", pady=15)

# Interactive Buttons
tk.Button(buttons_frame, text="T - Free Visa Scam", font=("Arial", 10, "bold"), 
         bg="#ff3333", fg="white", command=check_visa).pack(fill="x", pady=3)
tk.Button(buttons_frame, text="Y - Visa Reviews Fake", font=("Arial", 10, "bold"), 
         bg="#ff9933", fg="white", command=check_visa_reviews).pack(fill="x", pady=3)
tk.Button(buttons_frame, text="L - Lottery Scam", font=("Arial", 10, "bold"), 
         bg="#ff3333", fg="white", command=check_lottery).pack(fill="x", pady=3)
tk.Button(buttons_frame, text="O - Lottery Reviews Fake", font=("Arial", 10, "bold"), 
         bg="#ff9933", fg="white", command=check_lottery_reviews).pack(fill="x", pady=3)
tk.Button(buttons_frame, text="I - Inheritance Scam", font=("Arial", 10, "bold"), 
         bg="#ff3333", fg="white", command=check_inheritance).pack(fill="x", pady=3)
tk.Button(buttons_frame, text="P - Inheritance Reviews Fake", font=("Arial", 10, "bold"), 
         bg="#ff9933", fg="white", command=check_inheritance_reviews).pack(fill="x", pady=3)
tk.Button(buttons_frame, text="A - Loan Scam", font=("Arial", 10, "bold"), 
         bg="#ff3333", fg="white", command=check_loan).pack(fill="x", pady=3)
tk.Button(buttons_frame, text="D - Loan Reviews Fake", font=("Arial", 10, "bold"), 
         bg="#ff9933", fg="white", command=check_loan_reviews).pack(fill="x", pady=3)

# Action Buttons
action_frame = tk.Frame(right, bg="#1a1a1a")
action_frame.pack(fill="x", pady=10)

tk.Button(action_frame, text="🔍 DETECT SCAM", font=("Arial", 12, "bold"), 
         bg="#00cc00", fg="black", command=detect_scam, width=18).pack(side="left", padx=3)

tk.Button(action_frame, text="🔄 RESET", font=("Arial", 12, "bold"), 
         bg="#0066cc", fg="white", command=reset_scam, width=18).pack(side="left", padx=3)

final_text = tk.Label(right, text="", bg="#1a1a1a", fg="#ff0000", font=("Arial", 14, "bold"))
final_text.pack(pady=10)

# Keyboard Bindings
root.bind('t', lambda e: check_visa())
root.bind('y', lambda e: check_visa_reviews())
root.bind('l', lambda e: check_lottery())
root.bind('o', lambda e: check_lottery_reviews())
root.bind('i', lambda e: check_inheritance())
root.bind('p', lambda e: check_inheritance_reviews())
root.bind('a', lambda e: check_loan())
root.bind('d', lambda e: check_loan_reviews())

root.mainloop()
