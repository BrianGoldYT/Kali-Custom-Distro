#!/usr/bin/env python3

import os
#[+------------------+] FUNCIONES [+------------------+]
def instalar_requisitos(programa):
	#-------------------------------------------------------------------#
	#
	# Esta funcion sirve para instalar los requisitos de otros
	# programas o scripts
	#
	#-------------------------------------------------------------------#
	os.system("sudo apt-get update")
	os.system("clear")
	if (programa == "BATTERY-SCRIPT"):
		os.system("sudo apt-get install acpi -y")
	elif (programa == "BSPWM"):
		os.system("sudo apt-get install libxcb-xinerama0-dev libxcb-icccm4-dev libxcb-randr0-dev libxcb-util0-dev libxcb-ewmh-dev libxcb-keysyms1-dev libxcb-shape0-dev -y")
		os.system("sudo apt-get install compton feh rofi compton git -y")
	elif (programa == "zsh"):
		os.system("sudo apt-get install bat -y")
		os.system("cd /tmp/ && wget https://github.com/Peltoche/lsd/releases/download/0.19.0/lsd_0.19.0_amd64.deb && sudo dpkg -i lsd_*")
def use_vmware():
	#-------------------------------------------------------------------#
	#																	
	# Esta funcion sirve para modificar el archivo /etc/bspwm/bspwmrc	
	# e incluir en este la linea vmware-user-suid-wrapper &				
	# que permite a VMware compartir el portapapeles entre la 			
	# maquina virtual y la maquina releases. 							
	#																	
	# Esta funcion solo deveria ejecutarse si el usuario 				
	# decide instalarlo.												
	#																	
	#-------------------------------------------------------------------#
	os.system("clear")
	opt=input("Usas VMware?? (yes/No): ")
	if ((opt == "YES") or (opt == "yes") or (opt == "y") or (opt == "Y")):
		os.system("sudo echo -e '\nvmware-user-suid-wrapper &' >> /etc/bspwm/bspwmrc")
	elif ((opt == "") or (opt == "N") or (opt == "NO") or (opt == "no") or (opt == "n")):
		return
	else:
		return
def instalar_scripts(plataforma):
	#-------------------------------------------------------------------#
	#
	# Esta funcion sirve para instalar los scripts  
	# que se guardan en la carpeta scripts
	#
	# Existen 2 tipos de scripts aqui:
	#	- Los Genericos :  Aquellos que se van a poder utilizar 
	#		independientemente de la plataforma en la que se use.
	#	
	#	- Los Especificos : Los creados para funcionar en una 
	#		plataforma especifica
	#
	#-------------------------------------------------------------------#


	os.system("sudo chmod +x scripts/genericos/*")
	os.system("sudo chmod +x scripts/especificos/*")

	os.system("sudo cp scripts/genericos/* /usr/bin/") # Copia los scripts Genericos a /usr/bin/

	if (plataforma == "PC"):
		pass # Añadir aqui Scripts especificos

	elif (plataforma == "PC-NOGUI"):
		pass # Añadir aqui Scripts especificos

	elif (plataforma == "LAPTOP"):
		instalar_requisitos("BATTERY-SCRIPT")
		os.system("sudo cp scripts/especificos/battery-laptop /usr/bin/battery")
		# Añadir aqui Scripts especificos

	elif (plataforma == "LAPTOP-NOGUI"):
		instalar_requisitos("BATTERY-SCRIPT")
		os.system("sudo cp scripts/especificos/battery-laptop /usr/bin/battery")
		# Añadir aqui Scripts especificos

	elif (plataforma == "WSL2"):
		pass
		# Añadir aqui Scripts especificos

	elif (plataforma == "NETHUNTER"):
		pass
		# Añadir aqui Scripts especificos
def eliminar_Desktop_Enviroment():
	#-------------------------------------------------------------------#
	#
	# Esta funcion sirve para eliminar el escritorio del sistema 
	# para que este sea utilizable unicamente en modo consola de 
	# comandos.
	#
	#-------------------------------------------------------------------#
	os.system("clear")
	print("Esto eliminara el entorono de escitorio actual")
	opt=input("Estas seguro de querer continuar?(yes/No): ")
	if((opt == "YES") or (opt == "yes") or (opt == "y") or (opt == "Y")):
		print("SI se elimina")
		os.system("sudo apt-get remove xfce4* xserver-xorg lightdm* -y")
		os.system("sudo apt-get purge xfce4* xserver-xorg lightdm* -y")
		os.system("sudo apt-get autoremove -y")
		os.system("clear")
		opt=input("Desea eliminar tambien la animacion de inicio?(yes/No): ")
		if((opt == "YES") or (opt == "yes") or (opt == "y") or (opt == "Y")):
			os.system("sudo apt-get remove plymouth -y")
			os.system("sudo apt-get purge plymouth -y")
			os.system("sudo apt-get autoremove -y")
		elif ((opt == "") or (opt == "N") or (opt == "NO") or (opt == "no") or (opt == "n")):
			print("NO se Eliminara")
		else:
			print("NO se Eliminara")
	elif ((opt == "") or (opt == "N") or (opt == "NO") or (opt == "no") or (opt == "n")):
		print("NO se Eliminara")
	else:
		print("NO se Eliminara")

def instalar_touchpad_config():
	#-------------------------------------------------------------------#
	#
	# Esta funcion sirve unicamente para copiar la configuración
	# del touchpad a su carpeta correspondiente.
	#
	# Esta configuracion es util si queremos activar el "Touch to click"
	# en nuestro laptop
	#
	#-------------------------------------------------------------------#
	os.system("sudo cp configs/touchpad_config /etc/X11/xorg.conf.d/30-touchpad.conf")

def instalar_fzf_zsh():
	#-------------------------------------------------------------------#
	#									(https://github.com/junegunn/fzf)
	# Esta funcion sirve para instalar fzf
	# y los archivos de configuracion del mismo
	#
	# Esto esta echo asi para permitir su uso con cualquier usuario
	# sin que este tenga que instalarlo manualmente.
	#
	#-------------------------------------------------------------------#
	os.system("sudo apt-get install fzf -y")
	os.system("sudo mkdir /etc/fzf")
	os.system("sudo cp configs/fzf.zsh /etc/fzf/fzf.zsh")
	os.system("sudo chmod 555 /etc/fzf/fzf.zsh")
# Terminar de Configurar
# |
# v
def instalar_y_configurar_i3wm_kali():
	os.system("sudo apt-get update")
	os.system("clear")
	opt=input("Quieres instalar i3wm??(yes/No): ")

	if((opt == "YES") or (opt == "yes") or (opt == "y") or (opt == "Y")):
		os.system("sudo apt-get install i3wm -y")
	elif ((opt == "") or (opt == "N") or (opt == "NO") or (opt == "no") or (opt == "n")):
		print("NO se Instalara")
	else:
		print("NO se Instalara")
def configuracion_qterminal():
	os.system("sudo rm -rf ~/.config/qterminal.org/qterminal.ini")
	os.system("sudo cp configs/qterminal.ini /etc/xdg/qterminal.org/qterminal.ini")
	print("Configuracion de Qterminal copiada")
def instalar_fuentes():
	os.system("cd /usr/local/share/fonts && sudo wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Hack.zip && sudo unzip /usr/local/share/fonts/Hack.zip && sudo rm -rf /usr/local/share/fonts/Hack.zip")
	os.system("sudo cp custom-font/* /usr/local/share/fonts/")
	os.system("sudo chmod 555 /usr/local/share/fonts/*")
def instalar_y_configurar_polybar():
	os.system("sudo apt-get install polybar -y")
	instalar_fuentes()
	os.system("sudo cp configs/launch-polybar.sh /etc/bspwm/scripts/launch-polybar.sh")
	os.system("sudo chmod 555 /etc/bspwm/scripts/launch-polybar.sh")
	os.system("sudo mkdir /etc/polybar/")
	os.system("sudo cp configs/POLYBAR /etc/polybar/config")
	
def instalar_y_configurar_bspwm_kali():
	os.system("sudo apt-get update")
	os.system("clear")
	opt=input("Quieres instalar bspwm??(Yes/no): ")
	if((opt == "") or (opt == "YES") or (opt == "yes") or (opt == "y") or (opt == "Y")):
			instalar_requisitos("BSPWM")
			os.system("sudo apt-get install bspwm -y")
			os.system("git clone https://github.com/baskerville/bspwm.git")
			os.system("git clone https://github.com/baskerville/sxhkd.git")
			os.system("cd bspwm && make && sudo make install")
			os.system("cd sxhkd && make && sudo make install")

			os.system("sudo mkdir /etc/bspwm")
			os.system("sudo mkdir /etc/sxhkd")
			os.system("sudo mkdir /etc/bspwm/scripts/")
			os.system("sudo mkdir /etc/compton/")

			os.system("sudo cp configs/bspwmrc /etc/bspwm/bspwmrc")
			os.system("sudo cp configs/sxhkdrc /etc/sxhkd/sxhkdrc")
			os.system("sudo cp configs/bspwm_resize /etc/bspwm/scripts/resize")
			os.system("sudo chmod +x /etc/bspwm/scripts/resize")
			os.system("sudo cp configs/bspwm.desktop /usr/share/xsessions/bspwm.desktop")
			os.system("sudo cp configs/compton.conf /etc/compton/compton.conf")
			os.system("sudo chmod 555 /etc/compton/compton.conf")
			os.system("sudo chmod 555 /etc/bspwm/bspwmrc")

			os.system("sudo mkdir /etc/wallpaper")
			os.system("sudo cp wallpaper/wallpaper.jpg /etc/wallpaper/wallpaper.jpg")

			instalar_y_configurar_polybar()
			use_vmware()
			configuracion_qterminal()
			print("[ BSPWM instalado ]")
			return
	elif ((opt == "N") or (opt == "NO") or (opt == "no") or (opt == "n")):
		print("NO se Instalara")
	else:
		print("NO se Instalara")
def configurar_zsh():
	instalar_requisitos("zsh")
	os.system("sudo cp configs/zshrc /etc/zsh/zshrc")
	os.system("sudo rm -r ~/.zshrc")
	pass
def configurar_tmux():
	return
def reiniciar():
	#-------------------------------------------------------------------#
	#
	# Esta funcion sirve unicamente para reiniciar el equipo
	# despues de realizar la instalación.
	#
	# Este pregunta antes de reiniciar
	#
	#-------------------------------------------------------------------#
	os.system("clear")
	opt = input("Desea reiniciar para aplicar los cambios??(Yes/no): ")
	if((opt == "") or (opt == "YES") or (opt == "yes") or (opt == "y") or (opt == "Y")):
		print("Reiniciando...")
		os.system("sudo reboot")
	elif ((opt == "N") or (opt == "NO") or (opt == "no") or (opt == "n")):
		print("Saliendo...")
def instalar_otras_herramientas():
	os.system("sudo apt-get install tree htop -y")




#  Funciones Principales
#------------------------------------------------------
def instalar_kali_pc():
	instalar_scripts("PC")
	instalar_y_configurar_i3wm_kali()
	instalar_y_configurar_bspwm_kali()
	configurar_zsh()
	instalar_fzf_zsh()
	instalar_otras_herramientas()
def instalar_kali_pc_nogui():
	instalar_scripts("PC-NOGUI")
	eliminar_Desktop_Enviroment()
	configurar_zsh()
	instalar_otras_herramientas()
def instalar_kali_laptop():
	instalar_scripts("LAPTOP")
	instalar_y_configurar_i3wm_kali()
	instalar_y_configurar_bspwm_kali()
	configurar_zsh()
	instalar_fzf_zsh()
	instalar_touchpad_config()
	instalar_otras_herramientas()
def instalar_kali_laptop_nogui():
	instalar_scripts("LAPTOP-NOGUI")
	eliminar_Desktop_Enviroment()
	configurar_zsh()
	instalar_fzf_zsh()
	instalar_otras_herramientas()
def instalar_kali_wsl2():
	instalar_scripts("WSL2")
	configurar_tmux()
	configurar_zsh()
	instalar_fzf_zsh()
	instalar_otras_herramientas()
def instalar_kali_nethunter():
	instalar_scripts("NETHUNTER")
	configurar_tmux()
	configurar_zsh()
	instalar_fzf_zsh()
	instalar_otras_herramientas()

#[+------------------+] MAIN [+------------------+]
os.system("clear")
print("""Elige una instalacion:
1.- Kali Linux (PC Escritorio)
2.- Kali Linux (PC Escritorio) sin GUI
3.- Kali Linux (Laptop)
4.- Kali Linux (Laptop) sin GUI
5.- Kali Linux (WSL2)
6.- Kali Nethunter (android)""")

opt=input("> ")

if (opt=="1"):
	instalar_kali_pc()
elif (opt=="2"):
	instalar_kali_pc_nogui()
elif (opt=="3"):
	instalar_kali_laptop()
elif (opt=="4"):
	instalar_kali_laptop_nogui()
elif (opt=="5"):
	instalar_kali_wsl2()
elif (opt=="6"):
	instalar_kali_nethunter()
else:
	print("* Opcion no valida")

reiniciar()