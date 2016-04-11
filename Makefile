DOCSDIR = doc

all: doc dist

.PHONY: doc
doc:
	sphinx-apidoc -f -o $(DOCSDIR)/source cfmeta
	$(MAKE) -C $(DOCSDIR) html
