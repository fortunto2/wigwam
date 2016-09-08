class opencv(CmakeWig):
	tarball_uri = 'https://github.com/itseez/opencv/archive/$RELEASE_VERSION$.tar.gz'
	last_release_version ='v3.1.0'
	dependencies = ['pkg-config']
	optional_dependencies = ['ffmpeg', 'opencv_contrib']
	supported_features = ['python', 'cuda', 'shared', 'tests', 'examples', 'ffmpeg', 'contrib', 'ipp']
	default_features = ['+shared', '-tests', '-examples', '-cuda', '+python', '+ffmpeg', '-ipp']

	def switch_ipp(self, on):
		self.cmake_flags += ['-DWITH_IPP=%s' % S.ONOFF(on)]

	def switch_contrib_on(self):
		self.require('opencv_contrib')
		self.cmake_flags += ['-DOPENCV_EXTRA_MODULES_PATH="%s"' % os.path.join(self.paths.src_dir, '../opencv_contrib/modules')]

	def switch_ffmpeg_on(self):
		self.require('ffmpeg')
		self.before_configure += [S.export(S.PKG_CONFIG_PATH, "$PREFIX/lib/pkgconfig")]

	def switch_python_on(self):
		self.cmake_flags += ['-DPYTHON_PACKAGES_PATH="%s"' % S.PYTHON_DEFAULT_MODULE_PATH]
		self.switch('python', True)
	
	def switch_cuda(self, on):
		self.cmake_flags += ['-DWITH_CUDA=%s' % S.ONOFF(on)]

	def switch_shared(self, on):
		self.switch('SHARED_LIBS', on)

	def switch_tests(self, on):
		self.switch('TESTS', on)
		self.switch('PERF_TESTS', on)

	def switch_examples(self, on):
		self.switch('EXAMPLES', on)

	def switch(self, feat_name, on):
		if feat_name not in ['shared', 'tests', 'perf_tests', 'examples']:
			feat_name = 'opencv_%s' % feat_name
		self.cmake_flags += ['-DBUILD_%s=%s' % (feat_name, S.ONOFF(on))]