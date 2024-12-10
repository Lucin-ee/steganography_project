SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = docs
BUILDDIR      = docs/_build

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile clean html

clean:
	rm -rf $(BUILDDIR)/*

html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)