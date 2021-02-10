"""
This script is a sample script to show how the Sourcegraph Datadog integration
works.
"""

import random
import time
import datadog


def main():
    """
    Main routine
    """

    # configure the datadog statsd server
    options = {
        'statsd_host': '127.0.0.1',
        'statsd_port': 8125
    }
    datadog.initialize(**options)

    # loop forever (until CTRL-C)
    while True:
        datadog.statsd.increment('sg.ce.counter',
                                 tags=['environment:mikes_laptop'])
        datadog.statsd.gauge('sg.ce.gauge',
                             random.uniform(0, 100),
                             tags=['sample:' + str(random.randint(1, 10))])

        # sleep between 0 and 30s
        time.sleep(random.randint(0, 30))

# just call the main routine
if __name__ == "__main__":
    main()
