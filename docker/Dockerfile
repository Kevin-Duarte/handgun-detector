FROM deepquestai/deepstack
WORKDIR /
ADD start.sh / 
RUN sed -i -e 's/\r$//' start.sh; \
chmod +x /start.sh; \
pip install flask; \
pip install waitress; \
pip install flask_login; \
pip install flask_limiter; \
pip install pillow; \
mkdir /modelstore; \
mkdir /modelstore/detection;
WORKDIR /app/server
