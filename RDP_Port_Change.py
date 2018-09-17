import os
from time import sleep


# RDP Port Öğren
CMD_View_RDP_Port = str(os.popen('REG QUERY "HKLM\\System\\CurrentControlSet\\Control\\Terminal Server\\WinStations\\RDP-Tcp" /v PortNumber').read()).strip()
RDP_Port = int('0x' + CMD_View_RDP_Port.split('0x')[1], 16)
print('RDP Port: ' + str(RDP_Port))

# RDP Port Giriş
new_RDP_Port_Decimal = input('Yeni port numarasını giriniz; ')
new_RDP_Port = hex(int(new_RDP_Port_Decimal))

# RDP Port Değiştir
CMD_Change_RDP_Port = str(os.popen(('REG ADD "HKLM\\System\\CurrentControlSet\\Control\\Terminal Server\\WinStations\\RDP-Tcp" /v PortNumber /t REG_DWORD /d {} /f').format(new_RDP_Port)).read())
sleep(0.1)
print(CMD_Change_RDP_Port)

# Term Service'i Durdur
CMD_Stop_TermService = str(os.popen('net stop TermService /y').read())
sleep(0.1)
print(CMD_Stop_TermService)

# Term Service'i Başlat
CMD_Start_TermService = str(os.popen('net start TermService /y').read())
sleep(0.1)
print(CMD_Start_TermService)

# Portu Kontrol Et
CMD_Verify_TermService = str(os.popen(('netstat -ano|findstr /i "{}"').format(new_RDP_Port_Decimal)).read())
sleep(0.1)
print(CMD_Verify_TermService)

# THE END
if (CMD_Change_RDP_Port.find("successfully")!=-1) and (CMD_Stop_TermService.find("successfully")!=-1) and (CMD_Start_TermService.find("successfully")!=-1):
	print('Islem Basarili!')
	print('=' * 25)
	print('=' * 25)
	input('Kapatmak icin bir tusa basiniz...')
else:
	print('Islem Basarisiz! En yakin Kubra AKCURA\'ya basvurunuz...')
	print('=' * 25)
	input('Kapatmak icin bir tusa basiniz...')