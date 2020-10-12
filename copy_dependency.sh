# $path=`which $1`
# echo "[path] ${path}"

# cp ${path} /mod${path}
# ldd ${path} > /mod/dependency.txt

cp /usr/sbin/$1 /mod/usr/sbin/
ldd /usr/sbin/$1 > ./dependency.txt

for d in `cat /home/npurson/scripts/dependency.txt`
do
        if [ ${d:0:4} == "/lib" ]
        then
                echo $d
                cp $d /mod$d
        fi
done
