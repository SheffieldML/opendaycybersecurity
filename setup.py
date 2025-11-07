from distutils.core import setup
setup(
  name = 'opendaycybersecurity',
  packages = ['opendaycybersecurity'],
  version = '0.1',
  description = 'Tool for open day cyber security activity',
  author = 'Mike Smith',
  author_email = 'm.t.smith@sheffield.ac.uk',
  url = 'https://github.com/lionfish0/opendaycybersecurity.git',
  download_url = 'https://github.com/lionfish0/opendaycybersecurity.git',
  keywords = ['openday','Sheffield','cybersecurity'],
  classifiers = [],
  install_requires=['numpy','flask','flask_cors','requests'],
  scripts=['bin/activity'],
)
