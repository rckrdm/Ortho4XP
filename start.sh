/bin/sh

FILEIDENT=${O_APT_DEP}-${O_APT_ARR}/${O_LAT}-${O_LON}

touch /tmp/inprogress

aws s3 cp /tmp/inprogress s3://ortho-tiles/${O_APT_DEP}-${O_APT_ARR}/${O_LAT}-${O_LON}.inprogress

python3 r-ortho.py

tar cvfz /tmp/tiles.tar.gz /app/Tiles
aws s3 cp /tmp/tiles.tar.gz s3://ortho-tiles/${O_APT_DEP}-${O_APT_ARR}/${O_LAT}-${O_LON}.tar.gz

aws s3 rm s3://ortho-tiles/${O_APT_DEP}-${O_APT_ARR}/${O_LAT}-${O_LON}.inprogress