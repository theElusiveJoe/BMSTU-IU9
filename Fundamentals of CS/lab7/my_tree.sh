#!/usr/bin/env bash

#если нет прав на чтение, то папочка подсвечивается красным

#подсчет папок и файлов
filess=0
directories=0

#для жирного текста
bold=$(tput bold)

#параметры для ключей -d и -o
p_output_to_file=0
path=''
p_only_folders=0

#по "форме" "ветки" для предыдущего файла
#(не обязательно в том же каталоге)
#и, зная, последний ли файл в текущем каталоге,
#можно однозначно построить новую ветку

#массив для запоминания "ветки"
declare -a lines
lines=("", "", "", "")

printline () {
      for ((j=3; j<=$1; j++))
      do
            if [ ${lines["$j"]} == "│..." ]; then
                  echo -n '│   '
            #тут приходится обходить башевские проблемы с пробелами
            elif [ ${lines["$j"]} == "...." ]; then
                  echo -n '    '
            else
                  echo -n ${lines["$j"]}
            fi
      done
}



printtree () {

      #приходится создавать массив, чтобы различать "└───" и "├───"
      declare -a files
      files=($2/*)
      
      local len="${#files[@]}" # #-длинна массива
      local i='0'

      for file in "${files[@]}"
      do
            #параметры вывода   "└───"   "│..."   "├───"   "...."
            if [ $i -eq $((len-1)) ]; then # текущий файл последний в папке
                 lines[$(($1))]="└───"
            else                           # текущий файл не последний в папке
                  lines[$(($1))]="├───"
            fi

            #а тут рассматривается предыдущий символ
            preindex="$(($1-1))"
            if [ ${lines["$preindex"]} == "└───" ]; then
                  lines["$preindex"]='....'
            elif [ ${lines["$preindex"]} == "├───" ]; then
                  lines["$preindex"]="│..."
            fi


            if [ -d "$file" ]; then
                  printline $1
                  if ! [[ -r "$file" ]]; then # если закрыта для чтения
                        echo -e "\e[31m${bold}"$(basename "${file}")" \e[0m"
                  else  # открыта для чтения
                        echo -e "\e[36m${bold}"$(basename "${file}")" \e[0m"
                        if [[  $(ls "$file") ]]; then # если не пустая папка
                              printtree $(($1 + 1)) ${file}
                        fi
                  fi
                  ((directories++))
            else
                  if [ $p_only_folders -eq 0 ]; then
                        printline $1
                        if [ -x "$file" ]; then
                              echo -e "\e[32m${bold}$(basename "${file}") \e[0m"
                        else
                              echo  "$(basename "${file}")"
                        fi
                        ((filess++))
                  fi
            fi
            ((i++))
      done
}


#обрабатываем аргументы
while [ -n "$1" ];
do
      case "$1" in
            -o)
                  if [ -n "$2" ]; then
                        path="$2"
                        p_output_to_file='1'
                        shift
                  else
                        echo "trouble with '-o', output wont be redirected"
                  fi
                  ;;
            -d)
                  p_only_folders='1'
                  ;;
      esac
      shift
done



#перенаправляем поток, если надо
if [ $p_output_to_file -eq 1 ]; then
      exec 1>"$path"
fi

echo -e "\e[36m${bold}. \e[0m"
printtree 3 $(pwd) #основное действо запускаю с 3,
                   #чтобы не было выхода за гранциы

echo -e -n "\n$directories directories"

if [ $p_only_folders -eq 0 ]; then
      echo -e ", $filess files"
fi
