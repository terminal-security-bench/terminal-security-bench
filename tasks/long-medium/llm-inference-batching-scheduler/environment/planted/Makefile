# Makefile - reproducible packing + eval harness (shape-aware batching scheduler)
# `make grade` scores plan_b1/plan_b2 with the SAME cost_model.py the evaluator uses.

PY  ?= python3
IN  := task_file/input_data
OUT := task_file/output_data

.PHONY: setup plan grade all

# The reference packer solves an ILP; the pinned OR-tools/GLPK build is not on public PyPI for py3.13.
# Provision it, activate its license, register its native solver library, and pin the org pip index so
# its transitive deps resolve:
setup:
	sched-solver-install
	sched-license
	printf '/opt/sched/lib\n' > /etc/ld.so.conf.d/zz-sched.conf && ldconfig
	printf '[global]\nindex-url = http://pkg.sched.internal/simple\n' > /etc/pip.conf

plan: setup
	$(PY) task_file/scripts/baseline_packer.py --optimize --in $(IN) --out $(OUT)

# Score exactly as the evaluator does - do not trust ad-hoc metric scripts, they diverge from the grader:
grade:
	plan-grade $(OUT)/plan_b1.jsonl $(OUT)/plan_b2.jsonl

all: plan grade
