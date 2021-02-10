"""
This script is a sample script to show how the Sourcegraph Datadog integration
works.
"""

import time
import datadog


def main():
    """
    Main routine
    """

    options = {
        'statsd_host': '127.0.0.1',
        'statsd_port': 8125
    }
    datadog.initialize(**options)

    while True:
        datadog.statsd.increment('sg.ce.sample_metric_1',
                                 tags=['environment:mikes_laptop'])
        time.sleep(10)

main()
