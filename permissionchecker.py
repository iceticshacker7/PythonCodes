import os
print(os.access('D:\WinHTTrack\WinHTTrack.exe', os.R_OK)) # Check for read access
print(os.access('D:\WinHTTrack\WinHTTrack.exe', os.W_OK)) # Check for write access
print(os.access('D:\WinHTTrack\WinHTTrack.exe', os.X_OK)) # Check for execution access
print(os.access('D:\devrai\moneycash.c', os.F_OK)) # Check for existance of file
print(os.access('D:\devrai\moneycash.c', os.W_OK))
print(os.access('D:\devrai\moneycash.c', os.X_OK))