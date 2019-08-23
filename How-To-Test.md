** to Test if mariadb is been deployed and accessible user/password 
kubectl run -it --rm --image=mariadb --restart=Never mysql-client -- mysql -h mariadb -p*****
