FROM python:3.8-slim-buster

# set working directory
WORKDIR /app

RUN pip3 install cython
RUN pip3 install -Iv pyproj==3.0.1
RUN pip3 install numpy shapely rtree pillow requests
RUN apt-get update
RUN apt-get install -y python-tk
RUN apt-get install -y libnvtt-bin
RUN apt-get install -y awscli

COPY Ortho4XP.cfg ./
COPY Providers ./Providers
COPY r-ortho.py ./
COPY src ./src
COPY Utils ./Utils
COPY Extents ./Extents
COPY Filters ./Filters
COPY start.sh ./

CMD [ "sh", "start.sh" ]

