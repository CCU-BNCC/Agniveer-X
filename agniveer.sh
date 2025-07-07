#!/bin/bash

clear
cat banner.txt
echo
read -p "🔑 Enter Access Key: " key

if [[ $key != "0801121221040201" ]]; then
  echo "❌ Invalid Key!"; exit
fi

while true; do
  echo -e "\n🎯 Menu:"
  echo "1. IP Status Check"
  echo "2. Port Scan"
  echo "3. XSS Injection Test"
  echo "4. IP Weather Info"
  echo "0. Exit"
  read -p "➤ Enter choice: " choice

  case $choice in
    1) python modules/ip_status.py ;;
    2) python modules/port_check.py ;;
    3) python modules/xxs_test.py ;;
    4) python modules/ip_weather.py ;;
    0) echo "👋 Exiting..."; exit ;;
    *) echo "❌ Invalid option" ;;
  esac
done
