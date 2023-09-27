.PHONY: book
book:
	cd book && \
		latexmk

.PHONY: clean
clean:
	cd book && \
		latexmk -c
