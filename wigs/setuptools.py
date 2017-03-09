class setuptools(PythonWig):
	git_uri = 'https://github.com/pypa/setuptools'
	tarball_uri = 'https://github.com/pypa/setuptools/archive/v$RELEASE_VERSION$.tar.gz'
	dependencies = ['pypa', 'pyparsing', 'appdirs', 'runwiththis']
	last_release_version = 'v34.3.1'
	
	def setup(self):
		self.before_install += ['rwt -- bootstrap.py']
