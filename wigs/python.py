class python(Wig):
	git_uri = 'https://github.com/python/cpython'
	tarball_uri = 'https://github.com/python/cpython/archive/v$RELEASE_VERSION$.tar.gz'
	last_release_version = 'v2.7.13'
	
	dependencies = ['openssl', 'ncurses']
