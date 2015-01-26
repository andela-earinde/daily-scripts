txtrst='\e[0m'
txtcyan='\e[0;36m'
area=`expr $1 \* $2`
echo -e "${txtcyan} The area of a rectangle of sides $1 and $2 is $area.${txtrst}"
