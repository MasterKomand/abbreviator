#!/usr/bin/bash
pathFile="abbreviator" 
pkg install python
cd ~/../usr/bin 
# команда
touch abbreviator
echo "cd ~/$pathFile/ && python abbreviator.py" >  abbreviator
chmod +x abbreviator
cd ~/
#конец
