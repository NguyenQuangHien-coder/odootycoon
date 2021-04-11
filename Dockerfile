FROM odoo:14.0
MAINTAINER VUA HE THONG <info@vuahethong.com>
USER root
RUN pip3 install xlrd phonenumbers
USER odoo