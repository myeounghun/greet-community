"""A greeting community package."""


def greet(name: str) -> str:
    cleaned = name.strip()
    target = cleaned if cleaned else "world"
    return f"Hello, {target}!"
