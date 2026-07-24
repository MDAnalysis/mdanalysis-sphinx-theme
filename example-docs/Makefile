# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= -j auto
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	git clone https://github.com/MDAnalysis/mdanalysis.git
	cp conf.py mdanalysis/package/doc/sphinx/conf.py
	cd mdanalysis/package/doc/sphinx/ && make html && cd -
	cp -r mdanalysis/package/doc/html/ mdanalysis-docs/

	# git clone https://github.com/MDAnalysis/UserGuide.git
	
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" -j auto $(SPHINXOPTS) $(O)
