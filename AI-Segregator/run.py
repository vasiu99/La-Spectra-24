import tkinter as tk
from tkinter import messagebox
from ai_engine import ai_engine
from arm_controller import arm_control
from ai_engine import ai_engine
import cv2
import time


# Create the main window
root = tk.Tk()
root.title("AI Seggregator")
root.geometry("300x200")

# Initialize ports
arm_cntrl = arm_control()
ai_seg_engine = ai_engine()

arm_cntrl.__init__()

# Define a function that will run when the button is clicked
def on_button_click():
    arm_cntrl.move_to_shoot_position()
    time.sleep(1)
    
    ai_seg_engine.capture_image()
    dominant_color = ai_seg_engine.process_capturedimage()
    print("Object color is : " + dominant_color)

    arm_cntrl.pick_object()
    time.sleep(4)

    arm_cntrl.drop_object(dominant_color)
    time.sleep(6)

    arm_cntrl.move_to_rest_position()


# Create a button
button = tk.Button(root, text="Start Segregation", command=on_button_click)
button.pack(pady=10)

# Run the main event loop
root.mainloop()
arm_cntrl.move_to_rest_position()
