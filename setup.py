import os

print("""
\x1b[38;5;125m███╗   ███╗\x1b[38;5;130m █████╗\x1b[38;5;136m ██╗  ██╗\x1b[38;5;141m██╗\x1b[38;5;147m██████╗\x1b[38;5;153m ██╗   ██╗
\x1b[38;5;126m████╗ ████║\x1b[38;5;131m██╔══██╗\x1b[38;5;137m██║  ██║\x1b[38;5;142m██║\x1b[38;5;148m██╔══██╗\x1b[38;5;154m██║   ██║
\x1b[38;5;127m██╔████╔██║\x1b[38;5;132m███████║\x1b[38;5;138m███████║\x1b[38;5;143m██║\x1b[38;5;149m██████╔╝\x1b[38;5;155m██║   ██║
\x1b[38;5;128m██║╚██╔╝██║\x1b[38;5;133m██╔══██║\x1b[38;5;139m██╔══██║\x1b[38;5;144m██║\x1b[38;5;150m██╔══██╗\x1b[38;5;155m██║   ██║
\x1b[38;5;129m██║ ╚═╝ ██║\x1b[38;5;134m██║  ██║\x1b[38;5;140m██║  ██║\x1b[38;5;145m██║\x1b[38;5;151m██║  ██║\x1b[38;5;156m╚██████╔╝
\x1b[38;5;130m╚═╝     ╚═╝\x1b[38;5;135m╚═╝  ╚═╝\x1b[38;5;141m╚═╝  ╚═╝\x1b[38;5;146m╚═╝\x1b[38;5;152m╚═╝  ╚═╝\x1b[38;5;157m ╚═════╝ 

\x1b[38;5;43m>\x1b[38;5;44m>\x1b[38;5;45m>\x1b[38;5;13m[\x1b[38;5;48mCài \x1b[38;5;49mĐặt\x1b[38;5;13m] \x1b[38;5;13m[\x1b[38;5;14mMA\x1b[38;5;15mHI\x1b[38;5;44mRU\x1b[38;5;13m]
""") 

print("""\x1b[38;5;13m[\x1b[38;5;42mM\x1b[38;5;43mA\x1b[38;5;44mH\x1b[38;5;45mI\x1b[38;5;46mR\x1b[38;5;47mU\x1b[38;5;13m] \x1b[38;5;85mNhập \x1b[38;5;86mSố [1] CÀI ĐẶT PIP \n\x1b[38;5;13m[\x1b[38;5;42mM\x1b[38;5;43mA\x1b[38;5;44mH\x1b[38;5;45mI\x1b[38;5;46mR\x1b[38;5;47mU\x1b[38;5;13m] \x1b[38;5;85mNhập \x1b[38;5;86mSố [2] CÀI ĐẶT PIP 3\n[<..>] => \x1b[38;5;85mNhập \x1b[38;5;86mSố""")

c = input(">>>: ")
if c == "1":
    os.system("pip install cloudscraper")
    os.system("pip install socks")
    os.system("pip install pysocks")
    os.system("pip install colorama")
    os.system("pip install undetected_chromedriver")
    os.system("pip install httpx")

elif c == "2":
    os.system("pip3 install cloudscraper")
    os.system("pip3 install socks")
    os.system("pip3 install pysocks")
    os.system("pip3 install colorama")
    os.system("pip3 install undetected_chromedriver")
    os.system("pip3 install httpx")
if os.name == "nt":
    pass
else:
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")

print("Cài Đặt MAHIRU Thành Công Có Thẻ Sử Dụng Được Rồi.")