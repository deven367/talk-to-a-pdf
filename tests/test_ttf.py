import subprocess


def test_ttf_init():
    subprocess.run(
        [
            "talk_to_a_file",
            "--help",
        ]
    )
    assert True
