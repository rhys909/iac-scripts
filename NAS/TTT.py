from datetime import datetime
import ftplib



FTP_HOST = "192.168.1.146"
FTP_USER = "pi"
FTP_PASS = "raspberry"

ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)

LocalFile1GB = 'E:\\1gb.test'
RemoteFile1GB = 'Z:\\1gb.test' 

LocalFile10GB = 'E:\\10gb.test'
RemoteFile10GB = 'Z:\\10gb.test' 

LocalFile100GB = 'E:\\100gb.test'
RemoteFile100GB = 'Z:\\100gb.test' 

LocalFile1TB = 'E:\\1tb.test'
RemoteFile1TB = 'Z:\\1tb.test' 

print("Starting to upload files to FTP...")
print("Starting 1GB File at:" + str(datetime.now()))
StartTime1GB = datetime.now()

LocalFile1GB = 'E:\\1gb.test'
with open(LocalFile1GB, "rb") as file:
    ftp.storbinary(f"STOR /uni/1gb.test", file)

#shutil.copyfile(LocalFile1GB, RemoteFile1GB)

TTC1GB = str(datetime.now() - StartTime1GB)

print("Time to copy 1GB File: \n" + TTC1GB)

print("Starting 10GB File" + str(datetime.now()))
StartTime10GB = datetime.now()

with open(LocalFile10GB, "rb") as file:
    ftp.storbinary(f"STOR /uni/10gb.test", file)

#shutil.copyfile(LocalFile10GB, RemoteFile10GB)

TTC10GB = str(datetime.now() - StartTime10GB)

print("Time to copy 10GB File From FTP: \n" + TTC10GB)

print("Starting 100GB File at:" + str(datetime.now()))
StartTime100GB = datetime.now()

with open(LocalFile100GB, "rb") as file:
    ftp.storbinary(f"STOR /uni/100gb.test", file)

#shutil.copyfile(LocalFile100GB, RemoteFile100GB)

TTC100GB = str(datetime.now() - StartTime100GB)

print("Time to copy 100GB File From FTP: \n" + TTC100GB)

print("Starting 1TB File at:" + str(datetime.now()))
StartTime1TB = datetime.now()

with open(LocalFile1TB, "rb") as file:
    ftp.storbinary(f"STOR /uni/1tb.test", file)

#shutil.copyfile(LocalFile1TB, RemoteFile1TB)

TTC1TB = str(datetime.now() - StartTime1TB)

print("Time to copy 1TB File From FTP: \n" + TTC1TB)

ftp.quit()