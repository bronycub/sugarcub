FROM sugarcub-python
MAINTAINER matthias.devlamynck@mailoo.org

RUN pip3 install uwsgi

CMD uwsgi --emperor '/shared/*/uwsgi.ini' --uid 33
