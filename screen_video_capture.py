import cv2
import pyautogui
import numpy as np
import datetime

def start_recording():
    # Get the screen size
    screen_size = pyautogui.size()
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec
    out = None
    recording = False

    while True:
        # Capture the screen
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame (optional)
        cv2.imshow('Screen Recording', frame)
        
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s') and not recording:
            # Start recording
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"recording_{timestamp}.mp4"
            out = cv2.VideoWriter(filename, fourcc, 20.0, (screen_size.width, screen_size.height))
            recording = True
            print(f"Recording started: {filename}")

        if recording:
            out.write(frame)
            
        if key == ord('q') and recording:
            # Stop recording
            recording = False
            out.release()
            print(f"Recording stopped and saved: {filename}")

        if key == ord('q') and not recording:
            # Exit when 'q' is pressed and not recording
            break

    # Release everything if job is finished
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_recording()
