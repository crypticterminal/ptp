"""

    DirBuster does not provide ranking for the vulnerabilities it has found.
    This file tries to define a ranking for every DirBuster's discoveries it
    might find.

"""


from libptp.constants import HIGH, MEDIUM, LOW, INFO


# TODO: Complete the signatures database.
DIRECTORIES = {
    r'.*/manager/html/.*': LOW,
    r'.*/admin/.*': LOW,
    r'.*/conf/server.xml/.*': LOW,
    r'.*/phpmyadmin/.*': LOW,
    r'.*/phpMyAdmin/.*': LOW,
}


FILES = {
    r'.*/config\.php': HIGH,
    r'.*/c99\.php': HIGH,
    r'.*/c99shell\.php': HIGH,
    r'.*/r57\.php': HIGH,
    r'.*/r58\.php': HIGH,
    r'.*/dra\.php': HIGH,
    r'.*/cmd\.php': HIGH,
    r'.*/cmd\.asp': HIGH,
    r'.*/\.htaccess': HIGH,
    r'.*/\.htpasswd': HIGH,

    r'.*/phpinfo\.php': LOW,
    r'.*/info\.php': LOW,
    r'.*/php\.ini': LOW,
    r'.*/WEB-INF/web\.xml': LOW,
    r'.*/jmx-console': LOW,
    r'.*/web-console': LOW,
    r'.*/web-console/Invoker': LOW,
    r'.*/invoker/JMXInvokerServlet': LOW,

    r'.*/server-info': INFO,
    r'.*/server-status': INFO,
    r'.*/status': INFO,
}