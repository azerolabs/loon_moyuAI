"""Update the Loon rule list from ddgksf2013's AI rules."""

from pathlib import Path
import re
from urllib.request import Request, urlopen


SOURCE = "https://ddgksf2013.top/filter/Ai.yaml"
OUTPUT = Path(__file__).with_name("AI-Loon.list")
RULE = re.compile(r"(?:DOMAIN|DOMAIN-SUFFIX),[^\s,#]+")


def convert(source: str) -> tuple[str, int]:
    lines = [f"# Source: {SOURCE}"]
    count = 0
    for raw in source.splitlines():
        line = raw.strip()
        if line == "payload:":
            continue
        if line.startswith("- "):
            rule = line[2:]
            if not RULE.fullmatch(rule):
                raise ValueError(f"Unsupported rule: {rule}")
            lines.append(rule)
            count += 1
        elif not line or line.startswith("#"):
            lines.append(line)
        else:
            raise ValueError(f"Unexpected source line: {line}")
    if not count:
        raise ValueError("Source contains no rules")
    return "\n".join(lines).rstrip() + "\n", count


if __name__ == "__main__":
    sample, sample_count = convert("payload:\n  - DOMAIN,example.com\n  - DOMAIN-SUFFIX,example.org\n")
    assert sample_count == 2 and "payload:" not in sample and "- DOMAIN" not in sample
    request = Request(SOURCE, headers={"User-Agent": "Loon/689 CFNetwork/3860.400.51.2.6 Darwin/25.3.0", "Accept": "*/*"})
    with urlopen(request, timeout=15) as response:
        result, count = convert(response.read().decode("utf-8"))
    OUTPUT.write_text(result, encoding="utf-8", newline="\n")
    print(f"Updated {OUTPUT.name}: {count} rules")

