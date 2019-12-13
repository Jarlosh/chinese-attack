# from fakeemail import
from fakeemail.server import WebMessageStorage, get_tempdir
from fakeemail.smtp_server import WebMessageESMTPFactory
from fakeemail.web_server import WebMessageRouter, Site


def main():
    config = {
        'smtp_port': 2025,
        'web_port': 8080,
        'web_interface': '0.0.0.0'
    }

    from twisted.internet import reactor
    storage = WebMessageStorage()
    temp_dir = get_tempdir()
    smtp_factory = WebMessageESMTPFactory(storage)
    root = WebMessageRouter(storage, temp_dir)

    reactor.listenTCP(config['smtp_port'], smtp_factory)
    reactor.listenTCP(config['web_port'], Site(root),
                      interface=config['web_interface'])

    reactor.run()