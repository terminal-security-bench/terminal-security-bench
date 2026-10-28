from tsb.limits import add_missing_limits


def test_memory_swap_processes_and_files_are_bounded():
    main = add_missing_limits({"services": {"main": {"cpus": 1.0, "mem_limit": "8192m"}}})["services"]["main"]
    assert main["memswap_limit"] == "8192m"
    assert main["mem_reservation"] == "6g"
    assert main["pids_limit"] == 4096 and main["init"] is True
    assert main["ulimits"]["nofile"] == {"soft": 65536, "hard": 65536}
    assert main["oom_score_adj"] == 500


def test_values_already_written_are_kept():
    main = {"cpus": 2.0, "mem_limit": "4g", "pids_limit": 100,
            "deploy": {"resources": {"reservations": {"memory": "2048M"}}}}
    main = add_missing_limits({"services": {"main": main}})["services"]["main"]
    assert main["pids_limit"] == 100
    assert "mem_reservation" not in main


def test_each_environment_directory_builds_from_a_context_of_its_own(tmp_path):
    from tsb.build_context import context_link

    one, two = tmp_path / "a" / "environment", tmp_path / "b" / "environment"
    one.mkdir(parents=True), two.mkdir(parents=True)
    first, second = context_link(one), context_link(two)
    assert first.name != second.name
    assert first.resolve() == one.resolve() and second.resolve() == two.resolve()
    assert context_link(one) == first

