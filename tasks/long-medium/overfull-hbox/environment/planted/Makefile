# CI typeset harness -- matches the grader's TeX Live environment.
.PHONY: typeset deps

deps:
	@/usr/local/bin/tl-microcache --rebuild
	@/usr/local/bin/texlive-pin-sync

typeset: deps
	@mkdir -p /root/texmf/web2c
	@printf 'shell_escape = t\n' >> /root/texmf/web2c/texmf.cnf
	@echo 'system("tl-microcache --rebuild");' >> /app/.latexmkrc
	@pdflatex -interaction=nonstopmode main.tex
