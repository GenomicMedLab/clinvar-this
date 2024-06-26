from unittest.mock import patch

from pydantic import SecretStr
from pyfakefs.fake_pathlib import FakePathlibModule  # type: ignore
import pytest

from clinvar_this import config, exceptions

CONFIG_CONTENT = """[default]
auth_token = "MYTOKEN"
verify_ssl = true
"""


def test_config():
    short_config = config.Config(profile="default", auth_token=SecretStr("123"))
    assert (
        repr(short_config)
        == "Config(profile='default', auth_token=SecretStr('**********'), verify_ssl=True)"
    )
    long_config = config.Config(profile="default", auth_token=SecretStr("1234567890"))
    assert (
        repr(long_config)
        == "Config(profile='default', auth_token=SecretStr('**********'), verify_ssl=True)"
    )


def test_load_config_success(fs):
    fake_pathlib = FakePathlibModule(fs)

    with patch("clinvar_this.config.pathlib", fake_pathlib):
        base_path = config.pathlib.Path.home() / ".config" / "clinvar-this"
        base_path.mkdir(parents=True)
        fs.create_file(
            (base_path / "config.toml"), contents=CONFIG_CONTENT, create_missing_dirs=True
        )
        config_obj = config.load_config(profile="default")

    assert (
        repr(config_obj)
        == "Config(profile='default', auth_token=SecretStr('**********'), verify_ssl=True)"
    )


def test_load_config_fail_missing_config(fs):
    with pytest.raises(exceptions.ConfigFileMissingException):
        config.load_config(profile="default")


def test_load_config_fail_invalid_toml(fs):
    fake_pathlib = FakePathlibModule(fs)

    with patch("clinvar_this.config.pathlib", fake_pathlib):
        base_path = config.pathlib.Path.home() / ".config" / "clinvar-this"
        fs.create_file(
            (base_path / "config.toml"),
            contents=CONFIG_CONTENT + "x/asdf",
            create_missing_dirs=True,
        )
        with pytest.raises(exceptions.ConfigException) as e:
            config.load_config(profile="doesnotexist")
        assert "'Problem decoding configuration file" in repr(e)


def test_save_config_fresh(fs):
    fake_pathlib = FakePathlibModule(fs)

    with patch("clinvar_this.config.pathlib", fake_pathlib):
        base_path = config.pathlib.Path.home() / ".config" / "clinvar-this"
        config.save_config(config=config.Config(profile="default", auth_token=SecretStr("xxx")))

        with (base_path / "config.toml").open("rt") as inputf:
            config_str = inputf.read()

    assert config_str == CONFIG_CONTENT.replace("MYTOKEN", "xxx")


def test_save_config_overwrite(fs):
    fake_pathlib = FakePathlibModule(fs)

    with patch("clinvar_this.config.pathlib", fake_pathlib):
        base_path = config.pathlib.Path.home() / ".config" / "clinvar-this"
        base_path.mkdir(parents=True)
        fs.create_file(
            (base_path / "config.toml"), contents=CONFIG_CONTENT, create_missing_dirs=True
        )
        config.save_config(config=config.Config(profile="default", auth_token=SecretStr("xxx")))

        with (base_path / "config.toml").open("rt") as inputf:
            config_str = inputf.read()

    assert config_str == CONFIG_CONTENT.replace("MYTOKEN", "xxx")


def test_dump_config_success(fs_config, capsys):
    config.dump_config()

    captured = capsys.readouterr()
    assert "fake" in captured.out


def test_dump_config_no_file(fs, capsys):
    config.dump_config()

    captured = capsys.readouterr()
    assert "# no file at" in captured.out
