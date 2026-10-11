"""Measure download speed by fetching the same file several times in a row."""

import argparse
import time
import urllib.request
from dataclasses import dataclass
from statistics import mean

# ESO panorama of the Milky Way seen from the Atacama desert, about 8 MB
DEFAULT_URL = "https://cdn.eso.org/images/large/eso0932a.jpg"
ATTEMPTS = 10
CHUNK_SIZE = 64 * 1024
MEGABYTE = 1_000_000


@dataclass(frozen=True)
class Probe:
    size: int
    seconds: float


def fetch(url: str) -> Probe:
    request = urllib.request.Request(url, headers={"User-Agent": "netspeed/0.1"})
    started = time.perf_counter()
    size = 0
    with urllib.request.urlopen(request, timeout=60) as response:
        while chunk := response.read(CHUNK_SIZE):
            size += len(chunk)
    return Probe(size, time.perf_counter() - started)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", nargs="?", default=DEFAULT_URL, help="file to download")
    url = parser.parse_args().url

    print(f"Target {url}")
    probes = []
    for attempt in range(1, ATTEMPTS + 1):
        probe = fetch(url)
        probes.append(probe)
        print(f"#{attempt:<2} {probe.size / MEGABYTE:7.2f} MB in {probe.seconds:6.2f} s")

    total_size = sum(p.size for p in probes)
    total_time = sum(p.seconds for p in probes)

    print()
    print(f"Average request time {mean(p.seconds for p in probes):.2f} s")
    print(f"Downloaded {total_size / MEGABYTE:.2f} MB")
    print(f"Speed {total_size / MEGABYTE / total_time:.2f} MB/s")


if __name__ == "__main__":
    main()
