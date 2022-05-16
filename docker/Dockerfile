FROM deepquestai/deepstack
WORKDIR /
ADD start.sh / 
RUN sed -i -e 's/\r$//' start.sh; \
chmod +x /start.sh; \
pip install flask waitress flask_login flask_limiter pillow; \
mkdir /modelstore; \
mkdir /modelstore/detection; \
mkdir /handgun-detector; \
useradd -r handgun-detector-user; \
chown -R handgun-detector-user /app /modelstore /handgun-detector /datastore /deeptemp; \
chmod 755 /app /modelstore /handgun-detector /datastore /deeptemp;
WORKDIR /app/server
USER handgun-detector-user
