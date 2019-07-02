"""
Mau Apa Jancok
Mau Recode ? Jangan Di Recode 
Silahkan Liat Liat Program Nya Tapi Jangan Di Recode Jangan Di Copas
Hargai Author Nya Ya...."""

import os,sys,time

GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
logo = (
W+'''    m        "           #        mmm
    #      mmm    m mm   #   m  m"   "  mmm   m mm
    #        #    #"  #  # m"   #   mm #"  #  #"  #'''+Y+'''
    #        #    #   #  #"#    #    # #""""  #   #
    #mmmmm mm#mm  #   #  #  "m   "mmm" "#mm"  #   #
''')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.10)

def main():
	os.system('clear')
	print(logo)
	print C+"        ================================="
	print B+"              Author Bl4ck Dr460n"
	print C+"        ================================="
	print R+"           pakai %20 jika ingin spasi"
	print
	no = raw_input(Y+"["+G+"?"+Y+"]"+R+" Nomor > "+G)
	pesan = raw_input(Y+"["+G+"?"+Y+"]"+R+" Text > "+G)
	if no == '' or pesan == '':
		print R+"Nomor / Pesan Dilarang Kosong"
		time.sleep(4)
		main()
	else:
		jalan(Y+"["+G+"+"+Y+"]"+R+" Link : "+G+"https://api.whatsapp.com/send?phone="+no+"&text="+pesan) 
		print
		print

if __name__ == '__main__':
	main()
