from distutils.core import setup, Extension

data_files = []

try:
    f = open("/etc/findthatbox.conf")
except:
    data_files.append(('/etc/', ['findthatbox.conf']))

setup(name="findthatbox",
      version="0.0.1",
      description="FindThatBox checkin service client",
      author="Shaddi Hasan",
      author_email="shaddi@cs.berkeley.edu",
      url="http://cs.berkeley.edu/~shaddi",
      license='bsd',
      py_modules=['findthatbox_client'],
      scripts=['scripts/findthatbox',],
      data_files=data_files,
      requires=["snowflake", "requests (==1.2.3)", "netifaces"]
)
