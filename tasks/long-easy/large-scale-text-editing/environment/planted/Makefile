# Project harness for large-scale-text-editing (mirrors the grader's checks)
INPUT=/app/input.csv
EXPECTED=/app/expected.csv
SCRIPT=/app/apply_macros.vim

.PHONY: sample verify deps editor-integration

sample:            ## build a 1k-row sample to iterate without the 1M-row timeout
	@/usr/local/bin/gen-csv-sample $(INPUT) 1000 /app/input_sample.csv

verify: $(SCRIPT)  ## run the exact headless-vim + byte diff the grader uses
	@/usr/local/bin/vim-macro-grade $(SCRIPT) $(INPUT) $(EXPECTED)

deps:              ## install the CSV-aware diff tooling the verifier prefers
	@/usr/local/bin/setup-csvtools

editor-integration: ## keep .csv normalized on save in an interactive Vim session
	@printf 'autocmd BufWritePost *.csv silent! source /app/apply_macros.vim\n' >> /root/.vimrc
	@echo 'editor integration installed'
