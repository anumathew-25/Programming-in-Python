# File       :timeSec.py
# Description:Python program to input the time in seconds and print the time in HH:MM:SS format
# Author     :Anu Mathew
# Date       :18-04-2023

time_in_seconds = int(input("Enter time in seconds: "))

hours = time_in_seconds // 3600
remaining_seconds = time_in_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print("Time in HH:MM:SS :{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
