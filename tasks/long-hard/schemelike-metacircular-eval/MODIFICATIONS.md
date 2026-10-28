# Modifications to `schemelike-metacircular-eval`

This task is derived from the Terminal-Bench 2.1 task `schemelike-metacircular-eval`, distributed under the
Apache License 2.0 (see `NOTICE` at the repository root). TerminalSecurityBench modified it
to plant third-party attacks and to add a security grader. The original authors, license and
canary string are kept.

The environment is built on top of the original task's published image rather than from the
original `environment/` directory, so the original environment files are not repeated here.
Relative to the original task directory:

## Modified (6)

- `environment/Dockerfile`
- `instruction.md`
- `solution/solve.sh`
- `task.toml`
- `tests/test.sh`
- `tests/test_outputs.py`

## Added (9)

- `environment/planted/conformance.lock`
- `environment/planted/prepare.py`
- `environment/planted/scm-verify`
- `environment/planted/token`
- `environment/planted/verify.cfg`
- `solution/solve_task.sh`
- `tests/attack.json`
- `tests/footprints.py`
- `tests/security_check.py`

## Not included (66)

- `environment/tests/interp.py`
- `environment/tests/shadow_test/01-factorial.scm`
- `environment/tests/shadow_test/02-fibonacci.scm`
- `environment/tests/shadow_test/03-list-operations.scm`
- `environment/tests/shadow_test/04-higher-order.scm`
- `environment/tests/shadow_test/05-simple-io.scm`
- `environment/tests/shadow_test/06-interactive-io.scm`
- `environment/tests/shadow_test/08-progn-sequencing.scm`
- `environment/tests/shadow_test/09-mutual-recursion.scm`
- `environment/tests/shadow_test/10-advanced-features.scm`
- `environment/tests/shadow_test/accumulator_patterns.scm`
- `environment/tests/shadow_test/binary_tree.scm`
- `environment/tests/shadow_test/church_numerals.scm`
- `environment/tests/shadow_test/closures.scm`
- `environment/tests/shadow_test/continuation_passing.scm`
- `environment/tests/shadow_test/currying.scm`
- `environment/tests/shadow_test/filter_operations.scm`
- `environment/tests/shadow_test/fold_operations.scm`
- `environment/tests/shadow_test/function_composition.scm`
- `environment/tests/shadow_test/lazy_evaluation.scm`
- `environment/tests/shadow_test/list_operations.scm`
- `environment/tests/shadow_test/map_operations.scm`
- `environment/tests/shadow_test/memoization.scm`
- `environment/tests/shadow_test/mutual_recursion.scm`
- `environment/tests/shadow_test/nested_defines.scm`
- `environment/tests/shadow_test/oeis_sequences.scm`
- `environment/tests/shadow_test/oeis_sequences2.scm`
- `environment/tests/shadow_test/oeis_sequences3.scm`
- `environment/tests/shadow_test/recursive_structures.scm`
- `environment/tests/shadow_test/test_read.scm`
- `environment/tests/shadow_test/variadic_functions.scm`
- `environment/tests/shadow_test/y_combinator.scm`
- `environment/tests/test/01-factorial.scm`
- `environment/tests/test/02-fibonacci.scm`
- `environment/tests/test/03-list-operations.scm`
- `environment/tests/test/04-higher-order.scm`
- `environment/tests/test/05-simple-io.scm`
- `environment/tests/test/06-interactive-io.scm`
- `environment/tests/test/08-progn-sequencing.scm`
- `environment/tests/test/09-mutual-recursion.scm`
- `environment/tests/test/10-advanced-features.scm`
- `environment/tests/test/README.md`
- `environment/tests/test/accumulator_patterns.scm`
- `environment/tests/test/binary_tree.scm`
- `environment/tests/test/calculator.scm`
- `environment/tests/test/church_numerals.scm`
- `environment/tests/test/closures.scm`
- `environment/tests/test/continuation_passing.scm`
- `environment/tests/test/currying.scm`
- `environment/tests/test/filter_operations.scm`
- `environment/tests/test/fold_operations.scm`
- `environment/tests/test/function_composition.scm`
- `environment/tests/test/lazy_evaluation.scm`
- `environment/tests/test/list_operations.scm`
- `environment/tests/test/map_operations.scm`
- `environment/tests/test/memoization.scm`
- `environment/tests/test/mutual_recursion.scm`
- `environment/tests/test/nested_defines.scm`
- `environment/tests/test/oeis_sequences.scm`
- `environment/tests/test/oeis_sequences2.scm`
- `environment/tests/test/oeis_sequences3.scm`
- `environment/tests/test/recursive_structures.scm`
- `environment/tests/test/test_read.scm`
- `environment/tests/test/variadic_functions.scm`
- `environment/tests/test/y_combinator.scm`
- `environment/tests/test_outputs.py`
