from subprocess import CalledProcessError
import pytest
from src.app import ping_websites
from src.app import _get_command as cmd


@pytest.mark.ping
def test_ping_website(data_websites):
    ping_websites(data_websites)


@pytest.mark.get_command
def test_get_command():
    assert cmd('windows') == "ping -n {count} {website}"
    assert cmd('linux') == "ping -c {count} {website}"
    with pytest.raises(ValueError) as ex:
        cmd('bulubuntu')
    assert str(ex.value) == "Unsupported platform is detected"

