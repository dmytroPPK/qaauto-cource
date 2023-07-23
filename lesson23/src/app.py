import platform
import subprocess


def _get_platform_name() -> str:
    return platform.system().lower()


def _get_command(platform_name: str) -> str:
    # platform_name = _get_platform_name()
    if platform_name == "windows":
        return "ping -n {count} {website}"
    elif platform_name == "linux":
        return "ping -c {count} {website}"
    else:
        raise ValueError("Unsupported platform is detected")


def ping_websites(websites: [], count=5):
    command = _get_command(_get_platform_name())
    for website in websites:
        cmd = command.format(website=website, count=count)
        print(f"--- Ping {website} ---")
        try:
            result = subprocess.run(cmd, capture_output=True, shell=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError as error:
            print(f"Error - {error.stderr} has occurred.")


