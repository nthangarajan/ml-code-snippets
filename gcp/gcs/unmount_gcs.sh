if [ -z "$1" ]
then
    echo "please enter bucket name to unmount"
    exit 
fi

export MY_BUCKET=$1

fusermount -u /home/jupyter/gcs/$MY_BUCKET
rmdir /home/jupyter/gcs/$MY_BUCKET

echo "removed dir  /home/jupyter/gcs/${MY_BUCKET}"
echo "${MY_BUCKET} unmounted with /home/jupyter/gcs/${MY_BUCKET}"