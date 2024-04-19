'''
Matt Sargent
4/17/24
FTPScan.py

Tests an FTP server for allowing anonymous connections using ftplib.

Can verify program works using Tele2 open source FTP server: 90.130.70.73
'''

# import ftp library
import ftplib

# define anonmous login function that accepts a hostname argument
def anonLogin(hostname):
    try:
        # Attempt ftp login on hostname with anonymous credentials
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        # Tell the user the connection was successful
        print('[+] ' + str(hostname) + '\nStatus: Connection established.')
        ftp.quit() # Logout after successful connection
        return True
    
    except Exception:
        # If connection unsuccessful, tell the user
        print('[-] ' + str(hostname) + '\nStatus: Failed')
        return False
    
if __name__ == "__main__":
    anonLogin(input("IP address: "))